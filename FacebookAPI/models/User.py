
from FacebookAPI.enums.CredentialsType import CredentialsType
from FacebookAPI.enums.MetaInfFbMeta import MetaInfFbMeta
from FacebookAPI.enums.Source import Source
from FacebookAPI.enums.XFbFriendlyName import XFbFriendlyName
from FacebookAPI.models.Group import Group
from FacebookAPI.models.Image import Image
from FacebookAPI.config import AUTH_URL, GRAPH_URL
import requests
import json_repair
import json

def uid_required(func):
    def wrapper(self, *args, **kwargs):
        self.get_user_information(profile_pic_required = False)
        return func(self, *args, **kwargs)
    return wrapper

class User():
    
    def __init__(self, device = None, email = None, password = None, access_token = None, uid = None, session_cookies = []):
        if device is None:
            raise Exception("The user require an Device")
        if not(email is None and password is None) and not(access_token is None):
            raise Exception("The user require (email and password) or (access_token)") 
        self.device = device
        self.email=email
        self.password=password
        self.full_name=""
        self.birthday=""
        self.gender=""
        self.location=""
        self.relationship_status=""
        self.profile_pic=None
        self.access_token=access_token
        self.uid=uid
        self.session_cookies = session_cookies

    def sign_login_body(self, data, login):
        if login:
            data["source"] = data["source"]+self.device.app.const_key
        else:
            data["userid"] = data["userid"]+self.device.app.const_key
        data_to_sign = [f'{key}={value}' for key, value in data.items()]
        
        data_to_sign.sort() 
        str_data="".join(data_to_sign)
        #print(str_data)
        return self.device.app.get_signature(str_data)

    def login(self):
        url = f"{AUTH_URL}/method/auth.login"
        
        self.device.app.headers.set_header("X-Fb-Friendly-Name", XFbFriendlyName.AUTHENTICATE.value)
        #self.device.app.headers.set_header("Authorization", user_agent)
        headers = self.device.app.headers.get_all_headers()

        data = {"adid": self.device.app.adid,
        "format": self.device.app.format,
        "device_id": self.device.device_id,
        "email": self.email,
        "password": self.password,
        "cpl": self.device.app.cpl,
        "family_device_id": self.device.family_device_id,
        "credentials_type": CredentialsType.LOGIN.value,
        "generate_session_cookies": self.device.app.generate_session_cookies,
        "error_detail_type": self.device.app.error_detail_type,
        "source": Source.DEVICE_BASED_LOGIN.value,
        "machine_id": self.device.machine_id,
        "meta_inf_fbmeta": MetaInfFbMeta.EMPTY.value,
        "advertiser_id": self.device.app.advertiser_id,
        "currently_logged_in_userid": self.device.app.currently_logged_in_userid,
        "locale": self.device.app.locale,
        "client_country_code": self.device.app.client_country_code,
        "method": self.device.app.method,
        "fb_api_req_friendly_name": self.device.app.fb_api_req_friendly_name,
        "fb_api_caller_class": self.device.app.fb_api_caller_class,
        "api_key": self.device.app.api_key}
        
        data["sig"] = self.sign_login_body(data.copy(),True)
        r=requests.post(url, headers=headers, data=data,timeout=5)
        
        r_json=r.json()
        #print(r_json)
        try:
            self.access_token=str(r_json["access_token"])
            self.uid=str(r_json["uid"])
            self.session_cookies = r_json["session_cookies"]
            return {"access_token":self.access_token,"uid":self.uid,"session_cookies":self.session_cookies}
        except:
            message=r_json["error_msg"]
            code=r_json["error_code"]
            if code==406: #Error 2FA
                self.uid=str(json.loads(r_json["error_data"])["uid"])
                login_first_factor=json.loads(r_json["error_data"])["login_first_factor"]
                return {"message":message,"code":code,"uid":self.uid,"login_first_factor":login_first_factor}
            return {"message":message,"code":code}
            
            """
            "message":"Login approvals are on. Expect an SMS shortly with a code to use for log in",
            "code":406,
            """
               
            """
            "message":"Invalid username or password",
            "code":401
            """
       
    def verify_2FA(self, uid, login_first_factor, pin):
        if uid is None:
            raise Exception("The user's object require an id") 
        
        url = f"{AUTH_URL}/method/auth.login"
        self.device.app.headers.set_header("X-Fb-Friendly-Name", XFbFriendlyName.AUTHENTICATE.value)
        #self.device.app.headers.set_header("Authorization", user_agent)
        headers = self.device.app.headers.get_all_headers()
                
        data = {
            "adid": self.device.app.adid,
            "advertiser_id": self.device.app.advertiser_id,
            "api_key": self.device.app.api_key,
            "client_country_code": self.device.app.client_country_code,
            "cpl": self.device.app.cpl,
            "credentials_type": CredentialsType.TWO_FACTOR.value,
            "currently_logged_in_userid": self.device.app.currently_logged_in_userid,
            "device_id": self.device.device_id,
            "email": self.email,
            "error_detail_type": self.device.app.error_detail_type,
            "family_device_id": self.device.family_device_id,
            "fb_api_caller_class": self.device.app.fb_api_caller_class,
            "fb_api_req_friendly_name": self.device.app.fb_api_req_friendly_name,
            "first_factor": login_first_factor,
            "format": self.device.app.format,
            "generate_session_cookies": self.device.app.generate_session_cookies,
            "locale": self.device.app.locale,
            "machine_id": self.device.machine_id,
            "meta_inf_fbmeta": MetaInfFbMeta.NO_FILE.value,
            "method": self.device.app.method,
            "password": pin,
            "source": Source.LOGIN.value,
            "try_num": "1",
            "twofactor_code": pin,
            "userid": uid,
        }

        data["sig"] = self.sign_login_body(data.copy(),False)

        r=requests.post(url, headers=headers, data=data)
        r_json=r.json()
        #print(r_json)
        try:
            self.access_token=str(r_json["access_token"])
            self.uid = uid
            self.session_cookies = r_json["session_cookies"]
            return {"access_token":self.access_token,"uid":self.uid,"session_cookies":self.session_cookies}
        except: # incorrect pin
            message=r_json["error_msg"]
            code=r_json["error_code"]
            print(message,type,code)  
            return {"message":message,"code":code}
    
    def get_user_image(self):
        url = f"{GRAPH_URL}/graphql"
        
        self.device.app.headers.set_header("X-Fb-Friendly-Name", XFbFriendlyName.USER_TIMELINE_QUERY.value)
        self.device.app.headers.set_header("Authorization", f"OAuth {self.access_token}")
        headers = self.device.app.headers.get_all_headers()

        json_variables = {"profile_id":self.uid}
        
        data = {
        "client_doc_id": "36410619711761190567959011903",
        "method": "post",
        "locale": "es_LA",
        "pretty": "false",
        "format": "json",
        "variables": json.dumps(json_variables),
        "fb_api_req_friendly_name": "UserTimelineQuery",
        "fb_api_caller_class": "graphservice",
        "fb_api_analytics_tags": "[\"At_Connection\",\"GraphServices\"]",
        "client_trace_id": '',
        "server_timestamps": "true",
        "purpose": "refresh"}
        
        r=requests.post(url, headers=headers, data=data)
        r_json = json_repair.loads(r.text)
        
        user_image = None 
        
        try:
            image_url=r_json["data"]["user"]["profile_photo"]["image"]["uri"]
            user_image = Image(image_url)
        except:
            print("Error to get user image")
        
        return user_image
    
    def get_user_information(self, profile_pic_required = True):
        url = f"{GRAPH_URL}/v20.0/me?access_token={self.access_token}&fields=email,birthday,gender,location,relationship_status,id,name"
        
        r=requests.get(url)                
        r_json = r.json()
        print(r_json)

        try:
            self.email=r_json["email"]
            self.full_name=r_json["name"]
            self.birthday=r_json["birthday"]
            self.gender=r_json["gender"]
            self.location=r_json["location"]["name"]
            self.relationship_status=r_json["relationship_status"]
            self.uid=r_json["id"]
            self.profile_pic = self.get_user_image() if profile_pic_required else None
        except:
            raise Exception("Error to get user information")
            
        return {
            "full_name": self.full_name,
            "email":self.email,
            "birthday": self.birthday,
            "gender":self.gender,
            "location":self.location,
            "relationship_status":self.relationship_status,
            "id":self.uid,
            "profile_pic":self.profile_pic.url if self.profile_pic else None
        }

    @uid_required
    def get_groups(self):
        url = f"{GRAPH_URL}/graphql"
        
        self.device.app.headers.set_header("X-Fb-Friendly-Name", XFbFriendlyName.FETCH_GROUPS_TAB_GROUP_POGS_AT_CONNECTION.value)
        self.device.app.headers.set_header("Authorization", f"OAuth {self.access_token}")
        headers = self.device.app.headers.get_all_headers()
        
        json_variables={"group_item_small_cover_photo_size":105,
        "group_item_small_cover_photo_height":105,
        "entry_point":"TAB_STORIES",
        "group_list_type":"ALL_GROUPS", #ALL_GROUPS_WITHOUT_PINNED
        "badged_group_list_connection_first":1000
        }
        
        fb_api_analytics_tags=["GraphServices","At_Connection"]
        
        data = {
        "doc_id": "3431125043569008",
        "method": "post",
        "locale": "es_LA",
        "pretty": "false", 
        "format": "json", 
        "purpose": "refresh", 
        "variables": json.dumps(json_variables), 
        "fb_api_req_friendly_name": "FetchFullGroupList", 
        "fb_api_caller_class": "graphservice", 
        "fb_api_analytics_tags": json.dumps(fb_api_analytics_tags), 
        "server_timestamps": "true"}
        
        r=requests.post(url, headers = headers, data = data, timeout = 5)

        groups=[]

        try:
            r_json=r.json()
            number_of_groups= r_json["data"]["viewer"]["groups_tab"]["badged_group_list"]["count"]
            for group in r_json["data"]["viewer"]["groups_tab"]["badged_group_list"]["edges"]:
                name=group["node"]["name"]
                id=group["node"]["id"]
                url=group["node"]["groupItemProfilePic"]["uri"]
                group = Group(id = id, name = name, url = url)
                groups.append(group.get_json())
        except:
            raise Exception("Error to get user's groups")
        
        return {"number_of_groups": number_of_groups, "groups": groups}    

    def get_cookies(self):
        cookies = {}
        for s in self.session_cookies:
            cookies[s["name"]]=s["value"]
        return cookies