from flask import Flask, Response, jsonify
from pyArango.connection import *
import json

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def hello():

    return Response("Hi from your Flask app running in your Docker container!")

@app.route("/about")
def about():
    conn = Connection(arangoURL='http://192.168.2.5:8529', username='root', password='password')
    db = conn["Test"]
    # # studentsCollection = db.createCollection(name="Blog")
    aql = "FOR u IN Blog RETURN u"
    queryResult = db.AQLQuery(aql, rawResults=True)
    
    # return jsonify(queryResult[2])
    # return json.dumps(str(queryResult))
    return json.JSONEncoder().encode(queryResult)

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)

