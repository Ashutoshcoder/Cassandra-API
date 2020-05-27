"""
Author : Ashutosh Kumar
Version : 1.0
Description : 
Email : ashutoshkumardbms@gmail.com
"""
from random import randrange

from cassandra.query import SimpleStatement
from cassandra.cluster import Cluster
from faker import Faker

fake = Faker()

# Connecting with Cassandra
cluster = Cluster()
session = cluster.connect('health_sector')
print("Connected ")

query = SimpleStatement("INSERT INTO hospital(h_id,h_name,h_livebeds)"
                        "VALUES (%s,%s,%s)")

for counter in range(1, 21):
    session.execute(query, (counter,fake.company(), randrange(100, 500)))
