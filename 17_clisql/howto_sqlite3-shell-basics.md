SJS: Shinji, Jeffery, Sebastian

SoftDev

K17 -- SQLite How-To

2022-24-10

time spent: .5hrs


DISCOS:

* Utilize databases for long sets of data through making specific categories of data accessible and visible
* Use queries to find items that have specific values


# how-to :: SQLite3 Shell Basics
---
## Overview
This how-to will teach how to do the basics in SQLite3, which is used to create data files. 
This guide will go through creating tables, inserting data, and accessing that data.

### Estimated Time Cost: 0.1 hrs (round to nearest 0.1)

### Prerequisites:
- Install SQLite3


1. Create a file for data
2. Create a table 
NOTE: Semicolon (;) required after each statement
```
CREATE TABLE <name> (<column name> <data type>, ...);
```
a. Can put in different data types (TEXT, INTEGER, REAL, NUMERIC, BLOB)

b. Column can be PRIMARY KEY  (every entry is unique & != NULL) or NOT NULL (No entry == NULL)

3. Insert data into table
```
INSERT INTO <tbl_name> VALUES ( <field 1>, <field 2> ...)
```

4. Get values from entries
```
SELECT * FROM <tbl_name>;
SELECT <field_name> FROM <tbl_name>;
```

a. Use * to get all fields from that table
b. Use <field_name> to get a single field

### Resources
* [Mr. Mykolyk's readme](https://github.com/stuy-softdev/notes-and-code/blob/main/smpl/k17-18sqlite/readme.md)
* [SQLite Documentation](https://www.sqlite.org/cli.html)
---

Accurate as of (last update): 2022-10-24

#### Contributors:  
Jeffery, pd8  
Sebastian, pd8  
Shinji, pd8  


