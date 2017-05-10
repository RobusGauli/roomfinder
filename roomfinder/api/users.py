from roomfinder.api import api
from flask import abort
from flask import request

@api.route('/users', methods=['POST'])
def register_login_user():
    if not request.json:
        abort(400)
    print(request.json, request.args)
    print(type(request.json), type(request.args))
    return 'yeah'