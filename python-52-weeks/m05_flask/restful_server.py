from flask import  Flask, request


app = Flask(__name__)


# NOT SAFE FOR MULTI-THREADING, using for testing
global_hosts = dict()
global_devices = dict()
global_services = dict()


@app.route("/hosts", methods=["GET", "POST", "PUT", "DELETE"])
def hosts():
    global global_hosts

    if request.method == "GET":
        return global_hosts

    elif request.method == "POST":
        global_hosts = request.get_json()
        return {}, 204

    elif request.method == "PUT":
        hostname = request.args.get("hostname")

        if not hostname:
            return "must provide hostname on PUT", 400

        host = request.get_json()
        global_hosts[hostname] = host

        return {}, 204

    elif request.method == "DELETE":
        hostname = request.args.get("hostname")

        if not hostname:
            return "must provide hostname on DELETE", 400

        del global_hosts[hostname]

        return {}, 204


@app.route("/devices", methods=["GET", "POST", "PUT", "DELETE"])
def devices():
    global global_devices

    if request.method == "GET":
        return global_devices

    elif request.method == "POST":
        global_devices = request.get_json()
        return {}, 204

    elif request.method == "PUT":
        name = request.args.get("name")

        if not name:
            return "must provide name on PUT", 400

        device = request.get_json()
        global_devices[name] = device

        return {}, 204

    elif request.method == "DELETE":
        name = request.args.get("name")

        if not name:
            return "must provide name on DELETE", 400

        del global_devices[name]

        return {}, 204


@app.route("/services", methods=["GET", "POST", "PUT", "DELETE"])
def services():
    global global_services

    if request.method == "GET":
        return global_services

    elif request.method == "POST":
        global_services = request.get_json()
        return {}, 204

    elif request.method == "PUT":
        name = request.args.get("name")

        if not name:
            return "must provide name on PUT", 400

        service = request.get_json()
        global_services[name] = service

        return {}, 204

    elif request.method == "DELETE":
        name = request.args.get("name")

        if not name:
            return "must provide name on DELETE", 400

        del global_services[name]

        return {}, 204


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
