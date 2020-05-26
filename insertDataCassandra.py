"""
Author : Ashutosh Kumar
Version : 1.0
Description : Inserting Bulk Data into Cassandra
Email : ashutoshkumardbms@gmail.com
"""

# Modules imported
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

# schemes and Programs to be randomly selected
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
    "INSERT INTO hospital(h_id,h_name,h_address,h_city,h_state,h_totalbeds,h_contactNo,h_schemes_programs)"
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


# Patient Table

# Insert query
queryForPatient = SimpleStatement(
    "INSERT INTO patients(p_id,p_name,p_age,p_gender,p_admission_date,p_discharge_date,p_disease,p_treatment,p_hospital_name)"
    " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)")


# disease and treatement list for random allocation
diseases = ["Autoimmune Diseases", "Allergies & Asthma", "COVID-19", "Cancer", "Celiac Disease", "Crohn's & Colitis",
            "Heart Disease", "Infectious Diseases", "Liver Disease", "Lupus", "Multiple Sclerosis",
            "Relapsing Polychondritis", "Rheumatoid Arthritis", "Scleroderma", "Type 1 Diabetes"]

treatments = ["Back surgery (spinal surgery)", "Bad breath", "Baker's cyst", "Balloon kyphoplasty",
              "Balloon sinuplasty for chronic sinusitis", "Bariatric surgery", "Barium enema",
              "Barium swallow and barium meal", "Benign prostate treatments", "Birthmarks",
              "Bladder cancer", "Bladder investigations(cystoscopy)", "Bladder lesion removal",
              "Blood clot or thrombosis test", "Blood disorder test", "heart disease risk (cardiac testing)",
              "Blood type or blood group test", "Blurred vision", "Body Movement Therapy", "Bone density scan",
              "Cancer investigations and treatments", "Cancer tests", "Capsule endoscopy", "Cardiac catheterisation",
              "Cardiac CT scan (heart CT)", "Cardiac electrophysiology", "Cardiac MRI scan (heart MRI)",
              "Cardiomemo recording",
              ]

gender = ['Male', 'Female', 'Other']

'''
Following few lines of code is to generate the dates for admission and discharge of patients 
This will give discharge dates which is greater than admit dates 
'''

from random import randrange

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)


from datetime import datetime, timedelta

# generating 2 dates
d1 = datetime.strptime('1/1/2020 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('3/28/2020 11:59 PM', '%m/%d/%Y %I:%M %p')

for counter in range(1, 501):

    # generating Dates
    admitDate = datetime.strftime(random_date(d1, d2), "%Y-%m-%d")
    dischargeDate = datetime.strftime(random_date(d1, d2), "%Y-%m-%d")

    # Discharge Date Should always be ahead of admit date so this loop
    while dischargeDate < admitDate:
        dischargeDate = datetime.strftime(random_date(d1, d2), "%Y-%m-%d")

    # Executing query
    session.execute(queryForPatient, (counter, fake.name(), randrange(20, 100), secrets.choice(gender),
                                      admitDate, dischargeDate, secrets.choice(diseases),
                                      secrets.choice(treatments), secrets.choice(hospitals)))

# Employees Table

designation = ["Doctors", "Surgeons", "Nurse", "Therapist", "Medical Assistants",
               "Pharmacists", "Dietitian", "Medical Laboratory Technologist", "Medical Technologist", "Techs"]

queryForEmployee = SimpleStatement(
    "INSERT INTO employees(e_id,e_name,e_designation,e_age,e_gender,e_salary,e_contact_number,e_address,e_city,e_hospital_name)"
    " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

for counter in range(1, 501):
    session.execute(queryForEmployee,
                    (counter, fake.name(), secrets.choice(designation), randrange(20, 100), secrets.choice(gender),
                     randrange(50000, 100000), fake.phone_number(),
                     fake.address(), cities[randrange(0, 20)], secrets.choice(hospitals)))

print(" Data Inserted Successfully !")

""" Finally the code prints the above message after inserting data into the Database 
    Data is also generated by the code.
"""
