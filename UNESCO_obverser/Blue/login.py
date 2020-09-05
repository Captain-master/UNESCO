from flask import Blueprint, request, jsonify
from opmysql.opm import operationmysql

sign_in = Blueprint('sign', __name__)

@sign_in.route('/sign', methods=['POST'])
def landing():
    json_data = request.get_json()
    opration = operationmysql()
    sql = 'select pwd from user where username = %s'
    values = (json_data["username"],)
    result = opration.search(sql=sql, values=values)
    data = {
        "code": 0,
     }
    if result != None:
        if result[0]["pwd"] == json_data['pwd']:
            data["code"] = 1
    return jsonify(data)