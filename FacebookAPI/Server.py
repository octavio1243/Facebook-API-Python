from FacebookAPI.models.Device import Device
from FacebookAPI.models.Group import Group
from FacebookAPI.models.Post import Post
from FacebookAPI.models.User import User
from flask import Flask, jsonify, request

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
    
    device = Device()
    user = User(device = device, email = email, password = password)
    
    return jsonify(user.login())

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
    
    device = Device()
    user = User(device = device, email = email, password = "unknow" )
    
    return jsonify(user.verify_2FA(uid = uid, login_first_factor = login_first_factor, pin = pin))

"""
Request body: {"access_token":"EAAAA...","uid":"XXX..."}
Response body: {"full_name":"...","image_name":"..."}
"""
@app.route('/get_user_information',methods=['POST'])
def get_user_information():
    json_request=request.json
    access_token=json_request["access_token"]
    uid=json_request["uid"]
    
    device = Device()
    user = User(device = device, access_token = access_token, uid = uid)

    return jsonify(user.get_user_information())

"""
Request body: {"access_token":"EAAAA...","uid":"XXX..."}
Response body: { "groups":[{"name": "...","id": "...","url": "..."}, ... ] }
"""
@app.route('/get_groups',methods=['POST'])
def get_groups():
    json_request=request.json
    access_token=json_request["access_token"]
    uid=json_request["uid"]
    
    device = Device()
    user = User(device = device, access_token = access_token, uid = uid )

    return jsonify(user.get_groups())


"""
Request body: {"access_token":"EAAAA...","uid":"XXX...", "group_id":"YYY...", "description":"..."}
Response body: {"post_url":"https://..."}
"""
@app.route('/make_post',methods=['POST'])
def make_post():
    json_request=request.json
    access_token=json_request["access_token"]
    uid=json_request["uid"]
    description=json_request["description"]
    group_id=json_request["group_id"]
    
    device = Device()
    user = User(device = device, access_token = access_token, uid = uid)
    group = Group(id = group_id)
    post = Post(user = user, description = description, group = group)

    return jsonify(post.make())


if __name__ == '__main__':
    app.run(debug=True,port=4000)
