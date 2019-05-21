from . import SDKModules as Modules

"""description of class"""
class SDKSettings():

    language = "EN";                            # SDK Language
    modules = None;                             # SDK Modules 
    auth_timeout = 30;                          # Auth timeout

    def __init__(self, _Language, _Modules, _Timeout):
        self.language = _Language;
        self.modules = _Modules;
        self.timeout = _Timeout;   

class AppSettings():

    app_id = "";                                # Application ID
    app_key = "";                               # Application Key
    app_name = "";                              # Application Name
    app_desc = "";                              # Application Desc
    app_version = "";                           # Application Version

    def __init__(self, _AppID, _AppKey):
        self.app_id = _AppID;
        self.app_key = _AppKey;




