import time
from flask import Flask
from flask import abort
from flask import request
import json
import requests

app = Flask(__name__)

@app.route('/register', methods=['PUT'])
def register():
    data_req = request.json
    ip = data_req["ip"]
    hostname = data_req["hostname"]
    as_ip = data_req["as_ip"]
    as_port = data_req["as_port"]
    data_changed = {
        "NAME": hostname,
        "TYPE": "A",
        "VALUE": ip,
        "TTL": 10,
    }
    data_in_json = json.dumps(data_changed)
    result = requests.post("http://" + "0.0.0.0" + ":" + str(as_port) + "/registerdns", data_in_json)
    return result

@app.route('/fibonacci')
def Fib():
    num = request.args.get('number')
    return calculate(num)

def calculate(number):
    number_to_count = 0
    dm = []
    if number == 0:
        return 0
    for number in dm:
        number_to_count = dm[number]

    if number <= 2:
        number_to_count = 1
    else:
        number_to_count = calculate(number - 1) + calculate(number - 2)
    return number_to_count

app.run(host='0.0.0.0',
        port=9090,
        debug=True)
