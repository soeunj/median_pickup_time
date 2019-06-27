import flask
from flask import request
from flask_pymongo import PyMongo
import json

app = flask.Flask(__name__)
# mongodb config
app.config["MONGO_URI"] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)

# route
@app.route('/median_pickup_time', methods=['GET'])
def median_pickup_time():
    # params
    location_id = request.args.get('location_id')
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    # aggregation
    pipeline = [{"$match":{"location_id":int(location_id),"iso_8601_timestamp":{"$gte":start_time, "$lte":end_time}}},\
        {"$group":{"_id":"$location_id", "median":{"$avg":"$pickup_time"}}}]
    result = {}
    for r in mongo.db.pickup_time.aggregate(pipeline):
        result['median'] = int(r['median'])
    res = json.dumps(result)
    return res

app.run()