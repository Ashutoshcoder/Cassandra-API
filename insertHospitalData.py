"""
Author : Ashutosh Kumar
Version : 1.0
Description : Insert Hospital Data
Email : ashutoshkumardbms@gmail.com
"""

import secrets
from random import randrange

from cassandra.query import SimpleStatement
from cassandra.cluster import Cluster
from faker import Faker

# Connecting with Cassandra
cluster = Cluster()
session = cluster.connect('health_sector')
print("Connected ")

# Faker module for Fake Data Generation
fake = Faker()

# Hospital Table

schemes_and_programs = [[" Ayushman Bharat", "Awaz Health Insurance Scheme"],
                        ["Aam Aadmi Bima Yojana", "Bhamashah Swasthya Bima Yojana"],
                        ["Central Government Health Scheme (CGHS)"],
                        ["Chief Minister’s Comprehensive Insurance Scheme", "Employees’ State Insurance Scheme"],
                        ["Karunya Health Scheme", "Ayushman Bharat", "Awaz Health Insurance Scheme"],
                        ["Karunya Health Scheme", "Ayushman Bharat", "Awaz Health Insurance Scheme",
                         "Central Government Health Scheme (CGHS)"]
                        ]
# Insert Query

query = SimpleStatement(
    "INSERT INTO hospital2(h_id,h_name,h_address,h_city,h_state,h_totalbeds,h_contactNo,h_schemes_programs)"
    " VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")

hospitals = []
cities = []

for counter in range(1, 21):
    # Randomly Selecting Scheme for hospital
    schemes_for_this_hospital = schemes_and_programs[randrange(0, (len(schemes_and_programs) - 1))]

    # getting hospital name
    hospitals.append(fake.company())
    cities.append(fake.city())

    # inserting data
    session.execute(query, (counter, hospitals[counter - 1], fake.address(), cities[counter - 1], fake.state()
                            , randrange(500, 1000), fake.phone_number(), schemes_for_this_hospital))