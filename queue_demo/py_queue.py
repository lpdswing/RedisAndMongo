# 简单的生产者 消费者
import time
import random
from queue import Queue
from threading import Thread


class Producer(Thread):
    '''生产者'''
    def __init__(self, queue: Queue):
        super(Producer, self).__init__()
        self.queue = queue

    def run(self) -> None:
        while 1:
            a = random.randint(0, 10)
            b = random.randint(90, 100)
            print(f'生成2个数字{a},{b}')
            self.queue.put((a, b))
            time.sleep(2)


class Consumer(Thread):
    '''消费者'''
    def __init__(self, queue: Queue):
        super(Consumer, self).__init__()
        self.queue = queue

    def run(self) -> None:
        while 1:
            nums = self.queue.get(block=True)  # 队列为空则阻塞,直到队列有数据
            sum_a_b = sum(nums)
            print(f'消费者消费了数据,{nums[0]}+{nums[1]}={sum_a_b}')
            time.sleep(random.randint(0, 10))


queue = Queue()
producer = Producer(queue)
consumer = Consumer(queue)
producer.start()
consumer.start()