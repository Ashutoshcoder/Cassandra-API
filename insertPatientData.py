"""
Author : Ashutosh Kumar
Version : 1.0
Description : Insert Patient Data
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

queryForPatient = SimpleStatement(
    "INSERT INTO patients(p_id,p_name,p_age,p_gender,p_admission_date,p_discharge_date,p_disease,p_treatment,p_hospital_name)"
    " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)")

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

d1 = datetime.strptime('1/1/2020 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('3/28/2020 11:59 PM', '%m/%d/%Y %I:%M %p')

for counter in range(1, 501):

    # generating Dates
    admitDate = datetime.strftime(random_date(d1, d2), "%Y-%m-%d")
    dischargeDate = datetime.strftime(random_date(d1, d2), "%Y-%m-%d")

    # Discharge Date Should always be ahead of admit date so this loop
    while dischargeDate < admitDate:
        dischargeDate = datetime.strftime(random_date(d1, d2), "%Y-%m-%d")

    session.execute(queryForPatient, (counter, fake.name(), randrange(20, 100), secrets.choice(gender),
                                      admitDate, dischargeDate, secrets.choice(diseases),
                                      secrets.choice(treatments), secrets.choice(hospitals)))
