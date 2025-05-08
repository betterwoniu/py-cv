# !/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
# class DownloadFile(Thread):
#     def __init__(self, url, fileName):
#         Thread.__init__(self)
#         self.url = url
#         self.fileName = fileName
#     def run(self):
#         print("开始下载：" + self.fileName)
#         time.sleep(10)

def downloadFile(url, fileName):
    print("开始下载：" + fileName)
    time.sleep(10)
def main():
  start = time.time()
  # threads = [
  #   DownloadFile("https://www.baidu.com/", "baidu.html"),
  #   DownloadFile("https://www.taobao.com/", "taobao.html"),
  #   DownloadFile("https://www.jd.com/", "jd.html")
  # ]

  
  # threads = [
  #   Thread(target=downloadFile, args=("https://www.baidu.com/", "baidu.html")),
  #   Thread(target=downloadFile, args=("https://www.taobao.com/", "taobao.html")),
  #   Thread(target=downloadFile, args=("https://www.jd.com/", "jd.html"))
  # ]
  
  # for t in threads:
  #   t.start()
  # for t in threads:
  #   t.join()


  # with ThreadPoolExecutor(max_workers=4) as executor:
  #   for i in range(3):
  #     executor.submit(downloadFile, "https://www.baidu.com/", "baidu.html")

  # for i in range(3):
  #   downloadFile("https://www.baidu.com/", "baidu.html")
      

    
  end = time.time()
  print("下载完成，耗时：" + str(end - start))
  

if __name__ == '__main__':
    main()
    print("主线程结束")