
class Header():
    
    def __init__(self):
        self.headers = {}

    def set_header(self, key, value):
        self.headers[key] = value

    def get_header(self, key):
        return self.headers.get(key)

    def get_all_headers(self):
        return self.headers
