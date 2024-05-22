import requests

class Image():
    
    def __init__(self, url = None, binary = None):
        if url is None and binary is None:
            raise Exception("Error to create image. The url or binary is required")
        self.url = url
        self.binary = binary

    def get_binary(self):
        if self.binary is None:
            r = requests.get(self.url)
            r.raise_for_status()
            self.binary = r.content.decode('Latin_1')
        return self.binary
