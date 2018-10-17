# -*- coding: utf-8 -*-

import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages/')
import fitbit
from ast import literal_eval

# ��������ID��
CLIENT_ID =  "22D8LY"
CLIENT_SECRET  = "2067adb0d0e86d9f6c076c453e702121"
TOKEN_FILE    = "token.txt"

tokens = open(TOKEN_FILE).read()
token_dict = literal_eval(tokens)
ACCESS_TOKEN = token_dict['access_token']
REFRESH_TOKEN = token_dict['refresh_token']

def updateToken(token):
    f = open(TOKEN_FILE, 'w')
    f.write(str(token))
    f.close()
    return

# �擾���������t
DATE = "2018-10-10"

# ID���̐ݒ�
authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET
                             ,access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN, refresh_cb = updateToken)
# �S�������擾�i1�b�P�ʁj
#data_sec = authd_client.intraday_time_series('activities/heart', DATE, detail_level='1sec', start_time="02:00", end_time="04:00") #'1sec', '1min', or '15min'
#heart_sec = data_sec["activities-heart-intraday"]["dataset"]
#print(heart_sec)

#�������擾(1���P�ʁj
#data2_sec = authd_client.intraday_time_series('activities/steps', base_date="2018-10-10", detail_level='1min', start_time="02:00", end_time="04:00") #'1sec', '1min', or '15min'
#steps_sec = data2_sec["activities-steps-intraday"]["dataset"]
#print(steps_sec)

#�����Ă��鎞��(1���P��)
data3_sec = authd_client.intraday_time_series('activities/minutesSedentary', base_date="2018-10-10", detail_level='15min', start_time="02:00", end_time="04:00") #'1sec', '1min', or '15min'
print(data3_sec)

#����
data4_sec = authd_client.bp(date="2018-10-10") #'1sec', '1min', or '15min'
print(data4_sec)
