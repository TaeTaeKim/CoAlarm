#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 10:09:29 2021

@author: bizzy
"""

from flask import Flask, jsonify

import entry_requirement

app = Flask(__name__)

corona = entry_requirement.AsyncTask()
corona.Entry()
corona.CD()



@app.route("/number", methods = ["GET"])
def Number():
    data = CD()
    return jsonify(data)

@app.route("/entry", methods = ["GET"])
def EntryRequirement():
    data = Entry()
    return jsonify(data)

if __name__ == "__main__":
    app.run()