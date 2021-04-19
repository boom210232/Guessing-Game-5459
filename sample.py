from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import os, json, redis

# App
application = Flask(__name__)

# connect to MongoDB
mongoClient = MongoClient(
    'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ[
        'MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_AUTHDB'])
db = mongoClient[os.environ['MONGODB_DATABASE']]

# connect to Redis
redisClient = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=os.environ.get("REDIS_PORT", 6379),
                          db=os.environ.get("REDIS_DB", 0))

my_game = db.Guessing_game


@application.route('/')
def index():
    my_game.delete_many({})
    return render_template('index.html')


@application.route('/game')
def game():
    my_game.insert_one({
        "answer": [],
        "winner": False,
        "count": 0,
        "wrong": 0,

    })
    on_the_game = my_game.find_one({"winner": False})
    return render_template('game.html', game=on_the_game)


@application.route('/a-button/')
def a_button():
    pass


@application.route('/b-button/')
def b_button():
    pass


@application.route('/c-button/')
def c_button():
    pass


@application.route('/d-button/')
def c_button():
    pass


if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("FLASK_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("FLASK_PORT", 5000)
    application.run(host='0.0.0.0', port=ENVIRONMENT_PORT, debug=ENVIRONMENT_DEBUG)
