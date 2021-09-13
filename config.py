import redis as redis

PROJECT_PATH = '/home/artem/PycharmProjects/igor_server/'
PROJECT_FOLDER = PROJECT_PATH.split('/')[-2]


# MEM CACHE SERVER
MEMORY_CACHE = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# MEM CACHE CONST
MEM_USERS = 'users'

# Logging
# LOG_PATH = PROJECT_PATH + 'log'
# GENERAL_LOG = 'general'
