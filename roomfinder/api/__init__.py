from flask import Blueprint


api = Blueprint('api', __name__)
#from roomfinder.api import hello
from roomfinder.api import (
    users,
    properties
)
