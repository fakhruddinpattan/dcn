import json
from flask import abort
from flask import Flask, request

app = Flask(__name__)

@app.route('/registerdns', methods=['GET', 'POST'])
def registerdns():
    data_recieved = request.json
    #dump data into a file
    with open('file.txt', 'w') as jfile:
        json.dump(data_recieved, jfile)
    return '201'

@app.route('/dnsquery', methods=['GET', 'POST'])
def dnsquery():
    data_recieved = request.json
    if data_recieved['NAME'] == 'fibonacci.com' and data_recieved['TYPE'] == 'A':
        with open('file.txt', 'r') as jfile:
            data = json.load(jfile)
            result = {
                "TYPE": data["TYPE"],
                "NAME": data["NAME"],
                "VALUE": data["VALUE"],
                "TTL": data["TTL"],
            }
        return result
    else:
        return abort(400)

app.run(host='0.0.0.0',
        port=53533,
        debug=True)
