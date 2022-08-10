import datetime
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect
db_connect = MongoClient('mongodb://root:junlang0217!@localhost:27117')
db = db_connect.local

app = Flask(__name__)
# app.config['MONGO_URI'] = "mongodb://root:junlang0217!@localhost:27117"
# mongo = PyMongo(app)
# print(mongo)
# db = mongo.db['local']
# print(db)
print(db)

@app.route('/write', methods=["POST"])
def write():
    name = request.form.get('name')
    content = request.form.get('content')

    db.db['wedding'].insert_one({
        "name": "content",
        "content" : content
    })
    return redirect('/')

@app.route('/')
def index():
    now = datetime.datetime.now()
    wedding = datetime.datetime(2022, 9 ,4, 0 , 0 , 0)
    diff = (wedding - now).days

    return render_template('index.html', diff=diff)

if __name__ == '__main__':
    app.run()