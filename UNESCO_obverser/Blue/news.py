from flask import request, Blueprint, jsonify, Response
from opmysql.opm import operationmysql

news = Blueprint('news', __name__)

#新闻详情
@news.route('/list', methods=["GET"])
def list():
    sql = 'select name,time, img_src,sdetail from UNESCOnews where year = 2020;'
    opration = operationmysql()
    result = opration.search(sql=sql)
    data = {
        "code": 1,
        "data": result
    }
    return jsonify(data)

#年份搜索
@news.route('/year',methods=['POST'])
def year():
    json_data = request.get_json()
    sql = 'select name,time, img_src,sdetail from UNESCOnews where year = %s'
    opration = operationmysql()
    values = (json_data['year'],)
    result = opration.search(sql=sql, values=values)
    data = {
        "code": 2,
        "data": result
    }
    return jsonify(data)

#名字搜索
@news.route('/detail',methods=['POST'])
def detail():
    json_data = request.form.to_dict()
    sql = 'select name,time, Detail,dsrc,year from UNESCOnews where name = %s'
    operation = operationmysql()
    values = (json_data["name"],)
    result = operation.search(sql=sql, values=values)
    data = {
        "code": 3,
        "data": result
    }
    return jsonify(data)
