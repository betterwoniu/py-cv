# !user/bin/env python3
# -*- coding:utf-8 -*-

import  threading
import  time
from concurrent.futures import ThreadPoolExecutor

class Account(object):
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance
        # self.lock = threading.Lock()

    def add_balance(self, money):
        # self.lock.acquire()
        try:
            tmp = self.balance
            tmp += money
            time.sleep(0.1)
            self.balance = tmp
        finally:
            # self.lock.release()
            pass



def main():
    account = Account('123456789', 1000)

    
    # threads = []
    # for i in range(100):
    #     t = threading.Thread(target=account.add_balance, args=(1,))
    #     threads.append(t)
    #     t.start()
    # for  t in threads:
    #     t.join()

    ThreadPoolExecutor  = ThreadPoolExecutor(max_workers=10)
    with ThreadPoolExecutor(max_workers=4) as executor:
        for i in range(100):
            executor.submit(account.add_balance, 1)
    print(account.balance)





if __name__ == '__main__':
    main()