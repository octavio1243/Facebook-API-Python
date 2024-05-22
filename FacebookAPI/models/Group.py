
class Group():
    def __init__(self,id = None, name = None, url = None, number_of_members = None ):
        if id is None:
            raise Exception("Group ID is required")
        self.id = id
        self.name = name
        self.url = url
        self.number_of_members = number_of_members

    def get_json(self):
        return {"id":self.id,"name":self.name,"image_url":self.url,"number_of_members":self.number_of_members}
