import csv
import pprint
csvfile = open('data-text.csv','rb')
reader = csv.DictReader(csvfile)

for row in reader:
    #pprint.pprint(row)
    print row
    

