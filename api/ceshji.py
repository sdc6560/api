import redis

conn=redis.Redis(host='192.168.11.151',port=6379)
#设置值

conn.set('sudc_name','于超')


val= conn.get('sudc_name').decode('utf-8')


print(val)