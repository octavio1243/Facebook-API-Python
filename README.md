# Facebook-API-Python

Unofficial Facebook API library based in Facebook for Android V207.

If you like this project:  

**Bitcoin**: 342eSZjvzW2GWkJAraGCY5T72zB47sKoDN

**Ethereum**: 0xE0e14A8103b81e2984cF69a0c3646C43CE0DEc2c

# How to run

```
python -m FacebookAPI.Server
```

# Server's routes

| Description | Method HTTP | Endpoint | Body Type | Request Body | Response Body | 
|-|-|-|-|-|
| Log in | POST | /login | Json | {"email": "...", "password": "..."} | {"access_token": "EAAAA...", "uid": "XXX...", "session_cookies":[{"name": "...","value": "..."}, ...]} Or: {"code": 406, "login_first_factor": "...", "message": "Login approvals are on. Expect an SMS shortly with a code to use for log in (406)", "uid": "..."} |
| Security login code | POST | /verify | Json | {"email": "...","uid": "XXX...", "login_first_factor": "YYY...", "pin": "ZZZ..."} | {"access_token": "EAAAA...", "uid": "XXX...", "session_cookies":[{"name": "...","value": "..."}, ...]} | 
| Get user information | POST | /get_user_information | Json | {"access_token": "EAAAA...", "uid": "XXX...", "session_cookies":[{"name": "...","value": "..."}, ...]} | {"full_name": "...", "image_name": "..."} |
| Get all groups | POST | /get_groups | Json | {"access_token": "EAAAA...", "uid": "XXX...", "session_cookies":[{"name": "...","value": "..."}, ...]} | { "groups":[{"name": "...", "id": "...","url": "..."}, ... ] }|
| Make post | POST | /make_post | multipart/form-data | {"access_token": "EAAAA...", "uid": "XXX...", "session_cookies":[{"name": "...","value": "..."}, ...], "group_id": "YYY...", "description": "..."} | {"post_url": "https://..."} |
