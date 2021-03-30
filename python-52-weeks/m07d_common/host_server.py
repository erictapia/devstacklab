from flask import  Flask, request


app = Flask(__name__)


# NOT SAFE FOR MULTI-THREADING, using for testing
global_hosts = dict()


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
            return "must prvoide hostname on DELETE", 400

        del global_hosts[hostname]

        return {}, 204


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
