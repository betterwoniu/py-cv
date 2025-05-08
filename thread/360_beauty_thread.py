# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 16:05
# @File    : 360_beauty.py
# @Software: PyCharm

import  requests
import re
import json
import os
import threading
import time


def downloadBeauty(url:str):
  imgDir = '360_beauty_img'
  if not os.path.exists(imgDir):
    os.mkdir(imgDir)
  fileName = url.split('/')[-1]
  result = requests.get(url)
  with open(os.path.join(imgDir, fileName), 'wb') as f:
    f.write(result.content)

def main():
    result = requests.get('https://image.so.com/j?callback=jQuery183006499542355427201_1746675769138&q=%E7%BE%8E%E5%A5%B3&qtag=%E4%B8%AD%E5%9B%BD&pd=1&pn=60&correct=%E7%BE%8E%E5%A5%B3&adstar=0&tab=all&sid=5df485bcb38f82b9e71df181b61a81b8&ras=0&cn=0&gn=0&kn=0&crn=0&bxn=0&cuben=0&pornn=0&manun=0&src=srp&sn=600&ps=595&pc=60&_=1746678902657')
    if(result.status_code == 200):
        match = re.search(r'\(\{.*?\}\)', result.text)
        json_dirt = json.loads(match.group(0)[1:-1]) if match else ''
        img_list = json_dirt['list']
        print('开始下载图片...，此次共下载%s张图片' % len(img_list))
        threads = []
        for img in img_list:
            t = threading.Thread(target=downloadBeauty, args=(img['thumb'],))
            t.start()
        for t in threads:
              t.join()

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print('下载完成，耗时%.2f秒' % (end_time - start_time))