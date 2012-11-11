import ConfigParser
#import hashlib
import subprocess
import json
from pymongo import Connection

# Grab the info from the config
config = ConfigParser.ConfigParser()
config.read("server.cfg")

# Server Configs
host       = config.get('Server','host')
port       = config.getint('Server','port')
backlog    = 5
size       = 1024

# MongoDB Configs
mongo_host = config.get('Mongo', 'host')
mongo_port = config.getint('Mongo', 'port')
mongo_db = config.get('Mongo', 'database')
connection = Connection(mongo_host, mongo_port)
db         = connection[mongo_db]

# Crypto Config
#salt = config.get('Crypto', 'salt')

while 1:
    test = subprocess.Popen(["python", "test.py"], stdout=subprocess.PIPE)
    output = test.communicate()[0]
    try:
        json_result = json.loads(output)
        print json_result
    except:
        continue # keep scanning, no results