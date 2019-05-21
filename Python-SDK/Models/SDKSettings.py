from . import SDKModules as Modules
#===================================================
#  Ocugine SDK
#  Sofware Development Kit developed specially for
#  Ocugine Services. With this library you can
#  use all features of Ocugine Services
#
#  @name           Ocugine SDK
#  @developer      CodeBits Interactive
#  @version        0.4.0a
#  @build          401
#  @url            https:#ocugine.pro/
#  @docs           https:#docs.ocugine.pro/
#  @license        MIT
#===================================================


#================================================
#  Ocugine SDKs Settings Model
#================================================
class SDKSettings():

    language = "EN";                            # SDK Language
    modules = None;                             # SDK Modules 
    auth_timeout = 30;                          # Auth timeout

    #================================================
    # @class        SDKSettings
    # @method       __init__  
    # @usage        Constructor
    # @args         none
    #================================================
    def __init__(self, _Language, _Modules, _Timeout):
        self.language = _Language;
        self.modules = _Modules;
        self.timeout = _Timeout;   

#================================================
# Ocugine Application Settings Model
#================================================
class AppSettings():

    app_id = "";                                # Application ID
    app_key = "";                               # Application Key
    app_name = "";                              # Application Name
    app_desc = "";                              # Application Desc
    app_version = "";                           # Application Version

    #================================================
    # @class        APPSettings
    # @method       __init__  
    # @usage        Constructor
    # @args         none
    #================================================
    def __init__(self, _AppID, _AppKey):
        self.app_id = _AppID;
        self.app_key = _AppKey;




