"""
Author : Ashutosh Kumar
Version : 1.0
Description : Insert Employee Data
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
hospitals = ['A', 'B', "C", 'AA', 'BB', "CC"]
gender = ['Male', 'Female', 'Other']
designation = ["Doctors", "Surgeons", "Nurse", "Therapist", "Medical Assistants",
               "Pharmacists", "Dietitian", "Medical Laboratory Technologist", "Medical Technologist", "Techs"]

queryForEmployee = SimpleStatement(
    "INSERT INTO employees(e_id,e_name,e_designation,e_age,e_gender,e_salary,e_contact_number,e_address,e_city,e_hospital_name)"
    " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

for counter in range(1, 101):
    session.execute(queryForEmployee,
                    (counter, fake.name(), secrets.choice(designation), randrange(20, 100), secrets.choice(gender),
                     randrange(50000, 100000), fake.phone_number(),
                     fake.address(), fake.city(), secrets.choice(hospitals)))
