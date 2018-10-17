# -*- coding: utf-8 -*-

import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages/')
import fitbit
from ast import literal_eval

# メモしたID等
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

# 取得したい日付
DATE = "2018-10-10"

# ID等の設定
authd_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET
                             ,access_token=ACCESS_TOKEN, refresh_token=REFRESH_TOKEN, refresh_cb = updateToken)
# 心拍数を取得（1秒単位）
#data_sec = authd_client.intraday_time_series('activities/heart', DATE, detail_level='1sec', start_time="02:00", end_time="04:00") #'1sec', '1min', or '15min'
#heart_sec = data_sec["activities-heart-intraday"]["dataset"]
#print(heart_sec)

#歩数を取得(1分単位）
#data2_sec = authd_client.intraday_time_series('activities/steps', base_date="2018-10-10", detail_level='1min', start_time="02:00", end_time="04:00") #'1sec', '1min', or '15min'
#steps_sec = data2_sec["activities-steps-intraday"]["dataset"]
#print(steps_sec)

#座っている時間(1分単位)
data3_sec = authd_client.intraday_time_series('activities/minutesSedentary', base_date="2018-10-10", detail_level='15min', start_time="02:00", end_time="04:00") #'1sec', '1min', or '15min'
print(data3_sec)

#血圧
data4_sec = authd_client.bp(date="2018-10-10") #'1sec', '1min', or '15min'
print(data4_sec)
