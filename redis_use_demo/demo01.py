import redis

client = redis.Redis(password='123456')

# print(client.keys())

# 创建字符串
client.set('key1','demo1')
print(client.get('key1'))

client.set('key1','demo2',nx=True) # 如果key存在,则不会覆盖原有数据
print(client.get('key1'))

client.append('key1',' and demo2')
print(client.get('key1'))

client.set('n1',0)
print(client.get('n1'))
client.incr('n1')
client.incr('n1',3)
print(client.get('n1'))



