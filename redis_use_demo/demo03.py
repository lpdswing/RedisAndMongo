import json

import redis

client = redis.Redis(password='123456')

def send_sms(phone):
    return True

client.lpush('phone_queue',json.dumps({'phone_number': 12345678}))

while 1:
    phone_infos_byte = client.lpop('phone_queue')
    if not phone_infos_byte:
        print('短信发送完毕')
        break
    phone_infos = json.loads(phone_infos_byte)
    retry_times = phone_infos.get('retry_times', 0)
    phone_number = phone_infos['phone_number']
    result = send_sms(phone_number)
    if result:
        print(f'手机号{phone_number}发送成功')
        continue
    if retry_times >= 3:
        print(f'重试超过3次,放弃{phone_number}')
        continue
    next_phone_info = {
        'phone_number':phone_number,
        'retry_times':retry_times+1
    }
    client.rpush('phone_queue', json.dumps(next_phone_info))