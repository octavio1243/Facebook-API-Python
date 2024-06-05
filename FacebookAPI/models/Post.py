from FacebookAPI.enums.XFbFriendlyName import XFbFriendlyName
from FacebookAPI.config import GRAPH_URL
from FacebookAPI.config import MBASIC_URL
import requests
from bs4 import BeautifulSoup
import brotli
import re
import random
import json

class Post():
    
    # It doesn't support images. The API has changed ! 
    def __init__(self,user = None, description = None, images = [], group = None):
        if user is None:
            raise Exception("Error: The user can not be None")
        if description is None:
            raise Exception("Error: The post description can not be None")
        if group is None:
            raise Exception("Error: The group can not be None")
        self.user = user
        self.images = images
        self.description = description
        self.group = group
    
    def decode_content(self, response):
        content = response.content
        try:
            if response.headers.get('Content-Encoding') == 'br':
                content = brotli.decompress(response.content).decode('utf-8')
            elif response.headers.get('Content-Encoding') == 'gzip':
                print("Make the implementation to decode the content")
        except:
            pass
            #print("Error to decode the content. Maybe it isn't encoded")
        #print(content,"\n\n")
        return content

    def get_headers(self, previous_url):
        headers = {
        "Cache-Control": "max-age=0", 
        "Upgrade-Insecure-Requests": "1", 
        "Origin": f"{MBASIC_URL}", 
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
        "Sec-Fetch-Site": "same-origin", 
        "Sec-Fetch-Mode": "navigate", 
        "Sec-Fetch-User": "?1", 
        "Sec-Fetch-Dest": "document",
        "Accept-Encoding": "gzip, deflate, br", 
        "Accept-Language": "es-ES,es;q=0.9", 
        "Priority": "u=0, i"
        }

        if previous_url:
            headers["Referer"] = f"{previous_url}"

        return headers

    def get_next_request(self, response):
        content = self.decode_content(response)
        soup = BeautifulSoup(content, 'html.parser')
        form = soup.find('form', method='post')
        action = form.get('action')
        inputs = form.find_all('input')
        text_areas = form.find_all('textarea')
        
        require_text_area = None
        required_files = {}
        data ={}
        for input in inputs:
            key = input.get('name')
            value = input.get('value','')
            if input.get('type') == "file":
                required_files[key]=b""
            elif key in data:
                if isinstance(data[key], list):
                    data[key].append(value)
                else:
                    data[key] = [data[key], value]
            else:
                data[key] = value
        for text_area in text_areas:
            data[text_area.get('name')] = text_area.get('value','')
            require_text_area = text_area.get('name')
        
        headers = self.get_headers(response.url)
        return action, headers, data, required_files, require_text_area

    def get_permalink(self, response):
        pattern = re.compile(r'.*\/permalink\/\d+')
        content = self.decode_content(response)
        soup = BeautifulSoup(content, 'html.parser')
        articles = soup.find_all('article')
        for article in articles:
            links =article.find_all('a')
            for link in links:
                href = link.get("href",None)
                #print(link," - ",href)
                match = pattern.search(href)
                if match:
                    return match.group(0)
        return "Error: Link not founded"

    def make_next_request(self, response,num):
        action, headers, data, required_files, require_text_area = self.get_next_request(response)
        url = f"{MBASIC_URL}{action}"
        #print(f"POST to URL: {url}")
        if require_text_area and num == 3:
            data[require_text_area]=f"{self.description}"
        if required_files:
            if len(self.images)>len(required_files):
                raise Exception(f"The files are too many. The max is {len(required_files)}")
            for i, key in enumerate(required_files):
                if i < len(self.images):
                    required_files[key]=self.images[i].get_binary()
            #print(required_files)
            response = requests.post(url, data=data, files=required_files, headers=headers, cookies=self.user.get_cookies(),timeout=20)
        else:  
            response = requests.post(url, data=data, headers=headers, cookies=self.user.get_cookies(),timeout=10)
        
        if num<3:
            link = self.make_next_request(response,num+1)
        else:
            link = self.get_permalink(response)
        return link

    def make_with_images(self):        
        group_url = f"{MBASIC_URL}/groups/{self.group.id}"
        headers = self.get_headers(None)
        response = requests.get(group_url, headers=headers, cookies=self.user.get_cookies(),timeout=10)
        link = self.make_next_request(response,1)
        return {"post_url": link}
    
    def make_without_images(self):
        client_mutation_id = self.user.device.app.get_token()
        composer_session_id = self.user.device.app.get_token()
        deduplication_id=composer_session_id
        idempotence_token="FEED_"+composer_session_id
        timestamp=self.user.device.app.get_timestamp()

        url = f"{GRAPH_URL}/graphql"
        
        self.user.device.app.headers.set_header("X-Fb-Friendly-Name", XFbFriendlyName.COMPOSER_STORY_CREATE_MUTATION.value)
        self.user.device.app.headers.set_header("Authorization", f"OAuth {self.user.access_token}")
        headers = self.user.device.app.headers.get_all_headers()
        
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
            "actor_id":self.user.uid,
            "is_group_linking_post":False,
            "camera_post_context":
                {
                "source":"COMPOSER",
                "platform":"FACEBOOK",
                "deduplication_id":deduplication_id
                },
            "action_timestamp":self.user.device.app.get_timestamp(),
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
                "text":self.description,
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
        
        if (self.group.id!="0"): # post for profile
            json_variables["input"]["audiences"].append(
                {
                "wall":
                    {
                    "to_id":self.group.id
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

        data = {
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
        
        r=requests.post(url, headers = headers, data = data, timeout = 5)
        
        #print(r.text)

        r_json=r.json()
        url=r_json["data"]["story_create"]["story"]["url"]
        
        return {"post_url":url}
    
    def make(self):        
        if self.images:
            return self.make_with_images()
        else:
            return self.make_without_images()