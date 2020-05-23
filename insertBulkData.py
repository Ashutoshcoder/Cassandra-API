"""
Author : Ashutosh Kumar
Version : 1.0
Description : Inserting Bulk Data into Cassandra
Email : ashutoshkumardbms@gmail.com
"""

from time import sleep
from cassandra.query import SimpleStatement
from cassandra.cluster import Cluster
from faker import Faker

fake = Faker()
names = []
email = []
address = []
empid = []
phone = []

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

print(random_date(d1, d2))

for i in range(1, 6):
    names.append(fake.name())
    empid.append(i)
    email.append(fake.email())
    phone.append(fake.phone_number())

cluster = Cluster()
session = cluster.connect('dbrnd')
print("Connected ")

query = SimpleStatement(
    "INSERT INTO tbl_employee (empid, empfirstname, emplastname,empsalary,dateofemp,dateofdischarge) VALUES (%s, %s, %s,%s,%s,%s)")

for i in range(0, 5):
    admitDate = datetime.strftime(random_date(d1, d2), "%Y-%m-%d")
    dischargeDate = datetime.strftime(random_date(d1, d2), "%Y-%m-%d")

    # Discharge Date Should always be ahead of admit date so this loop
    while dischargeDate < admitDate:
        dischargeDate = datetime.strftime(random_date(d1, d2), "%Y-%m-%d")

    print(admitDate, dischargeDate)
    session.execute(query, (empid[i], names[i], email[i], empid[i] * 10000, admitDate, dischargeDate))
    # sleep(1)

rows = session.execute('SELECT * FROM tbl_employee ;')
for user_row in rows:
    print(user_row.empid, user_row.empfirstname, user_row.emplastname, user_row.empsalary)
