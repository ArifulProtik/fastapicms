import redis

class Getredis:
    def getClient():
        try:
            r = redis.Redis("localhost")
        except Exception as E:
            raise ValueError(E)
        return r
        
        