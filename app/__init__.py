import gridfs, pika
from flask import Flask
from config import Config
from flask_pymongo import PyMongo


mongo = PyMongo()
channel = ""
fs = ""
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    mongo.init_app(app)

    fs = gridfs.GridFS(mongo.db)

    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = connection.channel()

    # #Blue prints
    from app.auth import authpb as auth_bp
    app.register_blueprint(auth_bp)

    from app.auth_svc import authsvcpb as authsvc_bp
    app.register_blueprint(authsvc_bp,  url_prefix="/login")

    from app.updownload import updown as uploads_bp
    app.register_blueprint(uploads_bp)
    

    return app

def get_channel():
    return channel

def get_fs():
    return fs
