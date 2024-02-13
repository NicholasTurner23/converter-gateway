from flask import Blueprint

authpb =Blueprint("auth", __name__)

from app.auth import validate