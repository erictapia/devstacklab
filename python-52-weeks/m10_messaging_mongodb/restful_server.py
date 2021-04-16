from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


from db_apis import get_all_devices, set_device
from db_apis import get_all_hosts, set_host
from db_apis import get_all_services, set_service
from db_apis import get_portscan, get_traceroute
from db_apis import record_portscan_data, record_traceroute_data
from worker_apis import start_portscan, start_traceroute


@app.route("/hosts", methods=["GET", "PUT"])
def hosts():
    if request.method == "GET":
        return get_all_hosts()

    elif request.method == "PUT":
        hostname = request.args.get("hostname")

        if not hostname:
            return "must provide hostname on PUT", 400

        host = request.get_json()
        set_host(host)

        return {}, 204


@app.route("/devices", methods=["GET", "PUT"])
def devices():

    if request.method == "GET":
        return get_all_devices()

    elif request.method == "PUT":
        name = request.args.get("name")

        if not name:
            return "must provide name on PUT", 400

        device = request.get_json()
        set_device(device)

        return {}, 204


@app.route("/services", methods=["GET", "PUT"])
def services():

    if request.method == "GET":
        return get_all_services()

    elif request.method == "PUT":
        name = request.args.get("name")

        if not name:
            return "must provide name on PUT", 400

        service = request.get_json()
        set_service(service)

        return {}, 204


@app.route("/scan", methods=["GET", "POST"])
def scan_endpoint():

    target = request.args.get("target")

    if not target:
        return "must provide target to get portscan", 400

    if request.method == "GET":
        token = request.args.get("token")

        if not token:
            return "must provide token to get portscan", 400

        return get_portscan(target, token)

    elif request.method == "POST":
        token = start_portscan(target)

        return {"token": token}


@app.route("/traceroute", methods=["GET", "POST"])
def traceroute_endpoint():

    target = request.args.get("target")
    if not target:
        return "must provide service target to get traceroute", 400

    target = fix_target(target)

    if request.method == "GET":
        token = request.args.get("token")

        if not token:
            return "must provide token to get traceroute", 400

        return get_traceroute(target, token)

    elif request.method == "POST":
        token = start_traceroute(target)

        return {"token": token}


@app.route("/worker/portscan", methods=["POST"])
def worker_portscan_endpoint():

    portscan_data = request.get_json()
    record_portscan_data(portscan_data)

    return {}, 204


@app.route("/worker/traceroute", methods=["POST"])
def worker_traceroute_endpoint():

    traceroute_data = request.get_json()
    record_traceroute_data(traceroute_data)

    return {}, 204


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
