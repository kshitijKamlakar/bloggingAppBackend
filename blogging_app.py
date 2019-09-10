import datetime
import json

from flask import Flask, request, render_template
from flask_cors import CORS

from crud import *
from models import db

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://postgres:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/blog/all')
def getAllData():
    return json.dumps(getAllBlogs(), default=lambda o: blogJsonConvertor(o))


@app.route('/api/blog/<int:id>')
def getById(id):
    return json.dumps(getBlogById(id), default=lambda o: blogJsonConvertor(o))


@app.route('/api/blog/create', methods=['POST'])
def addData():
    data = request.get_json()
    blog = Blog(data['blogTitle'], data['blogContent'])
    return json.dumps(addBlog(blog))


@app.route('/api/blog/delete/<int:id>', methods=['DELETE'])
def deleteData(id):
    return json.dumps(deleteBlog(id))


@app.route('/api/blog/update', methods=['PUT'])
def updateData():
    data = request.get_json()
    return json.dumps(updateBlog(data))


def blogJsonConvertor(o):
    if isinstance(o, datetime.date):
        return o.__str__()
    elif isinstance(o, Blog):
        return o.__dict__


if __name__ == '__main__':
    app.run()
