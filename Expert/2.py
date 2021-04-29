#Write a Python code to configure the MySQL Connector in your system and Insert data to MySQL Table after which you Fetch and Display data from Table

import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root@123',
    database='memoir'
)

mycursor = database.cursor()

mycursor.execute("INSERT INTO `tdm_sample_resume` (`sampleResumeId`, `title`, `fontSize`, `fontFamily`, `template`, `createdAt`, `updatedAt`) VALUES (NULL, 'Full Stack Developer', '0', '0', '0', now(), now());")

mycursor.execute("SELECT * FROM tdm_sample_resume")

myresult = mycursor.fetchall()

for r in myresult :
    print(r)