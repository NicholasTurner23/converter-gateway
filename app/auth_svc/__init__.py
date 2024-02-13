from flask import Blueprint

authpb =Blueprint("auth", __name__)

from app.auth_svc import access
from app.auth_svc import routes