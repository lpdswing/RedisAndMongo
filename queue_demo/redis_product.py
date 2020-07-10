import time
import json
import redis
import random
from threading import Thread

class Producer(Thread):
    def __init__(self):
        super(Producer, self).__init__()
        self.queue = redis.Redis(password='123456')

    def run(self) -> None:
        while 1:
            a = random.randint(0, 10)
            b = random.randint(90,100)
            print(f'生成2个数字{a},{b}')
            self.queue.rpush('producer', json.dumps((a,b)))
            time.sleep(2)


p = Producer()
p.start()