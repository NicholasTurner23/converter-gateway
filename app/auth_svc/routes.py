from app.auth_svc import authpb, access
from flask import request

@authpb.route("/login", methods=["POST"])
def login():
    token, err = access.login(request)

    if not err:
        return token
    else:
        return err