from FacebookAPI.config import GRAPH_URL
import requests
import json

class Post():
    
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
    
    def upload_image_from_url(self, image_url, retries=3):        
        url = f'{GRAPH_URL}/v20.0/{self.group.id}/photos?access_token={self.user.access_token}'
        
        params = {
            'published': 'false',
            'url': image_url,
        }
        response = requests.post(url, params=params)
        
        if response.status_code == 200:
            return response.json()['id']
        if retries>0:
            return self.upload_image_from_url(image_url, retries-1)
        
        return None
    
    def make(self):        
        print(self.user,
        self.images,
        self.description,
        self.group)

        url = f'{GRAPH_URL}/v20.0/{self.group.id}/feed?access_token={self.user.access_token}'
        
        attached_media = []
        for image in self.images:
            image_id = self.upload_image_from_url(image.url)
            if image_id:
                attached_media.append(f'{{"media_fbid":"{image_id}"}}')

        payload = {
            'message': self.description,
        }
        
        if attached_media:
            payload['attached_media'] = json.dumps(attached_media)

        response = requests.post(url, data=payload)
        
        if response.status_code == 200:
            return {"group_post_id":response.json()["id"]}
        
        return {"url":None}