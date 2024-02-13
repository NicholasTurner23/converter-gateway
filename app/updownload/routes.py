from app.updownload import updown
from flask import request, json
from app.auth import validate
from app import get_channel, get_fs
from .util import uploadfile

@updown.route("/upload", methods=["POST"])
def upload():
    access, err = validate.token(request)

    access = json.loads(access)

    if access["admin"]:
        if len(request.files) != 1:
            return "Exactly 1 file required", 400
        
        for _, f in request.files.items():
            err = uploadfile(f, get_fs(), get_channel(), access)

            if err:
                return err
            
        return "success!", 200
    else:
        return "not authorized", 401

@updown.route("/download", methods=["POST"])
def download():
    pass

