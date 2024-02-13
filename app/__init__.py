import os, gridfs, pika, json
from flask import Flask, request
from config import Config
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util

mongo = PyMongo()
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    mongo.init_app(app)

    fs = gridfs.GridFS(mongo.db)

    connection = pika.BlockingConnection(pika,ConnectionParameters("rabbitmq"))
    channel = connection.channel()

    # #Blue prints
    # from app.main import bp as main_bp
    # app.register_blueprint(main_bp)

    # return app

# def get_db():
#     return db.connection.cursor()

# if __name__ == "__main__":
#     create_app().run(host="0.0.0.0", port=5000)