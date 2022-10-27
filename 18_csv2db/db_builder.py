#SJS: Shinji, Jeremy and Sebastian
#SoftDev  
#K18 -- SQLite in Python
#2022-10-26

#TODO: figure out how to run the python code multiple times without adding duplicate information into the tables

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
with open('courses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    c.execute("CREATE TABLE IF NOT EXISTS courses(code TEXT, mark INTEGER, id INTEGER)")    
    for row in reader:
        c.execute("INSERT INTO courses values (?, ?, ?)", [row['code'], row['mark'], row['id']])
        
info = c.execute("select * from courses;")  
print(info)

with open('students.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    c.execute("CREATE TABLE IF NOT EXISTS students(name TEXT, age INTEGER, id INTEGER PRIMARY KEY)")
    tolist = [(row['name'], row['age'], row['id']) for row in reader] # Adds every row in the csv into a list/tuple, which can be fed as an argument in the next line
    c.executemany("INSERT INTO students values (?, ?, ?)", tolist)
    
command = "SELECT * from students"          # test SQL stmt in sqlite3 shell, save as string

info = c.execute(command).fetchall()    # run SQL statement
print(info)

#==========================================================

db.commit() #save changes
db.close()  #close database


