from flask import Flask
from flask import request
from flask import jsonify
from flask import Blueprint
import requests
from . import api

@api.route ('/todos',methods=['GET','POST'])
def todos():
    if request.method == 'POST':
        res = requests.post('https://hooks.slack.com/services/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',json={
            'text': 'Hello World'
        }, header={'Content-Type': 'application/json'})
    elif request.method == 'GET':
        pass

    data = request.get_json()
    return jsonify(data)

@api.route('/test',methods=['POST'])
def test():
    res = request.form['text']
    print(res)
    return jsonify(res)