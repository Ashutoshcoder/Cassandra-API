"""
Author : Ashutosh Kumar
Version : 1.0
Description : Generating Fake DB Data to be inserted into the database
Email : ashutoshkumardbms@gmail.com
"""

from pydbgen import pydbgen

myDB = pydbgen.pydb()

print(myDB.city_real())

for _ in range(10):
    print(myDB.realistic_email("amything something"))
