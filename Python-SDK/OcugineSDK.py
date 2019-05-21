import Models.SDKModules as SDKModules
import Models.SDKSettings as SDKSettings

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
class Ocugine:

    PROTOCOL = "https:#";       # Requests Protocol
    SERVER = "cp.ocugine.pro";  # Server URL
    SSL = True;                 # SSL
    API_GATE = "/api/";         # API Gateway
    VERSION = "0.4.0a";         # Library Version
    BUILD = 401;                # Library Build

    # Settings Instances
    application : SDKSettings.AppSettings = SDKSettings.AppSettings();    # Application Settings
    settings : SDKSettings.SDKSettings = SDKSettings.SDKSettings();       # SDK Settings

    # Classes Instances
    auth : Auth;                                # Authentication Class
    analytics : Analytics;                      # Analytics Class
    game : GameServices;                        # Game Services
    monetization : Payments;                    # Monetization Services
    notifications : Notifications;              # Notifications Services
    marketing : Marketing;                      # Marketing Services
    ads : Ads;                                  # Ads Services
    backend : Backend;                          # Backend Services
    reports : Reporting;                        # Reporting Services
    perfomance : Performance;                   # Perfomance Services
    office : Backoffice;                        # Office Services
    locale : Localization;                      # Locale Services
    users : Users;                              # User Class
    ui : UI;                                    # UI Module
    utils : Utils;                              # Utils Module

    # Private Class Params
    STATE_OBJECT = "state";    # State Object

    # Public Class Params
    OAUTH_OBJECT = "oauth";     
    USERS_OBJECT = "users";      
    SETTINGS_OBJECT = "api_settings";
    LOCALE_OBJECT = "localization";
    CLOUD_OBJECT = "cloud";

    def Ocugine(app_settings : SDKSettings.AppSettings, sdk_settings : SDKSettings.SDKSettings = None):
        application = app_settings;

        if(sdk_settings != null):
            settings = sdk_settings;
        else:
            settings = SDKSettings.SDKSettings();
            settings.language = "EN";
            settings.auth_timeout = 30;

class Auth():

    # Private Class Params
    _sdk_instance : Ocugine;

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    @class      
    @method     __init__   
    @type       Constructor
    @usage      Initialize Module
    @args       none
    @return     none
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def __init__(self, instance : Ocugine):
        _sdk_instance = instance

class Analytics():

    # Private Class Params
    _sdk_instance : Ocugine;

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    @class      
    @method     __init__   
    @type       Constructor
    @usage      Initialize Module
    @args       none
    @return     none
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def __init__(self, instance : Ocugine):
        _sdk_instance = instance
 
class GameServices():

    # Private Class Params
    _sdk_instance : Ocugine;

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    @class      
    @method     __init__   
    @type       Constructor
    @usage      Initialize Module
    @args       none
    @return     none
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def __init__(self, instance : Ocugine):
        _sdk_instance = instance         
    
class Payments():

    # Private Class Params
    _sdk_instance : Ocugine;

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    @class      
    @method     __init__   
    @type       Constructor
    @usage      Initialize Module
    @args       none
    @return     none
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def __init__(self, instance : Ocugine):
        _sdk_instance = instance             
    
class Notifications():

    # Private Class Params
    _sdk_instance : Ocugine;

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    @class      
    @method     __init__   
    @type       Constructor
    @usage      Initialize Module
    @args       none
    @return     none
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def __init__(self, instance : Ocugine):
        _sdk_instance = instance          
 
class Marketing():

    # Private Class Params
    _sdk_instance : Ocugine;

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    @class      
    @method     __init__   
    @type       Constructor
    @usage      Initialize Module
    @args       none
    @return     none
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def __init__(self, instance : Ocugine):
        _sdk_instance = instance               
  
class Ads():

    # Private Class Params
    _sdk_instance : Ocugine;

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    @class      
    @method     __init__   
    @type       Constructor
    @usage      Initialize Module
    @args       none
    @return     none
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def __init__(self, instance : Ocugine):
        _sdk_instance = instance                               
 
class Backend():

    # Private Class Params
    _sdk_instance : Ocugine;

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    @class      
    @method     __init__   
    @type       Constructor
    @usage      Initialize Module
    @args       none
    @return     none
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def __init__(self, instance : Ocugine):
        _sdk_instance = instance       


class Reporting():

    # Private Class Params
    _sdk_instance : Ocugine;

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    @class      
    @method     __init__   
    @type       Constructor
    @usage      Initialize Module
    @args       none
    @return     none
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def __init__(self, instance : Ocugine):
        _sdk_instance = instance    


class Performance():

    # Private Class Params
    _sdk_instance : Ocugine;

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    @class      
    @method     __init__   
    @type       Constructor
    @usage      Initialize Module
    @args       none
    @return     none
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def __init__(self, instance : Ocugine):
        _sdk_instance = instance    


class Backoffice():

    # Private Class Params
    _sdk_instance : Ocugine;

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    @class      
    @method     __init__   
    @type       Constructor
    @usage      Initialize Module
    @args       none
    @return     none
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def __init__(self, instance : Ocugine):
        _sdk_instance = instance    

class Localization():

    # Private Class Params
    _sdk_instance : Ocugine;

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    @class      
    @method     __init__   
    @type       Constructor
    @usage      Initialize Module
    @args       none
    @return     none
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def __init__(self, instance : Ocugine):
        _sdk_instance = instance    

class Users():

    # Private Class Params
    _sdk_instance : Ocugine;

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    @class      
    @method     __init__   
    @type       Constructor
    @usage      Initialize Module
    @args       none
    @return     none
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def __init__(self, instance : Ocugine):
        _sdk_instance = instance    

class UI():

    # Private Class Params
    _sdk_instance : Ocugine;

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    @class      
    @method     __init__   
    @type       Constructor
    @usage      Initialize Module
    @args       none
    @return     none
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def __init__(self, instance : Ocugine):
        _sdk_instance = instance    

class Utils():

    # Private Class Params
    _sdk_instance : Ocugine;

    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    @class      
    @method     __init__   
    @type       Constructor
    @usage      Initialize Module
    @args       none
    @return     none
    """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
    def __init__(self, instance : Ocugine):
        _sdk_instance = instance    
