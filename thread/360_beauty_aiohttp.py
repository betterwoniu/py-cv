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
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import aiofiles
import os
from urllib.parse import urljoin
from aiofiles import open as aio_open

async def downloadBeauty(session: aiohttp.ClientSession,url:str):

  img_dir = '360_beauty_img'
  if not os.path.exists(img_dir):
    os.mkdir(img_dir)
  async with session.get(url) as response:
    file_name = url.split('/')[-1]
    async with aio_open(os.path.join(img_dir, file_name), 'wb') as f:
        await f.write(await response.read())

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://image.so.com/j?callback=jQuery183006499542355427201_1746675769138&q=%E7%BE%8E%E5%A5%B3&qtag=%E4%B8%AD%E5%9B%BD&pd=1&pn=60&correct=%E7%BE%8E%E5%A5%B3&adstar=0&tab=all&sid=5df485bcb38f82b9e71df181b61a81b8&ras=0&cn=0&gn=0&kn=0&crn=0&bxn=0&cuben=0&pornn=0&manun=0&src=srp&sn=600&ps=595&pc=60&_=1746678902657') as response:
            if response.status == 200:
                text = await response.text()
                match = re.search(r'\(\{.*?\}\)',text)
                json_dirt = json.loads(match.group(0)[1:-1]) if match else ''
                img_list = json_dirt['list']
                tasks = []
                # tasks = [downloadBeauty(session,img['thumb']) for img in img_list]
                for  img in img_list:
                    tasks.append(downloadBeauty(session,img['thumb']))

                await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print('图片下载完成，耗时%.2f秒' % (end_time - start_time))



