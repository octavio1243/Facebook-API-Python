from flask import Flask, jsonify, request
from Facebook_API import Post,FacebookAPI
import requests

app=Flask(__name__)

"""
Request body: {"email":"user@email.com","password":"pass1243!"}
Response body: {"access_token":"EAAAA...","uid":"XXX..."}
"""
@app.route('/login',methods=['POST'])
def login():
    json_request=request.json
    email=json_request["email"]
    password=json_request["password"]
    cuenta=FacebookAPI(email=email,password=password)
    return jsonify(cuenta.login())

"""
Request body: {"email":"user@email.com","uid":"YYY...","login_first_factor":"ZZZ...","pin":"XXX..."}
Response body: {"access_token":"EAAAA...","uid":"XXX..."}
"""
@app.route('/verify',methods=['POST'])
def verify_2FA():
    json_request=request.json
    email=json_request["email"]
    uid=json_request["uid"]
    login_first_factor=json_request["login_first_factor"]
    pin=json_request["pin"]
    cuenta=FacebookAPI(email=email,uid=uid,login_first_factor=login_first_factor,password=pin)
    return jsonify(cuenta.verify_2FA())
    
"""
Request body: {"access_token":"EAAAA...","uid":"XXX..."}
Response body: {"value":true/false}
"""
@app.route('/check',methods=['POST'])
def check():
    json_request=request.json
    access_token=json_request["access_token"]
    uid=json_request["uid"]
    cuenta=FacebookAPI(access_token=access_token,uid=uid)
    return jsonify({"value":cuenta.is_alive()})

"""
Request body: {"access_token":"EAAAA...","uid":"XXX...", "group_id":"YYY...", "description":"...","images_path":["...","..."]}
Response body: {"post_url":"https://..."}
"""
@app.route('/make_post',methods=['POST'])
def make_post():
    return jsonify({"post_url":"https://..."})

"""
Request body: {"access_token":"EAAAA...","uid":"XXX..."}
Response body: {"full_name":"...","image_name":"..."}
"""
@app.route('/get_user_information',methods=['POST'])
def get_user_information():
    json_request=request.json
    access_token=json_request["access_token"]
    uid=json_request["uid"]
    cuenta=FacebookAPI(access_token=access_token,uid=uid)
    return jsonify(cuenta.get_user_information())

"""
Request body: {"access_token":"EAAAA...","uid":"XXX..."}
Response body: { "groups":[{"name": "...","id": "...","url": "..."}, ... ] }
"""
@app.route('/get_groups',methods=['POST'])
def get_groups():
    json_request=request.json
    access_token=json_request["access_token"]
    uid=json_request["uid"]
    cuenta=FacebookAPI(access_token=access_token,uid=uid)
    return jsonify(cuenta.get_groups())

if __name__ == '__main__':
    app.run(debug=True,port=4000)
