import redis 

def listener_messages():
    r=redis.Redis(host='localhost', port=6379, db=0)
    pub=r.pubsub()
    pub.subscribe('radio_station')
    for item in pub.listen():
        if item['type'] == 'message':
            print(item['data'].decode('utf-8'))
        else:
            print(item)
        if item['type']=='message':
            print(item['data'].decode('utf-8'))


    r.close()


if __name__ == '__main__':
    listener_messages()
