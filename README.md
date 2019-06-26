# Requirments

For running this api, please install below items:
- MongoDB '3.6.x'~
- Flask '0.12.x'~
- Python '3.x.x'~


After installations, please download csv file as 'pickup_times.csv' through this link: http://summer2019.wolt.com/Helsinki/pickup_times.csv


Run the mongodb:
```
mongod
```


Run this command to import csv file to mongodb:
```
mongoimport --db <<your db>> --collection pickup_time --type csv --file <<pickup_times.csv file path>> --headerline
```
or
```
mongoimport --db <<your db>> --collection pickup_time --type csv --fields <<fields in pickup_times.csv>> --file <<pickup_times.csv file path>>
```


After importing data, clone this repository and run below command to run the app.
```
python api.py
```
