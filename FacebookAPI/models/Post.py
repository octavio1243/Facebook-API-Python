from FacebookAPI.enums.XFbFriendlyName import XFbFriendlyName
from FacebookAPI.config import GRAPH_URL
import random
import requests
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
    
    def upload_and_generate_json_image(self, image_index, image, composer_session_id, idempotence_token):

        url = f"{GRAPH_URL}/me/photos"
        self.user.device.app.headers.set_header("X-Fb-Friendly-Name", XFbFriendlyName.UPLOAD_PHOTO.value)
        self.user.device.app.headers.set_header("Authorization", f"OAuth {self.user.access_token}")
        headers = self.user.device.app.headers.get_all_headers()
        
        idempotence_token=idempotence_token+"_"+str(random.randint(100000000, 999999999))+"_"+str(image_index)
        
        if self.group.id!=0:
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
        'source':('3eae63ee-3f93818b1cc08729.tmp',image.get_binary(),('image/jpeg',{'Content-Transfer-Encoding': 'binary'}))
        }

        try:
            r= requests.post(url, headers = headers, files = files, timeout = 5)
            
            """
            print(f"URL: {r.request.url}")
            print(f"Método: {r.request.method}")
            print(f"Encabezados: {r.request.headers}")
            print(f"Cuerpo de la solicitud: {r.request.body}")
            """
            print(r.text)
            
            r_json=r.json()
            id=str(r_json["id"])
        
            if self.group.id!=0:     
                json_image={
                "photo":
                    {
                    "unified_stories_media_source":"CAMERA_ROLL",
                    "id":id
                    }
                }
            else:
                json_image={
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
            return json_image
        except:
            raise Exception("Error. It can not upload image to group")

    def make(self):
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
            
        for image_index,image in enumerate(self.images):
            json_variables["input"]["attachments"].append(self.upload_and_generate_json_image(image_index,image,composer_session_id,idempotence_token))

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
        
        print(r.text)

        r_json=r.json()
        url=r_json["data"]["story_create"]["story"]["url"]
        
        return {"url":url}
