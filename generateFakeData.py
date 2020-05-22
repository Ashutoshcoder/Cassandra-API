"""
Author : Ashutosh Kumar
Version : 1.0
Description : Generate Fake Data for Cassandra
Email : ashutoshkumardbms@gmail.com
"""
import secrets

from faker import Faker
from random import randrange
import random

fake = Faker()

foo = ['Male', 'Female', 'Other']

'''

hospital_name = []
hospital_address = []
hospital_city = []
hospital_zipcode = []


for _ in range(20):
    hospital_address.append(fake.address())
    hospital_name.append(fake.company())
    hospital_city.append(fake.city())
    hospital_zipcode.append(fake.zipcode())

print(hospital_name)
print(hospital_address)
print(hospital_city)
print(hospital_zipcode)

'''

designation = ["Doctors", "Surgeons", "Nurse", "Therapist", "Medical Assistants",
               "Pharmacists", "Dietitian", "Medical Laboratory Technologist", "Medical Technologist", "Techs"]

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
'''
for _ in range(5):
    # salary print(randrange(10000,100000))
    # age  print(randrange(25, 70))
    # designation print(secrets.choice(designation))
    # print(secrets.choice(diseases))
    # print(secrets.choice(treatments))
    print(secrets.choice(foo))
'''

print()