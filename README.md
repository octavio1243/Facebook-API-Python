# Facebook-API-Python


# Server's routes

| Description | Method HTTP | Endpoint | Request Body | Response Body | 
|-|-|-|-|-|
| Log in | POST | /login | {"email":"foo@foo.com","password":"foo1234"} | {"access_token":"EAAAA...","uid":"XXX..."} |
| Security login code | POST | /verify | {"email":"foo@foo.com","uid":"XXX...","login_first_factor":"YYY...","pin":"ZZZ..."} | {"access_token":"EAAAA...","uid":"XXX..."} | 
| Verify session | POST | /check | {"access_token":"EAAAA...","uid":"XXX..."} | {"value":true/false} |
| Make post (incomplete)| POST | /make_post | {"access_token":"EAAAA...","uid":"XXX...", "group_id":"YYY...", "description":"...","images_path":["...","..."]} | {"post_url":"https://..."} |
| Get user information | POST | {"access_token":"EAAAA...","uid":"XXX..."} | {"full_name":"...","image_name":"..."} |
| Get all groups | POST | {"access_token":"EAAAA...","uid":"XXX..."} | { "groups":[{"name": "...","id": "...","url": "..."}, ... ] }|
