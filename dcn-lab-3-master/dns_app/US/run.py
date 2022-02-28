import time
from flask import Flask
from flask import abort
from flask import request
import json
import requests

app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    url = "http://" + "localhost" + ":" + as_port + "/dnsquery"
    data_send = {
        "TYPE": "A",
        "NAME": hostname,
    }
    try:
        result = requests.post(url, data=data_send, timeout=5)
        time.sleep(60)
        result.raise_for_status()
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    ipFib = result['VALUE']
    domainName = result['NAME']
    urlfib = "http://" + ipFib + "/" + domainName + "?" + "number=" + number
    ans = requests.post(urlfib)
    return ans


app.run(host='0.0.0.0',
        port=8080,
        debug=True)
