from app.auth_svc import authsvcpb, access
from flask import request

@authsvcpb.route("", methods=["POST"])
def login():
    token, err = access.login(request)

    if not err:
        return token
    else:
        return err