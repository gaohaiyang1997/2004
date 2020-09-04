# !/usr/bin/env python
# -*-coding:utf8-*-
# Project_name:untitled1
# File_name:dingding.py
# Author: gao gao
# Time:2020年09月04日


import json
import requests

def message(link=1):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=9f697a1d211b4a3d8bc91594003033f3accd2cd355bb6401e46b5a31dfbf4c1c'
    pagrem = {
        "msgtype": "text",
        "text": {
            "content": "：%s " % ('铁憨憨')
        },
        "at":{
            "atMobiles":[
                "17634214826"       #需要填写自己的手机号，钉钉通过手机号@对应人
            ],
            "isAtAll":False    #是否@所有人，默认否
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    requests.post(url, data=json.dumps(pagrem), headers=headers)

if __name__ == "__main__":
    message()

















