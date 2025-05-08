# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 16:05
# @File    : 360_beauty.py
# @Software: PyCharm

import requests
import re
import json 
import os
import time

def downloadBeauty(url:str):
    result = requests.get(url)
    imgDir = '360_beauty_img'
    if not os.path.exists(imgDir):
        os.mkdir(imgDir)
    fileName  = url.split('/')[-1]
    with open(os.path.join(imgDir, fileName), 'wb') as f:
        f.write(result.content)
def main():
    result = requests.get('https://image.so.com/j?callback=jQuery183006499542355427201_1746675769138&q=%E7%BE%8E%E5%A5%B3&qtag=%E4%B8%AD%E5%9B%BD&pd=1&pn=60&correct=%E7%BE%8E%E5%A5%B3&adstar=0&tab=all&sid=5df485bcb38f82b9e71df181b61a81b8&ras=0&cn=0&gn=0&kn=0&crn=0&bxn=0&cuben=0&pornn=0&manun=0&src=srp&sn=600&ps=595&pc=60&_=1746678902657')
    if(result.status_code == 200):
      match = re.search(r'\(\{.*?\}\)', result.text)
      json_dirt = json.loads(match.group(0)[1:-1]) if match else ''
      length = len(json_dirt['list'])
      print('开始下载360美女图片，共计%s张图片' % length)
      for i in json_dirt['list']: 
        url = i['thumb']
        downloadBeauty(url)

if __name__ == '__main__':
    startTime = time.time()
    main()
    endTime = time.time()
    print('耗时：', endTime - startTime)
