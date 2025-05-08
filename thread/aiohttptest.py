#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import time, threading
import aiohttp
import asyncio

start_time = time.time()  # 记录开始时间
threads = []

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',}
url = 'https://dh5.cntv.lxdns.com/asp/h5e/hls/1200/0303000a/3/default/6eab8e206f4d4f189be93cce3ae24574/1200.m3u8'
###下载ts文件
resp = requests.get(url, headers=headers)

print(resp.text)
tsList = re.findall(r'^[^#].*\.ts$', resp.text,re.MULTILINE)

print(tsList)

async def downloadTs(session,ts):
  # result = requests.get('https://dh5.cntv.lxdns.com/asp/h5e/hls/1200/0303000a/3/default/6eab8e206f4d4f189be93cce3ae24574/'+ts)
  # with open(ts, 'wb') as f:
  #   f.write(result.content)

  async with session.get('https://dh5.cntv.lxdns.com/asp/h5e/hls/1200/0303000a/3/default/6eab8e206f4d4f189be93cce3ae24574/'+ts) as response:
    with open(ts, 'wb') as f:
      while True:
        chunk = await response.content.read(1024)
        if not chunk:
          break
        f.write(chunk)

async def main():
  async with aiohttp.ClientSession() as session:
      tasks = []
      for ts in tsList:
        task = asyncio.create_task(downloadTs(session, ts))
        tasks.append(task)
      await asyncio.gather(*tasks)


asyncio.run(main())
end_time = time.time()  # 记录结束时间
elapsed_time = end_time - start_time  # 计算运行时间（秒）

print(f"程序运行时间: {elapsed_time:.4f} 秒")  # 