import redis

def main():
    # connecting redis server
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


    # setting key value pair
    r.set('user:name','manan')
    name=r.get('user:name')
    print(name)


    # storing data into a hash
    r.hset('user:profile',mapping={
        'name':'manan',
        'age':25,
        'city':'NYC'
    })

    # retrieving data from a hash
    profile=r.hgetall('user:profile')
    print(f"USER PROFILE DETAIL : {profile}")


    # creating temporary key 
    r.setex('otp:1234',10,'8999')
    print(f"OTP GENERATED : 8999, EXPIRES IN 10 SECONDS")
    print(f"TIME REMAINING : {r.ttl('otp:1234')} SECONDS LEFT")

if __name__ == '__main__':
    main()



