from . import SDKModules as Modules

"""description of class"""
class SDKSettings():
    language = "";                      # SDK Language
    modules : Modules.SDKModules = [];  # SDK Modules 
    auth_timeout = 0;                   # Auth timeout

class AppSettings():
    app_id = 0;                         # Application ID
    app_key = "";                       # Application Key
    app_name = "";                      # Application Name
    app_desc = "";                      # Application Desc
    app_version = "";                   # Application Version



