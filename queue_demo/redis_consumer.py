import json
import time
import redis
import random
from threading import Thread

class Consumer(Thread):
    def __init__(self):
        super(Consumer, self).__init__()
        self.queue = redis.Redis(password='123456')

    def run(self) -> None:
        while 1:
            nums = self.queue.blpop('producer')
            print(nums)
            a, b = json.loads(nums[1].decode())
            print(f'消费{a}+{b}={a+b}')
            time.sleep(random.randint(0, 10))


consumer = Consumer()

consumer.start()