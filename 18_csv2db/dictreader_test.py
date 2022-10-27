import csv

with open('courses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    inlist = []
    for row in reader:
        inlist.append(row['code'],)
        print(row['code'], row['mark'], row['id'])
    print(reader)