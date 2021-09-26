#!/usr/bin/env python
# encoding: utf-8
import json
from flask.json import JSONEncoder
import requests
from flask import Flask, Request, jsonify
from flask import Flask, Response, jsonify

app = Flask(__name__)

@app.route('/<org>')
def get_gh_followers(org):
    api_end_point = "https://api.github.com/orgs/"+str(org)+"/members"
    org_members = requests.get(api_end_point)
    json_data = json.loads(org_members.text)
    return jsonify(json_data)

def sort_followers(json_data):
		# highest follower
    return jsonify(json_data)



if __name__ == "__main__":
    app.run(host="0.0.0.0")