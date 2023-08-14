import json
import subprocess
import os
import requests
import time
import random
import re
import io
import hashlib
import uuid

class Post():
    def __init__(self,description,images_binary,id_group):
        self.images_binary=images_binary
        self.description=description
        self.id_group=id_group

    def get_images_binary(self):
        return self.images_binary
        
    def get_description(self):
        return self.description
        
    def get_id_group(self):
        return self.id_group

class FacebookAPI():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    adid="dd709e93-08e4-4a4c-b9bd-c41d6d9a7092" #Constant
    advertiser_id="dd709e93-08e4-4a4c-b9bd-c41d6d9a7092" #Constant
    api_key="882a8490361da98702bf97a021ddc14d" #Constant
    client_country_code="AR" #Constant
    cpl="true" #Constant
    credentials_type="device_based_login_password" # It can be "password" also
    currently_logged_in_userid="0" #Constant
    error_detail_type="button_with_disabled" #Constant
    fb_api_caller_class="com.facebook.account.login.protocol.Fb4aAuthHandler" #Constant
    fb_api_req_friendly_name="authenticate" #Constant
    format="json" #Constant
    generate_session_cookies="1" #Constant
    locale="es_LA" #Constant
    meta_inf_fbmeta="" #Constant
    method="auth.login" #Constant
    source="device_based_login" # It can be "login" also
    const_key="62f8ce9f74b12f84c123cc23437a4a32" #const-string from smali code
    device_id="" # Variable
    machine_id="0k0hZkcZegv11yc2w1Iao-uA" # Variable
    family_device_id="686ffda5-e9af-464a-944e-3bbd4e1850ea" # I think it is constant (I don´t 100% sure)
    email=""
    password=""
    access_token=""
    uid=""
    full_name=""
    login_first_factor=""
    
    def __init__(self, email=None, password=None,access_token=None, uid=None, login_first_factor=None):
        self.email=email
        self.password=password
        self.access_token=access_token
        self.uid=uid
        self.login_first_factor=login_first_factor
        self.device_id = str(uuid.uuid4())
    
    def get_token(self):
        l = str(int(time.time() * 1000))
        secure_random = random.SystemRandom()
        token = str(uuid.UUID(int=(secure_random.getrandbits(64) ^ int(time.time() * 1000)),version=4))
        return token
    
    def get_signature(self, str_data):
        B = [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 97, 98, 99, 100, 101, 102]

        bArr = str_data.encode("utf-8")
        instance = hashlib.md5()
        instance.update(bArr)
        bArr = instance.digest()

        sb = []
        for b in bArr:
            i = b & 255
            sb.append(chr(B[i >> 4]))
            sb.append(chr(B[i & 15]))

        return "".join(sb)
        
    def get_login_signature(self):        
        data=[
        "adid="+self.adid,
        "format="+self.format,
        "device_id="+self.device_id,
        "email="+self.email,
        "password="+self.password,
        "cpl="+self.cpl,
        "family_device_id="+self.family_device_id,
        "credentials_type="+self.credentials_type,
        "generate_session_cookies="+self.generate_session_cookies,
        "error_detail_type="+self.error_detail_type,
        "source="+self.source+self.const_key,
        "machine_id="+self.machine_id,
        "meta_inf_fbmeta="+self.meta_inf_fbmeta,
        "advertiser_id="+self.advertiser_id,
        "currently_logged_in_userid="+self.currently_logged_in_userid,
        "locale="+self.locale,
        "client_country_code="+self.client_country_code,
        "method="+self.method,
        "fb_api_req_friendly_name="+self.fb_api_req_friendly_name,
        "fb_api_caller_class="+self.fb_api_caller_class,
        "api_key="+self.api_key]
        
        data.sort() 
        str_data="".join(data)
        return self.get_signature(str_data)

    def login(self):

        sig_gen=self.get_login_signature()
        
        burp0_url = "https://b-api.facebook.com:443/method/auth.login"
        burp0_headers = {"X-Fb-Friendly-Name": "authenticate",
        "X-Fb-Connection-Quality": "EXCELLENT",
        "X-Fb-Sim-Hni": "722310",
        "X-Fb-Net-Hni": "722310",
        "X-Fb-Connection-Type": "unknown",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 12; SM-N975F Build/SP1A.210812.016) [FBAN/FB4A;FBAV/207.0.0.33.100;FBPN/com.facebook.katana;FBLC/es_US;FBBV/140791848;FBCR/Claro AR;FBMF/samsung;FBBD/samsung;FBDV/SM-N975F;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2069};FB_FW/1;FBRV/0;]",
        "X-Fb-Connection-Bandwidth": "13447418",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate",
        "X-Fb-Http-Engine": "Liger"}
        
        burp0_data = {"adid": self.adid,
        "format": self.format,
        "device_id": self.device_id,
        "email": self.email,
        "password": self.password,
        "cpl": self.cpl,
        "family_device_id": self.family_device_id,
        "credentials_type": self.credentials_type,
        "generate_session_cookies": self.generate_session_cookies,
        "error_detail_type": self.error_detail_type,
        "source": self.source,
        "machine_id": self.machine_id,
        "meta_inf_fbmeta": self.meta_inf_fbmeta,
        "advertiser_id": self.advertiser_id,
        "currently_logged_in_userid": self.currently_logged_in_userid,
        "locale": self.locale,
        "client_country_code": self.client_country_code,
        "method": self.method,
        "fb_api_req_friendly_name": self.fb_api_req_friendly_name,
        "fb_api_caller_class": self.fb_api_caller_class,
        "api_key": self.api_key,
        "sig": sig_gen}
        r=requests.post(burp0_url, headers=burp0_headers, data=burp0_data,timeout=5)
        r_json=r.json()
        
        try:
            self.access_token=str(r_json["access_token"])
            self.uid=str(r_json["uid"])
            return {"access_token":self.access_token,"uid":self.uid}
        except:
            message=r_json["error_msg"]
            code=r_json["error_code"]
            if code==406: #Error 2FA
                self.uid=str(json.loads(r_json["error_data"])["uid"])
                self.login_first_factor=json.loads(r_json["error_data"])["login_first_factor"]
                return {"message":message,"code":code,"uid":self.uid,"login_first_factor":self.login_first_factor}
            return {"message":message,"code":code}
            
            """
            "message":"Login approvals are on. Expect an SMS shortly with a code to use for log in",
            "code":406,
            """
               
            """
            "message":"Invalid username or password",
            "code":401
            """
        
    def get_verify_signature(self):
        data=[
        "adid="+self.adid,
        "advertiser_id="+self.advertiser_id,
        "api_key="+self.api_key,
        "client_country_code="+self.client_country_code,
        "cpl="+self.cpl,
        "credentials_type=two_factor",
        "currently_logged_in_userid="+self.currently_logged_in_userid,
        "device_id="+self.device_id,
        "email="+self.email,
        "error_detail_type="+self.error_detail_type,
        "family_device_id="+self.family_device_id,
        "fb_api_caller_class="+self.fb_api_caller_class,
        "fb_api_req_friendly_name="+self.fb_api_req_friendly_name,
        "first_factor="+self.login_first_factor,
        "format="+self.format,
        "generate_session_cookies="+self.generate_session_cookies,
        "locale="+self.locale,
        "machine_id="+self.machine_id,
        "meta_inf_fbmeta=NO_FILE",
        "method="+self.method,
        "password="+self.password,
        "source=login",
        "try_num=1",
        "twofactor_code="+self.password,
        "userid="+self.uid+self.const_key
        ]
        
        data.sort() 
        str_data="".join(data)
        return self.get_signature(str_data)
        
    def verify_2FA(self):
        sig_gen=self.get_verify_signature()

        burp0_url = "https://b-api.facebook.com:443/method/auth.login"
        burp0_headers = {"X-Fb-Friendly-Name": "authenticate",
        "X-Fb-Connection-Quality": "EXCELLENT",
        "X-Fb-Sim-Hni": "722310",
        "X-Fb-Net-Hni": "722310",
        "X-Fb-Connection-Type": "unknown",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 12; SM-N975F Build/SP1A.210812.016) [FBAN/FB4A;FBAV/207.0.0.33.100;FBPN/com.facebook.katana;FBLC/es_US;FBBV/140791848;FBCR/Claro AR;FBMF/samsung;FBBD/samsung;FBDV/SM-N975F;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2069};FB_FW/1;FBRV/0;]",
        "X-Fb-Connection-Bandwidth": "13447418",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate",
        "X-Fb-Http-Engine": "Liger"}
        
        burp0_data = {"adid":self.adid,
        "advertiser_id":self.advertiser_id,
        "api_key":self.api_key,
        "client_country_code":self.client_country_code,
        "cpl":self.cpl,
        "credentials_type":"two_factor",
        "currently_logged_in_userid":self.currently_logged_in_userid,
        "device_id":self.device_id,
        "email":self.email,
        "error_detail_type":self.error_detail_type,
        "family_device_id":self.family_device_id,
        "fb_api_caller_class":self.fb_api_caller_class,
        "fb_api_req_friendly_name":self.fb_api_req_friendly_name,
        "first_factor":self.login_first_factor,
        "format":self.format,
        "generate_session_cookies":self.generate_session_cookies,
        "locale":self.locale,
        "machine_id":self.machine_id,
        "meta_inf_fbmeta":"NO_FILE",
        "method":self.method,
        "password":self.password,
        "source":"login",
        "try_num":"1",
        "twofactor_code":self.password,
        "userid":self.uid,
        "sig": sig_gen}
        
        r=requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
        r_json=r.json()
        
        try:
            self.access_token=str(r_json["access_token"])
            return {"access_token":self.access_token,"uid":self.uid}
        except: # incorrect pin
            message=r_json["error_msg"]
            code=r_json["error_code"]
            print(message,type,code)  
            return {"message":message,"code":code}

    def get_timestamp_now(self):
        timestamp =  str(int(round(time.time())))
        return timestamp

    def is_alive(self):
        try:
            burp0_url = "https://graph.facebook.com:443/graphql?locale=es_LA"
            burp0_headers = {"X-Zero-Eh": "2,,AW1yeNIME6oYtHQhy5EHk8D7mWM9H1Ws8rnvShBgXm4YB53nEHXlVizrng7P4qYr2n4", 
            "X-Fb-Sim-Hni": "722310", 
            "X-Fb-Net-Hni": "722310", 
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 12; SM-N975F Build/SP1A.210812.016) [FBAN/FB4A;FBAV/207.0.0.33.100;FBPN/com.facebook.katana;FBLC/es_US;FBBV/140791848;FBCR/Claro AR;FBMF/samsung;FBBD/samsung;FBDV/SM-N975F;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2069};FB_FW/1;FBRV/141746013;]", 
            "Content-Type": "application/x-www-form-urlencoded", 
            "Accept-Encoding": "gzip, deflate", 
            "X-Fb-Http-Engine": "Liger"}
            
            burp0_data = {"access_token": self.access_token, "fb_api_caller_class": "RelayModern", "variables": "{\"root_id\":\"303635947041725\",\"scale\":2.625}", "doc_id": "2167307960027518"}
            r=requests.post(burp0_url, headers=burp0_headers, data=burp0_data,timeout=5)
            r_json=r.json()

            for c in r_json["data"]["settings"]["children"][0]["children"]:
                if c["title"]=="Nombre":
                    self.full_name=c["description"][0]
            return True
        except:
            return False

    def upload_photo(self,image_binary,images_binary,id_group,composer_session_id,idempotence_token):

        burp0_url = "https://graph.facebook.com:443/me/photos"
        burp0_headers = {
        "Authorization": "OAuth "+self.access_token, 
        "X-Fb-Friendly-Name": "upload-photo", 
        "X-Zero-Eh": "2,,ATeXt1CiZAbhnku1-vpXJsCVfyr_HgHf4yZtKl-thisCiTCrxn6h04IxWNyXcderlAE", 
        "X-Fb-Connection-Quality": "EXCELLENT", 
        "X-Fb-Sim-Hni": "722310", 
        "X-Fb-Net-Hni": "722310", 
        "X-Fb-Connection-Type": "unknown", 
        "User-Agent": "[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129281;FBDM/{density=2.625,width=1080,height=2069};FBLC/es_LA;FBRV/228899333;FBCR/Claro AR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975F;FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;]", 
        "X-Fb-Connection-Bandwidth": "20486982", 
        "X-Fb-Socket-Option": "TCP_CONGESTION=bbr", 
        "X-Tigon-Is-Retry": "False", 
        "Accept-Encoding": "gzip, deflate", 
        "X-Fb-Http-Engine": "Liger"
        }
        
        idempotence_token=idempotence_token+"_"+str(random.randint(100000000, 999999999))+"_"+str(images_binary.index(image_binary))
        
        if id_group!=0:
            source_type="group"
        else:
            source_type="timeline"
        
        files={
        'published':(None,'false',('text/plain; charset=UTF-8',{'Content-Transfer-Encoding': '8bit'})),
        'audience_exp':(None,'true',('text/plain; charset=UTF-8',{'Content-Transfer-Encoding': '8bit'})),
        'qn':(None,composer_session_id,('text/plain; charset=UTF-8',{'Content-Transfer-Encoding': '8bit'})),
        'composer_session_id':(None,composer_session_id,('text/plain; charset=UTF-8',{'Content-Transfer-Encoding': '8bit'})),
        'idempotence_token':(None,idempotence_token,('text/plain; charset=UTF-8',{'Content-Transfer-Encoding': '8bit'})),
        'source_type':(None,source_type,('text/plain; charset=UTF-8',{'Content-Transfer-Encoding': '8bit'})),
        'locale':(None,'es_LA',('text/plain; charset=UTF-8',{'Content-Transfer-Encoding': '8bit'})),
        'client_country_code':(None,'AR',('text/plain; charset=UTF-8',{'Content-Transfer-Encoding': '8bit'})),
        'fb_api_req_friendly_name':(None,'upload-photo',('text/plain; charset=UTF-8',{'Content-Transfer-Encoding': '8bit'})),
        'fb_api_caller_class':(None,'com.facebook.photos.upload.uploaders.MultiPhotoUploader',('text/plain; charset=UTF-8',{'Content-Transfer-Encoding': '8bit'})),
        'source':('3eae63ee-3f93818b1cc08729.tmp',image_binary,('image/jpeg',{'Content-Transfer-Encoding': 'binary'}))
        }
        
        r= requests.post(burp0_url, headers=burp0_headers, files=files,timeout=5)
        
        r_json=r.json()
        id=str(r_json["id"])
        
        if id_group!=0:     
            json_img={
            "photo":
                {
                "unified_stories_media_source":"CAMERA_ROLL",
                "id":id
                }
            }
        else:
            json_img={
            "photo":
                {
                "media_source_info":
                    {
                    "source":"UPLOADED",
                    "entry_point":"OTHER"
                    },
                "id":id
                }
            }
             
        return json_img

    def make_post(self,post):
        client_mutation_id=self.get_token()
        composer_session_id=self.get_token()
        deduplication_id=composer_session_id
        idempotence_token="FEED_"+composer_session_id
        timestamp=self.get_timestamp_now()

        burp0_url = "https://graph.facebook.com:443/graphql"
        
        burp0_headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Fb-Friendly-Name": "ComposerStoryCreateMutation",
        "User-Agent": "[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129281;FBDM/{density=2.625,width=1080,height=2069};FBLC/es_LA;FBRV/228899333;FBCR/Claro AR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975F;FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
        "X-Fb-Net-Hni": "722310",
        "X-Fb-Sim-Hni": "722310",
        "Authorization": "OAuth "+self.access_token,
        "X-Fb-Connection-Type": "WIFI",
        "X-Fb-Socket-Option": "TCP_CONGESTION=bbr",
        "X-Tigon-Is-Retry": "False",
        "Accept-Encoding": "gzip, deflate",
        "X-Fb-Http-Engine": "Liger"
        }
        
        json_variables={
        "reading_attachment_profile_image_height":354,
        "profile_pic_media_type":"image/x-auto",
        "poll_facepile_size":105,
        "image_medium_height":2048,
        "image_large_aspect_width":1080,
        "media_type":"image/jpeg",
        "nt_context":{
            "using_white_navbar":True,
            "styles_id":"3a01b3513dd2f828d4890b6a53bfc00c",
            "pixel_ratio":3
            },
        "image_medium_width":540,
        "fetch_fbc_header":True,
        "size_style":"contain-fit",
        "action_location":"feed",
        "rich_text_posts_enabled":"false",
        "enable_comment_reactions_icons":True,
        "reading_attachment_profile_image_width":236,
        "enable_ranked_replies":"true",
        "enable_comment_shares":True,
        "default_image_scale":"3",
        "angora_attachment_cover_image_size":1260,
        "question_poll_count":100,
        "image_high_height":2048,
        "angora_attachment_profile_image_size":105,
        "should_fetch_share_count":"false",
        "input":
            {
            "reshare_original_post":"SHARE_LINK_ONLY",
            "producer_supported_features":["LIGHTWEIGHT_REPLY"],
            "place_attachment_setting":"SHOW_ATTACHMENT",
            "past_time":
                {
                "time_since_original_post":0
                },
            "composer_entry_point":"inline_composer",
            "connection_class":"EXCELLENT",
            "composer_entry_picker":"NULL",
            "actor_id":self.uid,
            "is_group_linking_post":False,
            "camera_post_context":
                {
                "source":"COMPOSER",
                "platform":"FACEBOOK",
                "deduplication_id":deduplication_id
                },
            "action_timestamp":self.get_timestamp_now(),
            "audiences_is_complete":True,
            "audiences":[],
            "ads_animator_metadata":None,
            "composer_source_surface":"newsfeed",
            "client_mutation_id":client_mutation_id,
            "logging":
                {
                "composer_session_id":composer_session_id
                },
            "composer_type":"status",
            "sponsor_id":None,
            "idempotence_token":idempotence_token,
            "extensible_sprouts_ranker_request":
                {
                "RequestID":""
                },
            "is_tags_user_selected":False,
            "is_boost_intended":False,
            "is_throwback_post":"NOT_THROWBACK_POST",
            "message":
                {
                "text":post.get_description(),
                "ranges":[]
                },
            "video_start_time_ms":0,
            "source":"MOBILE",
            "composer_session_events_log":
                {
                "number_of_keystrokes":5,
                "number_of_copy_pastes":0,
                "composition_duration":3
                },
            "nectar_module":"newsfeed_composer",
            "attachments":[]
            },
        "enable_comment_reactions":True,
        "automatic_photo_captioning_enabled":"false",
        "image_large_aspect_height":559,
        "image_low_width":360,
        "image_high_width":1080,
        "profile_image_size":105,
        "poll_voters_count":5,
        "enable_comment_replies_most_recent":"true",
        "max_comment_replies":3,
        "image_low_height":2048
        }
        
        for image_binary in post.get_images_binary():
            json_variables["input"]["attachments"].append(self.upload_photo(image_binary,post.get_images_binary(),post.get_id_group(),composer_session_id,idempotence_token))
        
        if (post.get_id_group()!="0"): # post for profile
            json_variables["input"]["audiences"].append(
                {
                "wall":
                    {
                    "to_id":post.get_id_group()
                    }
                })
        else: #post for group
            json_variables["input"]["audiences"].append(
                {
                "undirected":
                    {
                    "privacy":
                        {
                        "tag_expansion_state":"UNSPECIFIED",
                        "base_state":"EVERYONE",
                        "deny":[],
                        "allow":[]
                        }
                    }
                })
        
        json_nav_attribution_id={
        "0":
            {
            "bookmark_id":"",
            "session":"",
            "subsession":1,
            "timestamp":timestamp,
            "tap_point":"cold_start",
            "bookmark_type_name":None,
            "fallback":False
            }
        }
        
        json_fb_api_analytics_tags=[
        "GraphServices",
        "nav_attribution_id="+json.dumps(json_nav_attribution_id),
        "visitation_id=::1:"+timestamp,"surface_hierarchy=ComposerFragment,null,null;ComposerActivity,composer,null;NewsFeedFragment,native_newsfeed,null;FbChromeFragment,null,cold_start;FbMainTabActivity,unknown,null",
        "session_id="]

        burp0_data = {
        "doc_id": "3910201005720328",
        "method": "post",
        "locale": "es_LA",
        "pretty": "false",
        "format": "json",
        "variables": json.dumps(json_variables),
        "fb_api_req_friendly_name": "ComposerStoryCreateMutation",
        "fb_api_caller_class": "graphservice",
        "fb_api_analytics_tags": json.dumps(json_fb_api_analytics_tags),
        "server_timestamps": "true"
        }
        
        r=requests.post(burp0_url, headers=burp0_headers, data=burp0_data,timeout=5)
        
        r_json=r.json()
        url=r_json["data"]["story_create"]["story"]["url"]
        
        return url

    def get_user_information(self):
        burp0_url = "https://graph.facebook.com:443/graphql"
        burp0_headers = {
        "X-Graphql-Client-Library": "graphservice",
        "X-Graphql-Request-Purpose": "refresh",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Fb-Privacy-Context": "2644666885789663",
        "X-Fb-Background-State": "1",
        "User-Agent": "[FBAN/FB4A;FBAV/396.1.0.28.104;FBBV/429651044;FBDM/{density=2.625,width=1080,height=2069};FBLC/es_LA;FBRV/435144331;FBCR/Claro AR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975F;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]",
        "X-Fb-Net-Hni": "722310",
        "X-Fb-Sim-Hni": "722310",
        "Authorization": "OAuth "+self.access_token,
        "X-Fb-Session-Id": "nid=1hsx8OIWc8b0;tid=155;nc=0;fc=2;bc=1;cid=7507673a64ad69e0f5d8685e95327778",
        "X-Fb-Connection-Type": "WIFI",
        "X-Fb-Device-Group": "7325",
        "X-Fb-Qpl-Active-Flows-Json": "{\"schema_version\":\"v2\",\"inprogress_qpls\":[{\"marker_id\":25952257,\"annotations\":{\"current_endpoint\":\"ProfileFragment:profile_vnext_tab_posts\"}}],\"snapshot_attributes\":{}}",
        "X-Tigon-Is-Retry": "False",
        "X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE",
        "X-Fb-Friendly-Name": "UserTimelineQuery",
        "X-Fb-Request-Analytics-Tags": "graphservice",
        "Priority": "u=3, i",
        "Accept-Encoding": "gzip, deflate",
        "X-Fb-Http-Engine": "Liger",
        "X-Fb-Client-Ip": "True",
        "X-Fb-Server-Cluster": "True",
        "X-Fb-Connection-Token": "7507673a64ad69e0f5d8685e95327778"}
        
        json_variables = {"profile_id":self.uid}
        
        burp0_data = {
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
        
        r=requests.post(burp0_url, headers=burp0_headers, data=burp0_data)
        
        print(r.text)
        
        image_binary=None
        full_name=None
        
        try:
            r_json = [json.loads(s) for s in r.text.split("\n")]
            for e_json in r_json:
                try:
                    full_name=e_json["data"]["user"]["name"]
                    image_url=e_json["data"]["user"]["profile_photo"]["image"]["uri"]
                except:
                    pass
            image_binary=self.download_imagen(image_url)
        except:
            pass
            
        user_information={"full_name":full_name,"image":image_binary }
        
        return user_information
    
    def download_imagen(self,url):
        r = requests.get(url)
        r.raise_for_status()
        return r.content.decode('Latin_1')    
    
    def get_groups(self):
        burp0_url = "https://graph.facebook.com:443/graphql"
        burp0_headers = {
        "Content-Type": "application/x-www-form-urlencoded", 
        "X-Fb-Friendly-Name": "FetchGroupsTabGroupPogsAtConnection", 
        "User-Agent": "[FBAN/FB4A;FBAV/276.0.0.44.127;FBBV/225129281;FBDM/{density=2.625,width=1080,height=2069};FBLC/es_LA;FBRV/228899333;FBCR/Claro AR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N975F;FBSV/12;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
        "X-Fb-Net-Hni": "722310",
        "X-Fb-Sim-Hni": "722310",
        "Authorization": "OAuth "+self.access_token,
        "X-Fb-Connection-Type": "WIFI",
        "X-Fb-Socket-Option": "TCP_CONGESTION=bbr",
        "X-Tigon-Is-Retry": "False",
        "Accept-Encoding": "gzip, deflate",
        "X-Fb-Http-Engine": "Liger"}
        
        json_variables={"group_item_small_cover_photo_size":105,
        "group_item_small_cover_photo_height":105,
        "entry_point":"TAB_STORIES",
        "group_list_type":"ALL_GROUPS", #ALL_GROUPS_WITHOUT_PINNED
        "badged_group_list_connection_first":1000
        }
        
        fb_api_analytics_tags=["GraphServices","At_Connection"]
        
        burp0_data = {
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
        
        r=requests.post(burp0_url, headers=burp0_headers, data=burp0_data,timeout=5)

        groups=[]

        try:
            r_json=r.json()
            
            cantidad= r_json["data"]["viewer"]["groups_tab"]["badged_group_list"]["count"]
            print("Cantidad grupos: ",cantidad)

            for group in r_json["data"]["viewer"]["groups_tab"]["badged_group_list"]["edges"]:
                name=group["node"]["name"]
                id=group["node"]["id"]
                url=group["node"]["groupItemProfilePic"]["uri"]
                groups.append({"name":name,"id":id,"url":url})
        except:
            pass
        return {"groups":groups}

