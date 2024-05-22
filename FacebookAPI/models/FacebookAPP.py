from FacebookAPI.models.Header import Header
import random
import uuid
import hashlib
import time

class FacebookAPP():
    adid="dd709e93-08e4-4a4c-b9bd-c41d6d9a7092" #Constant
    advertiser_id="dd709e93-08e4-4a4c-b9bd-c41d6d9a7092" #Constant
    api_key="882a8490361da98702bf97a021ddc14d" #Constant
    const_key="62f8ce9f74b12f84c123cc23437a4a32" #const-string from smali code
    cpl="true" # Constant?
    currently_logged_in_userid="0" #Constant
    error_detail_type="button_with_disabled" #Constant
    fb_api_caller_class="com.facebook.account.login.protocol.Fb4aAuthHandler" #Constant
    fb_api_req_friendly_name="authenticate" #Constant
    format="json" #Constant
    generate_session_cookies="1" #Constant
    method="auth.login" #Constant    
    
    def __init__(self, client_country_code, locale, user_agent):
        self.client_country_code = client_country_code
        self.locale = locale
        self.headers = Header()
        
        # Custom Headers
        self.headers.set_header("User-Agent", user_agent)
        
        # Autogen Headers
        self.headers.set_header("X-Fb-Connection-Quality", self.get_x_fb_connection_quality())
        self.headers.set_header("X-Fb-Connection-Type", self.get_x_fb_connection_type())
        self.headers.set_header("X-Fb-Connection-Bandwidth", self.get_x_fb_connection_bandwidth())
        self.headers.set_header("X-Zero-Eh", self.get_x_zero_eh())

        # Constant Headers
        self.headers.set_header("X-Fb-Sim-Hni", "722310")
        self.headers.set_header("X-Fb-Net-Hni", "722310")
        self.headers.set_header("X-Fb-Http-Engine", "Liger")
        self.headers.set_header("X-Fb-Socket-Option", "TCP_CONGESTION=bbr")
        self.headers.set_header("X-Fb-Privacy-Context", "2644666885789663")
        self.headers.set_header("X-Fb-Background-State", "1")
        self.headers.set_header("X-Fb-Session-Id", "nid=1hsx8OIWc8b0;tid=155;nc=0;fc=2;bc=1;cid=7507673a64ad69e0f5d8685e95327778")
        self.headers.set_header("X-Fb-Device-Group", "7325")
        self.headers.set_header("X-Fb-Qpl-Active-Flows-Json", "{\"schema_version\":\"v2\",\"inprogress_qpls\":[{\"marker_id\":25952257,\"annotations\":{\"current_endpoint\":\"ProfileFragment:profile_vnext_tab_posts\"}}],\"snapshot_attributes\":{}}")
        self.headers.set_header("X-Fb-Rmd", "cached=0;state=URL_ELIGIBLE")
        self.headers.set_header("X-Fb-X-Fb-Request-Analytics-Tags", "graphservice")
        self.headers.set_header("X-Fb-Client-Ip", "True")
        self.headers.set_header("X-Fb-Server-Cluster", "True")
        self.headers.set_header("X-Fb-Connection-Token", "7507673a64ad69e0f5d8685e95327778")
        self.headers.set_header("X-Graphql-Client-Library", "graphservice")
        self.headers.set_header("X-Graphql-Request-Purpose", "refresh")
        self.headers.set_header("X-Tigon-Is-Retry", "False")
        self.headers.set_header("Content-Type", "application/x-www-form-urlencoded")
        self.headers.set_header("Accept-Encoding", "gzip, deflate")
        self.headers.set_header("Priority", "u=3, i")
    
    def get_x_fb_connection_quality(self):
        return "EXCELLENT"
    
    def get_x_fb_connection_type(self):
        return "WIFI" # or "unknown"
    
    def get_x_fb_connection_bandwidth(self):
        return "13447418" # or 20486982

    def get_x_zero_eh(self):
        return "2,,AW1yeNIME6oYtHQhy5EHk8D7mWM9H1Ws8rnvShBgXm4YB53nEHXlVizrng7P4qYr2n4"

    def get_token(self):
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

    def get_timestamp(self):
        timestamp =  str(int(round(time.time())))
        return timestamp

  