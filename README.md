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

| Description            | Method HTTP | Endpoint             | Body Type          | Request Body                                                                                     | Response Body                                                                                                                                                                  | 
|------------------------|-------------|----------------------|--------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Log in                 | POST        | /login               | JSON               | `{"email": "...", "password": "..."}`                                                           | `{"access_token": "EAAAA...", "uid": "XXX...", "session_cookies":[{"name": "...","value": "..."}, ...]}` <br> Or: <br>  `{"code": 406, "login_first_factor": "...", "message": "Login approvals are on. Expect an SMS shortly with a code to use for log in (406)", "uid": "..."}`
| Security login code    | POST        | /verify              | JSON               | `{"email": "...","uid": "XXX...", "login_first_factor": "YYY...", "pin": "ZZZ..."}`             | `{"access_token": "EAAAA...", "uid": "XXX..."}`                                                                      |
| Get user information   | POST        | /get_user_information | JSON               | `{"access_token": "EAAAA..."}` | `{"birthday": "...", "email": "...", "full_name": "...", "gender": "...", "id": "...", "location": "...", "profile_pic": "...", "relationship_status": "..."}`                                                                                                                                    |
| Get all groups         | POST        | /get_groups          | JSON               | `{"access_token": "EAAAA..."}` | `{ "groups":[{"name": "...", "id": "...","url": "..."}, ... ] }`                                                                                                              |
| Make post              | POST        | /make_post           | multipart/form-data | `{"access_token": "EAAAA...", "group_id": "YYY...", "description": "...", "images_urls": ["https://...", ...]}` | `{"group_post_id": "..."}` 

