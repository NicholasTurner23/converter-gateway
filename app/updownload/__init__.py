from flask import Blueprint

updown =Blueprint("uploads", __name__)

from app.updownload import routes
from app.updownload import util