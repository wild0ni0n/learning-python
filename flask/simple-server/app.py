# -*- coding: utf-8 -*-
from flask import Flask, render_template, make_response, jsonify
import argparse
app = Flask(__name__)


@app.route("/")
def index():
    resp = make_response(render_template('index.html'))    
    return resp

# json response server
@app.route("/json")
def json():
    import uuid
    return jsonify({"id": uuid.uuid4()})

def argparser_setup():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--addr", default="0.0.0.0", help="サーバのIPアドレスを指定します")
    parser.add_argument("-p", "--port", type=int, default=18080, help="サーバのポート番号を指定します")
    parser.add_argument("-d", "--debug", action="store_true", help="debugモードで実行します")
    return parser.parse_args()


if __name__ == "__main__":
    args = argparser_setup()

    host = args.addr
    port = args.port
    debug = args.debug if True else False
    
    print("[*] listening on {host} {port}...".format(host=host, port=port))
    print("[*] Open http://127.0.0.1:" + str(port))

    app.run(host=host, port=port, debug=debug)
