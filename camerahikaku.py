# -*- coding: utf-8 -*-

import time
from time import gmtime,strftime
import picamera
import time
import grovepi
import json
import os
import boto3

#センサーが反応してからシャッターがおりるまでの時間
INTERVAL = 2
COOLDOWN = 10

#S3アップロード用変数
bucket_name = 'bfdata1'
s3_client = boto3.client('s3')

#人感センサーがD8接続
pir_sensor = 8

#センサーの設定（まだよく分かってない
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
                    print("picture print")
                    camera.capture(strfile)
                    print("upload to s3")
                    s3_client.upload_file('/home/pi/pi_farm/' + strfile , bucket_name, strfile2)
                    print("delete photo")
                    os.system('rm /home/pi/pi_farm/*.jpg')
                    result = os.system("aws rekognition detect-labels --image '{\"S3Object\":{\"Bucket\":\""+bucket_name+"\", \"Name\":\""+ strfile2 +"\"}}\' > temp.json")
                    
                    with open('temp.json') as json_data:
                        data = json.load(json_data)
                        for d in data["Labels"]:
                            if (d["Name"] == "Human" and d["Confidence"] > 55.0):
                            
                                print ("Human found: " + str(d["Confidence"]))
                                
                                result2 = os.system("aws rekognition search-faces-by-image --image '{\"S3Object\":{\"Bucket\":\""+bucket_name+"\", \"Name\":\""+ strfile2 +"\"}}\' --collection-id \"bf\" > hikaku.json")
                                with open('hikaku.json') as json_data:
                                    data = json.load(json_data)
                                    for d in data["Labels"]:
                                        if (d["ExternalImageId"] == "kodani" and d["Confidence"] > 55.0):
                                            print ("kodani found: " + str(d["Confidence"]))
                                            #ここから修正os.system(aws s3 mv s3://bfdata1/raspberry_pi_camera/kojinbetu/kodani/kodani_sample.jpg s3://bfdata1/raspberry_pi_camera/kojinbetu/okuno/
                                        
                                break
                        else:
                            s3_client.delete_object(Bucket=bucket_name, Key=strfile2)
                            
            #time.sleep(INTERVAL)
            
os.system('rm /home/pi/pi_farm/*.json')
