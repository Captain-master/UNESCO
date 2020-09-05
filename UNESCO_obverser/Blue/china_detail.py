from flask import request, Blueprint, jsonify, Response
from opmysql.opm import operationmysql

CN = Blueprint('china', __name__)

#申遗成功名单
@CN.route('/list', methods=["GET"])
def List():
    operation = operationmysql()
    sql = 'select kind, name, time, province from successUNESCO'
    result = operation.search(sql=sql)
    List = []
    for j in result:
        i = list(j)
        if i[0] == 1:
            i[0] = '文化遗产'
        elif i[0] == 2:
            i[0] = '文化景观遗产'
        elif i[0] == 3:
            i[0] = '自然遗产'
        elif i[0] == 4:
            i[0] = '文化与自然双重遗产'
        List.append(i)
    data = {
        "code": 1,
        "data": List
    }
    return jsonify(data)

#预备名录
@CN.route('/pre_list', methods=["GET"])
def pre_list():
    operation = operationmysql()
    sql = 'select number, kind, name, aera from UNESCOpreminary'
    result = operation.search(sql=sql)
    List = []
    for i in result:
        if i['kind'] == 1:
            i['kind'] = '中国世界遗产预备名录确定申请世界遗产项目'
        elif i['kind'] == 2:
            i['kind'] = '中国文化遗产预备名录'
        elif i['kind'] == 3:
            i['kind'] = '中国文化景观遗产预备名录'
        elif i['kind'] == 4:
            i['kind'] = '中国自然遗产预备名录'
        elif i['kind'] == 5:
            i['kind'] = '中国文化与自然双重遗产预备名录'
        List.append(i)
    data = {
        "code": 2,
        "data": List
    }
    return jsonify(data)

@CN.route('/search', methods=["POST"])
def search():
    json_data = request.get_json()
    operation = operationmysql()
    sql = 'select name,detail,img,aera from UNESCOpreminary where name = %s'
    values = (json_data['name'],)
    result = operation.search(sql=sql, values=values)
    data = {
        "code": 3,
        "data": result
    }
    return jsonify(data)