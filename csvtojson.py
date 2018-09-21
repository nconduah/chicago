import csv
import json

csvfile = open('boston2015ToPresentCrime2.csv', 'r',encoding="latin-1")
jsonfile = open('boston2015ToPresentCrime.json', 'w')

fieldnames = ("INCIDENT_NUMBER","OFFENSE_CODE","OFFENSE_CODE_GROUP","OFFENSE_DESCRIPTION","DISTRICT","REPORTING_AREA","SHOOTING","OCCURRED_ON_DATE","YEAR","MONTH","DAY_OF_WEEK","HOUR","UCR_PART","STREET","Lat","Long","Location")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')