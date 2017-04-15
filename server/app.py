# coding: utf-8


import flask
from flask import Flask, render_template, request
app = Flask(__name__)

import os
import time

@app.route('/detect', methods=["POST"])
def process_image():
    if request.method == 'POST':
        request.files['image'].save("image.png")

    return "time is %s" % time.time()

if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run(host='0.0.0.0', threaded=True, use_reloader=False, debug=True, port=9999)