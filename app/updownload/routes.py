from app.updownload import updown
from flask import request
import json, gridfs, pika
from app.auth import validate
from .util import uploadfile
from app import mongo

fs = gridfs.GridFS(mongo.db)
connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = connection.channel()

@updown.route("/upload", methods=["POST"])
def upload():
    access, err = validate.token(request)

    if err:
        return err

    access = json.loads(access)

    if access["admin"]:
        if len(request.files) != 1:
            return "Exactly 1 file required", 400
        
        for _, f in request.files.items():
            err = uploadfile(f, fs, channel, access)

            if err:
                return err
            
        return "success!", 200
    else:
        return "not authorized", 401

@updown.route("/download", methods=["POST"])
def download():
    pass

