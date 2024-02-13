from flask import Blueprint

authsvcpb =Blueprint("auth_svc", __name__)

from app.auth_svc import routes