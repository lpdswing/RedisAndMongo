import redis

client = redis.Redis(password='123456')


# client.lpush('demo_list','py')
# client.lpush('demo_list','go')
# client.lpush('demo_list','c++')
# client.lpush('demo_list','java')

# client.rpush('demo_list',0,2,3,5)

print(client.llen('demo_list'))  # 8
print(client.lrange('demo_list',0,8))  # [b'java', b'c++', b'go', b'py', b'0', b'2', b'3', b'5']

# print(client.lpop('demo_list')) # b'java'

client.lset('demo_list',0,'c++_put') 
