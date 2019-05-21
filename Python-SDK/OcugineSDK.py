import Models.SDKModules as SDKModules
import Models.SDKSettings as SDKSettings

#===================================================
#  Ocugine SDK
#  Sofware Development Kit developed specially for
#  Ocugine Services. With this library you can
#  use all features of Ocugine Services
#
#  # @name           Ocugine SDK
#  # @developer      CodeBits Interactive
#  # @version        0.4.0a
#  # @build          401
#  # @url            https:#ocugine.pro/
#  # @docs           https:#docs.ocugine.pro/
#  # @license        MIT
#===================================================
class Ocugine(object):

    PROTOCOL = "https:#";       # Requests Protocol
    SERVER = "cp.ocugine.pro";  # Server URL
    SSL = True;                 # SSL
    API_GATE = "/api/";         # API Gateway
    VERSION = "0.4.0a";         # Library Version
    BUILD = 401;                # Library Build

    # Settings Instances
    application = None;         # Application Settings
    settings = None;            # SDK Settings

    # Classes Instances
    auth = None;                                # Authentication Class
    analytics  = None;                      # Analytics Class
    game = None;                        # Game Services
    monetization = None;                    # Monetization Services
    notifications  = None;              # Notifications Services
    marketing = None;                      # Marketing Services
    ads = None;                                  # Ads Services
    backend = None;                          # Backend Services
    reports  = None;                        # Reporting Services
    perfomance  = None;                   # Perfomance Services
    office  = None;                        # Office Services
    locale = None;                      # Locale Services
    users  = None;                              # User Class
    ui = None;                                    # UI Module
    utils  = None;                              # Utils Module

    # Private Class Params
    STATE_OBJECT = "state";    # State Object

    # Public Class Params
    OAUTH_OBJECT = "oauth";     
    USERS_OBJECT = "users";      
    SETTINGS_OBJECT = "api_settings";
    LOCALE_OBJECT = "localization";
    CLOUD_OBJECT = "cloud";

    def __init__(self, app_settings : SDKSettings.AppSettings, sdk_settings : SDKSettings.SDKSettings): # Constructor
        self.application = app_settings;
        self.settings = sdk_settings;
        Ocugine._initializeModules(self);
    
    #====================================
    # @class      General
    # @method     _initializeModules()
    # @type       Private
    # @usage      Initialize SDK modules for usage
    # @args       none
    # @returns    none
    #====================================
    def _initializeModules(this):
            if (SDKModules.SDKModules.Auth in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.auth = Auth(this); # Create Instance
            if (SDKModules.SDKModules.Analytics in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): analytics = Analytics(this); # Create Instance
            if (SDKModules.SDKModules.GameServices in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.game = GameServices(this); # Create Instance
            if (SDKModules.SDKModules.Payments in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.monetization =  Payments(this); # Create Instance
            if (SDKModules.SDKModules.Notifications in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.notifications =  Notifications(this); # Create Instance
            if (SDKModules.SDKModules.Marketing in this.settings.modules) or ( SDKModules.SDKModules.All in this.settings.modules): this.marketing =  Marketing(this); # Create Instance
            if (SDKModules.SDKModules.Ads in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.ads =  Ads(this); # Create Instance
            if (SDKModules.SDKModules.Backend in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.backend =  Backend(this); # Create Instance
            if (SDKModules.SDKModules.Reporting in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.reports =  Reporting(this); # Create Instance
            if (SDKModules.SDKModules.Perfomance in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.performance =  Performance(this); # Create Instance
            if (SDKModules.SDKModules.Backoffice in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.office =  Backoffice(this); # Create Instance
            if (SDKModules.SDKModules.Localization in this.settings.modules) or ( SDKModules.SDKModules.All in this.settings.modules): this.locale =  Localization(this); # Create Instance
            if (SDKModules.SDKModules.Users in this.settings.modules) or ( SDKModules.SDKModules.All in this.settings.modules): this.users =  Users(this); # Create Instance
            if (SDKModules.SDKModules.UI in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.ui =  UI(this); # Create Instance
            utils =  Utils(this); # Create Instance 

class Auth(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #====================================
    ## @class      
    ## @method     __init__   
    ## @type       Constructor
    ## @usage      Initialize Module
    ## @args       none
    ## @returns     none
    #====================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance

class Analytics(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #====================================
    # @class      
    # @method     __init__   
    # @type       Constructor
    # @usage      Initialize Module
    # @args       none
    # @returns     none
    #====================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance
 
class GameServices(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #====================================
    # @class      
    # @method     __init__   
    # @type       Constructor
    # @usage      Initialize Module
    # @args       none
    # @returns     none
    #====================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance         
    
class Payments(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #====================================
    # @class      
    # @method     __init__   
    # @type       Constructor
    # @usage      Initialize Module
    # @args       none
    # @returns     none
    #====================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance             
    
class Notifications(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #====================================
    # @class      
    # @method     __init__   
    # @type       Constructor
    # @usage      Initialize Module
    # @args       none
    # @returns     none
    #====================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance          
 
class Marketing(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #====================================
    # @class      
    # @method     __init__   
    # @type       Constructor
    # @usage      Initialize Module
    # @args       none
    # @returns     none
    #====================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance               
  
class Ads(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #====================================
    # @class      
    # @method     __init__   
    # @type       Constructor
    # @usage      Initialize Module
    # @args       none
    # @returns     none
    #====================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance                               
 
class Backend(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #====================================
    # @class      
    # @method     __init__   
    # @type       Constructor
    # @usage      Initialize Module
    # @args       none
    # @returns     none
    #====================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance       


class Reporting(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #====================================
    # @class      
    # @method     __init__   
    # @type       Constructor
    # @usage      Initialize Module
    # @args       none
    # @returns     none
    #====================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance    


class Performance(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #====================================
    # @class      
    # @method     __init__   
    # @type       Constructor
    # @usage      Initialize Module
    # @args       none
    # @returns     none
    #====================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance    


class Backoffice(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #====================================
    # @class      
    # @method     __init__   
    # @type       Constructor
    # @usage      Initialize Module
    # @args       none
    # @returns     none
    #====================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance    

class Localization(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #====================================
    # @class      
    # @method     __init__   
    # @type       Constructor
    # @usage      Initialize Module
    # @args       none
    # @returns     none
    #====================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance    

class Users(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #====================================
    # @class      
    # @method     __init__   
    # @type       Constructor
    # @usage      Initialize Module
    # @args       none
    # @returns     none
    #====================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance    

class UI(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #====================================
    # @class      
    # @method     __init__   
    # @type       Constructor
    # @usage      Initialize Module
    # @args       none
    # @returns     none
    #====================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance    

class Utils(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #====================================
    # @class      
    # @method     __init__   
    # @type       Constructor
    # @usage      Initialize Module
    # @args       none
    # @returns     none
    #====================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance    
