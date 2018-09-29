import time
from time import gmtime,strftime
import picamera
import time
import grovepi
import json
import os
import boto3

INTERVAL = 2
COOLDOWN = 10

bucket_name = 'bfdata1'
s3_client = boto3.client('s3')

pir_sensor = 8
motion=0
grovepi.pinMode(pir_sensor,"INPUT")
time.sleep(INTERVAL) 
while True:
        motion=grovepi.digitalRead(pir_sensor)
        if motion==0 or motion==1:
            if motion==1:
                print("shutter now")
                with picamera.PiCamera() as camera:
                    camera.resolution = (1024,768) 
                    camera.start_preview()                   
                    strf = strftime("%Y%m%d-%H:%M:%S")
                    strfile = strf + '.jpg'
                    strfile2 = 'raspberry_pi_camera/' + strfile
                    camera.capture(strfile)
                    s3_client.upload_file('/home/pi/pi_farm/' + strfile , bucket_name, strfile2)
                    os.system('rm /home/pi/pi_farm/*.jpg')
                    result = os.system("aws rekognition detect-labels --image '{\"S3Object\":{\"Bucket\":\""+bucket_name+"\", \"Name\":\""+ strfile2 +"\"}}\' > temp.json")
                    
                    with open('temp.json') as json_data:
                        data = json.load(json_data)
                        for d in data["Labels"]:
                            if (d["Name"] == "Human" and d["Confidence"] > 55.0):
                            
                                print ("Human found: " + str(d["Confidence"]))
                                break
                        else:
                            s3_client.delete_object(Bucket=bucket_name, Key=strfile2)
                            
            #time.sleep(INTERVAL)
            
os.system('rm /home/pi/pi_farm/* temp.json')
