import csv

with open('../test_01.csv', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['uid'], row['name'], row['order_id'])
