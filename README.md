# Instruction

For running this api, please install below items:
- MongoDB '3.6.x'~
- Flask '0.12.x'~
- Python '3.x.x'~


After installations, please download csv file through this link: http://summer2019.wolt.com/Helsinki/pickup_times.csv and save the file as 'pickup_times.csv'


Run the mongodb:
```
mongod
```


Run the command to import csv file to mongodb:

(If you prefer to use different database and collection name, please change them in both below command and mongodb config part in api.py)
```
mongoimport --db test --collection pickup_time --type csv --file <<pickup_times.csv file path>> --headerline
```
or
```
mongoimport --db test --collection pickup_time --type csv --fields <<fields in pickup_times.csv>> --file <<pickup_times.csv file path>>
```


After importing data, clone this repository and run the command to run the app:
```
python api.py
```


To test this api:
```
HTTP GET /median_pickup_time?location_id=12&start_time=2019-01-09T11:00:00&end_time= 2019-01-09T12:00:00
```
