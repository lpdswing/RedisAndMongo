# set
import json

import redis

client = redis.Redis(password='123456')

client.sadd('demo_set','py','java',22,'c++')

print(client.scard('demo_set'))  # 查看条数

# print(client.spop('demo_set',2))  #[b'java', b'py']

# print(client.smembers('demo_set'))  #{b'c++', b'22'}

# client.srem('demo_set','c++')
# print(client.smembers('demo_set'))  # {b'py', b'java', b'22'}  删除数据


client.sadd('demo_set1','py','java',322,'c++','gggg')
print(client.sinter('demo_set','demo_set1'))  # 交集
print(client.sunion('demo_set','demo_set1'))  # 并集
print(client.sdiff('demo_set1','demo_set'))  # 差集  {b'322', b'gggg'}

#求差集时，参数的顺序是很重要的，最后的结果是用第1个Key对 应的集合中的数据扣除后面的Key对应的集合中的数据。