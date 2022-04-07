from boot.config import db
from classes.csvReader.csvReaderFactory.PondasFactory import PondasFactory
import sys
import classes.translate.google as google

# Create table of csv data in postgresql
res = db.execute_query('''CREATE TABLE IF NOT EXISTS people (
    id serial primary key,
    age integer,
    workclass varchar(255),
    fnlwgt integer,
    education varchar(255),
    education_num integer,
    marital_status varchar(255),
    occupation varchar(255),
    relationship varchar(255),
    race varchar(255),
    sex varchar(255),
    capital_gain integer,
    capital_loss integer,
    hours_per_week integer,
    native_country varchar(255),
    salary varchar(255),
    persian_native_country varchar(255)
);''', "write");

# print success message if the query was successful
if res["status"] == "success":
    print("successful installation!")

data = PondasFactory(".././adult_data.csv")
res = data.createReader().get_data()

# for res and insert into the database
for index, row in res.iterrows():
    db.execute_query('''INSERT INTO people 
        (
            age ,
            workclass,
            fnlwgt ,
            education,
            education_num ,
            marital_status,
            occupation,
            relationship,
            race,
            sex,
            capital_gain ,
            capital_loss ,
            hours_per_week ,
            native_country,
            salary,
            persian_native_country
        ) VALUES (%s, '%s', %s, '%s', %s, '%s', '%s', '%s', '%s', '%s', %s, %s, %s, '%s', '%s', '%s') ''' % 
        (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12] ,row[13], row[14], google.translate(row[13], "fa")), "write")

    # progress precentage
    sys.stdout.write("\r%d%%" % (index / len(res) * 100))
    sys.stdout.flush()

print("\n import csv to postgreSQL has done!")

# close the connection
db.close()
