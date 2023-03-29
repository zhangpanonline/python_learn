from redis import Redis

redis_cli = Redis(host="localhost", port=6379, db=0)

redis_cli.set('name', 'it')

name = redis_cli.get('name')
print(name)

redis_cli.delete('name')
name = redis_cli.get('name')
print(name)
