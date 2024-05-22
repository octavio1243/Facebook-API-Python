# Facebook-API-Python

Unofficial Facebook API library based in Facebook for Android V207.

# How to run

```
python -m FacebookAPI.Server
```

# Server's routes

| Description | Method HTTP | Endpoint | Request Body | Response Body | 
|-|-|-|-|-|
| Log in | POST | /login | {"email": "...", "password": "..."} | {"access_token": "EAAAA...", "uid": "XXX..."} |
| Security login code | POST | /verify | {"email": "...","uid": "XXX...", "login_first_factor": "YYY...", "pin": "ZZZ..."} | {"access_token": "EAAAA...", "uid": "XXX..."} | 
| Verify session | POST | /check | {"access_token": "EAAAA...", "uid": "XXX..."} | {"value": True|False} |
| Make post (incomplete)| POST | /make_post | {"access_token": "EAAAA...", "uid": "XXX...", "group_id": "YYY...", "description": "...", "images_path": ["...","..."]} | {"post_url": "https://..."} |
| Get user information | POST | /get_user_information | {"access_token": "EAAAA...", "uid": "XXX..."} | {"full_name": "...", "image_name": "..."} |
| Get all groups | POST | /get_groups | {"access_token": "EAAAA...", "uid": "XXX..."} | { "groups":[{"name": "...", "id": "...","url": "..."}, ... ] }|
