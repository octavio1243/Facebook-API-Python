from FacebookAPI.models.Device import Device
from FacebookAPI.models.Group import Group
from FacebookAPI.models.Post import Post
from FacebookAPI.models.User import User
from FacebookAPI.models.Image import Image
from flask import Flask, jsonify, request
import json

app=Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    json_request=request.json
    email=json_request["email"]
    password=json_request["password"]
    
    device = Device()
    user = User(device = device, email = email, password = password)
    
    return jsonify(user.login())

@app.route('/verify',methods=['POST'])
def verify_2FA():
    json_request=request.json
    email=json_request["email"]
    uid=json_request["uid"]
    login_first_factor=json_request["login_first_factor"]
    pin=json_request["pin"]
    
    device = Device()
    user = User(device = device, email = email, password = "unknow" )
    
    return jsonify(user.verify_2FA(uid = uid, login_first_factor = login_first_factor, pin = pin))

@app.route('/get_user_information',methods=['POST'])
def get_user_information():
    json_request=request.json
    access_token=json_request["access_token"]
    uid=json_request["uid"]
    session_cookies=json_request["session_cookies"]
    
    device = Device()
    user = User(device = device, access_token = access_token, uid = uid, session_cookies = session_cookies)

    return jsonify(user.get_user_information())

@app.route('/get_groups',methods=['POST'])
def get_groups():
    json_request=request.json
    access_token=json_request["access_token"]
    uid=json_request["uid"]
    session_cookies=json_request["session_cookies"]

    device = Device()
    user = User(device = device, access_token = access_token, uid = uid, session_cookies = session_cookies)

    return jsonify(user.get_groups())

@app.route('/make_post',methods=['POST'])
def make_post():
    json_data = request.form.get('json')
    if json_data:
        json_data = json.loads(json_data)
    binary_images = request.files.getlist('images')
    
    access_token=json_data["access_token"]
    uid=json_data["uid"]
    session_cookies=json_data["session_cookies"]
    description=json_data["description"]
    group_id=json_data["group_id"]
    
    device = Device()
    user = User(device = device, access_token = access_token, uid = uid, session_cookies = session_cookies)
    group = Group(id = group_id)
    images = [Image(binary = binary_image) for binary_image in binary_images]
    post = Post(user = user, description = description, group = group, images=images)
    
    return jsonify(post.make())

if __name__ == '__main__':
    app.run(debug=True,port=4000)
