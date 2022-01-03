#!/usr/bin/env python

from wsgiref import simple_server
from flask import Flask, request, render_template
from flask import Response
import os


app = Flask(__name__)


@app.route("/", methods=['GET'])
# @cross_origin()
def home():
    return("jay prakash")
    # return render_template('index.html')




port = int(os.getenv("PORT", 5000))
if __name__ == "__main__":
    # app.run()
    host = '0.0.0.0'
    # port = 5000
    httpd = simple_server.make_server(host, port, app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()
    # it does not give something interminal but it runnung
 