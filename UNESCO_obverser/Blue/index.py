from flask import request, Blueprint, jsonify, Response
from opmysql.opm import operationmysql

index = Blueprint('index', __name__)



#世界遗产列表
@index.route('/UNESCOlist', methods=["POST"])
def get_UNESCO_list():
    json_data = request.form.to_dict()
    print(json_data["countryname"])
    opration = operationmysql()
    if json_data["countryname"] is undefined:
	sql = 'select UNESCOnumber,UNESCOname, country_name,utime from UNESCOlist, countrylist where UNESCOlist.country_number = countrylist.country_number and countrylist.country_name= %s;'
        values = (json_data["countryname"],)
        result = operation.search(sql=sql, values=values)
    else : 
    	sql = 'select UNESCOnumber,UNESCOname, country_name,utime from UNESCOlist, countrylist where UNESCOlist.country_number = countrylist.country_number;'
        result = opration.search(sql=sql)
    data = {
        "code": 1,
        "data": result
    }
    return jsonify(data)

#通过名字搜索
@index.route('/UNESCOsearch', methods=["POST"])
def search():
    json_data = request.get_json()
    opration = operationmysql()
    sql = 'select UNESCOname, detail, img_src from UNESCOlist where UNESCOname = %s'
    values = (json_data["UNESCOname"],)
    result = opration.search(sql=sql, values=values)
    data = {
        "code": 2,
        "data": result
    }
    return jsonify(data)

#通过国家搜索
@index.route('/countryUNESCO', methods=["POST"])
def contrylist():
    json_data = request.form.to_dict()
    result = []
    if json_data != None :
        operation = operationmysql()
        sql = 'select UNESCOnumber,UNESCOname, country_name,utime from UNESCOlist, countrylist where UNESCOlist.country_number = countrylist.country_number and countrylist.country_name= %s;'
        values = (json_data["countryname"],)
        result = operation.search(sql=sql, values=values)
        print(result)
    data = {
        "code": 3,
        "data": result
    }
    return jsonify(data)

@index.route('/UNESCOkind', methods=["POST"])
def unescokind():
    json_data = request.get_json()
    operation = operationmysql()
    sql = 'select UNESCOname from UNESCOkind where UNESOkind = %s'
    values = (json_data["kind"],)
    data = operation.search(sql=sql, values=values)
    data = {
        "code": 4,
        "data": data
    }
    return jsonify(data)

@index.route('/detail', methods=["POST"])
def datail():
    json_data = request.form.to_dict()
    result = []
    if json_data != {}:
        operation = operationmysql()
        sql = 'select UNESCOname, detail, img_src, utime,country_name from UNESCOlist,countrylist where UNESCOname = %s and UNESCOlist.country_number = countrylist.country_number'
        values = (json_data["name"],)
        result = operation.search(sql=sql, values=values)
    data = {
        "data": result
    }
    return jsonify(data)



