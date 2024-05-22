from FacebookAPI.models.FacebookAPP import FacebookAPP
import uuid

class Device():

    def __init__(self, device_id = None, machine_id = None, family_device_id = None, user_agent = None, client_country_code = None, locale = None):
        if device_id is None:
            device_id = self.generate_device_id()
        if machine_id is None:
            machine_id = self.generate_machine_id()
        if family_device_id is None:
            family_device_id = self.generate_family_device_id()
        if user_agent is None:
            user_agent = self.generate_user_agent()
        if client_country_code is None:
            client_country_code = self.generate_client_country_code()
        if locale is None:
            locale = self.generate_locale()
        
        self.device_id = device_id
        self.machine_id = machine_id
        self.family_device_id = family_device_id
        self.app = FacebookAPP(client_country_code, locale, user_agent)

    def generate_device_id(self):
        print("Device ID Generated")
        return str(uuid.uuid4())
    
    def generate_machine_id(self):
        print("Machine ID Generated")
        return "0k0hZkcZegv11yc2w1Iao-uA" # Research how generate

    def generate_family_device_id(self):
        print("Family Device ID Generated")
        return "686ffda5-e9af-464a-944e-3bbd4e1850ea" # Research how generate

    def generate_user_agent(self):
        print("User Agent Generated")
        return "Dalvik/2.1.0 (Linux; U; Android 12; SM-N975F Build/SP1A.210812.016) [FBAN/FB4A;FBAV/207.0.0.33.100;FBPN/com.facebook.katana;FBLC/es_US;FBBV/140791848;FBCR/Claro AR;FBMF/samsung;FBBD/samsung;FBDV/SM-N975F;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2069};FB_FW/1;FBRV/0;]" # Get of an list randomly

    def generate_client_country_code(self):
        print("Client Country Generated")
        return "AR" # Get of an list randomly
    
    def generate_locale(self):
        print("Locale Generated")
        return "es_LA" # Get of an list randomly
