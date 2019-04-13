from poloniex_api import Poloniex
import time
import threading


class DataGetter:
    secret = 'f88120222685903f42e571e2803ee4571838f257499bec38a051cdccbeb3f6f0914447b59608657dce7d4aecd4f' \
             '3320c1ebb9d0fe85b9c948291cf1f8df0a711'
    api_key = 'NS5AVY72-ZSKQ0HJ2-7K9SMTW0-V3FV425I'

    my_polo = Poloniex(
        API_KEY=api_key,
        API_SECRET=secret
    )

    def update(self, data):
        # self.data_buffer.update(data)
        # return
        # О блокировках http://www.quizful.net/post/thread-synchronization-in-python
        lock = threading.Lock()
        lock.acquire()
        self.data_buffer.update(data)
        lock.release()
        # lock.acquire()
        # try:  # release data in any case? try-finally too long, there is no need just for copying
        #     self.data_buffer.update(data)
        # finally:
        #     lock.release()

    def get_btc_usdt(self):
        res = {'USDT_BTC': self.my_polo.returnTicker()['USDT_BTC']}
        self.update(res)
        return res

    def get_btc_eth(self):
        res = {'BTC_ETH': self.my_polo.returnTicker()['BTC_ETH']}
        self.update(res)
        return self.data_buffer['BTC_ETH']

    def __init__(self):
        self.data_buffer = {}  # Buffer for results to extract from ThreadHandler/Gui

if __name__ == '__main':
    balances = DataGetter.my_polo.returnBalances()
    print('BALANCES', balances)

    ticker = DataGetter.my_polo.returnTicker()
    print('TICKER', ticker)

    def listen(self):
        while True:
            time.sleep(1)
            print('TICKER: BTC_ETH =', DataGetter().my_polo.returnTicker()['BTC_ETH'])

    listen()