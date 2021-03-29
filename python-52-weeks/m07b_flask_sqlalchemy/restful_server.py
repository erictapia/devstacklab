from flask import Flask, request

from extensions import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.app_context().push()

import db_classes
db.create_all()

from db_apis import get_all_hosts, set_host
from db_apis import get_all_devices, set_device
from db_apis import get_all_services, set_service


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


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
