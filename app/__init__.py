import gridfs, pika
from flask import Flask
from config import Config
from flask_pymongo import PyMongo


mongo = PyMongo()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    mongo.init_app(app, uri="mongodb://host.docker.internal:27017/videos")

    # #Blue prints
    from app.auth import authpb as auth_bp
    app.register_blueprint(auth_bp)

    from app.auth_svc import authsvcpb as authsvc_bp
    app.register_blueprint(authsvc_bp,  url_prefix="/login")

    from app.updownload import updown as uploads_bp
    app.register_blueprint(uploads_bp)
    

    return app

