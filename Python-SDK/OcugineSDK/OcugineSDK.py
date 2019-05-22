#================================================
#  Ocugine Libraries
#================================================
import OcugineSDK.Models.SDKModules as SDKModules
import OcugineSDK.Models.SDKSettings as SDKSettings
import OcugineSDK.Models.AuthentificationModel as AuthentificationModel
#================================================
#  Default Libraries
#================================================
import time
import requests
import traceback
import webbrowser

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
class Ocugine(object):

    PROTOCOL = "https://";      # Requests Protocol
    SERVER = "cp.ocugine.pro";  # Server URL
    SSL = True;                 # SSL
    API_GATE = "/api/";         # API Gateway
    VERSION = "0.4.0a";         # Library Version
    BUILD = 401;                # Library Build

    # Settings Instances
    application = None;         # Application Settings
    settings = None;            # SDK Settings

    # Classes Instances
    ads = None;                 # Ads Services
    auth = None;                # Authentication Class
    analytics  = None;          # Analytics Class
    backend = None;             # Backend Services
    game = None;                # Game Services
    locale = None;              # Locale Services
    marketing = None;           # Marketing Services  
    monetization = None;        # Monetization Services
    notifications  = None;      # Notifications Services
    office  = None;             # Office Services
    perfomance  = None;         # Perfomance Services
    reports  = None;            # Reporting Services        
    users  = None;              # User Class
    ui = None;                  # UI Module
    utils  = None;              # Utils Module

    # Private Class Params
    STATE_OBJECT = "state";    # State Object

    # Public Class Params
    OAUTH_OBJECT = "oauth";     
    USERS_OBJECT = "users";      
    SETTINGS_OBJECT = "api_settings";
    LOCALE_OBJECT = "localization";
    CLOUD_OBJECT = "cloud";

    #=================================================
    # @class        General
    # @method       __init__ 
    # @usage        Constructor
    # @args         SDKSettings.AppSettings() 
    #               SDKSettings.SDKSettings() 
    #=================================================
    def __init__(self, app_settings : SDKSettings.AppSettings, sdk_settings : SDKSettings.SDKSettings): # Constructor
        self.application = app_settings;
        self.settings = sdk_settings;
        Ocugine._initializeModules(self);
    
    #=================================================
    # @class        General
    # @method       _initializeModules()  
    # @usage        Initialize modules
    # @args         (Ocugine) this - SDK instance
    #=================================================
    def _initializeModules(this):
            if (SDKModules.SDKModules.Auth in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.auth = Auth(this); # Create Instance
            if (SDKModules.SDKModules.Analytics in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): analytics = Analytics(this); # Create Instance
            if (SDKModules.SDKModules.GameServices in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.game = GameServices(this); # Create Instance
            if (SDKModules.SDKModules.Payments in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.monetization = Payments(this); # Create Instance
            if (SDKModules.SDKModules.Notifications in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.notifications = Notifications(this); # Create Instance
            if (SDKModules.SDKModules.Marketing in this.settings.modules) or ( SDKModules.SDKModules.All in this.settings.modules): this.marketing = Marketing(this); # Create Instance
            if (SDKModules.SDKModules.Ads in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.ads = Ads(this); # Create Instance
            if (SDKModules.SDKModules.Backend in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.backend = Backend(this); # Create Instance
            if (SDKModules.SDKModules.Reporting in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.reports = Reporting(this); # Create Instance
            if (SDKModules.SDKModules.Perfomance in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.performance = Performance(this); # Create Instance
            if (SDKModules.SDKModules.Backoffice in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.office = Backoffice(this); # Create Instance
            if (SDKModules.SDKModules.Localization in this.settings.modules) or ( SDKModules.SDKModules.All in this.settings.modules): this.locale = Localization(this); # Create Instance
            if (SDKModules.SDKModules.Users in this.settings.modules) or ( SDKModules.SDKModules.All in this.settings.modules): this.users = Users(this); # Create Instance
            if (SDKModules.SDKModules.UI in this.settings.modules) or (SDKModules.SDKModules.All in this.settings.modules): this.ui = UI(this); # Create Instance
            this.utils =  Utils(this); # Create Instance 

#================================================
#  Ocugine Auth Module
#================================================
class Auth(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    # Authentification Objects
    credentials = AuthentificationModel.AuthentificationModel();
    profile = AuthentificationModel.ProfileModel();
    viewer = AuthentificationModel.ViewerModel();

    #================================================
    # @class        Auth
    # @method       __init__  
    # @usage        Constructor
    # @args         (Ocugine) instance - SDK instance
    #================================================  
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance     
        
    #=================================================
    # @class        Auth
    # @method       GetLink  
    # @usage        Gets authentification link
    # @args         (dictionary) grants - permissions
    #               (def) complete - succsess callback 
    #               (def) error - error callback
    #=================================================
    def GetLink(self, grants, complete, error):
        url = self._sdk_instance.PROTOCOL+self._sdk_instance.SERVER+self._sdk_instance.API_GATE+self._sdk_instance.OAUTH_OBJECT+'/get_link';
        data = {
            "app_id": self._sdk_instance.application.app_id, 
            "app_key": self._sdk_instance.application.app_key, 
            "grants": grants, 
            "lang": self._sdk_instance.settings.language};  
        response = {};
        self._sdk_instance.utils.SendRequest(url, data, lambda suc : response.update(suc), lambda err : error(err));
        if(response):
            complete(response);
            return True;
        else:
            return False;

    #=================================================
    # @class        Auth
    # @method       GetToken  
    # @usage        Gets Token
    # @args         (def) complete - succsess callback 
    #               (def) error - error callback
    #=================================================
    def GetToken(self, complete, error):
        url = self._sdk_instance.PROTOCOL+self._sdk_instance.SERVER+self._sdk_instance.API_GATE+self._sdk_instance.OAUTH_OBJECT+'/get_token';
        data = {
            "app_id": self._sdk_instance.application.app_id, 
            "app_key": self._sdk_instance.application.app_key, 
            "lang": self._sdk_instance.settings.language};  
        response = {};
        self._sdk_instance.utils.SendRequest(url, data, lambda suc : response.update(suc), lambda err : error(err));
        if(response):
            self.credentials.Token = response['access_token'];
            self.credentials.Is_auth = True;
            complete(response);
            return True;
        else:
            return False;
    
    #=================================================
    # @class        Auth
    # @method       Logout  
    # @usage        Logout account
    # @args         (def) complete - succsess callback 
    #               (def) error - error callback
    #=================================================
    def Logout(self, complete, error):
        if(self.credentials.Token == "" or self.credentials.Is_auth == False):
            self.credentials.Token = ""; self.credentials.Is_auth = False;
            if(self._sdk_instance.settings.language == "RU"): error("Ошибка деавторизации, приложение не авторизовано");
            else: error("Logout error, application not authorized");
            return False
        else:
            url = self._sdk_instance.PROTOCOL+self._sdk_instance.SERVER+self._sdk_instance.API_GATE+self._sdk_instance.OAUTH_OBJECT+'/logout';
            data = {
                "access_token": self.credentials.Token };
            response = {};
            self._sdk_instance.utils.SendRequest(url, data, lambda suc : response.update(suc), lambda err : error(err));
            if(response):
                self.credentials.Token = ""; 
                self.credentials.Is_auth = False;
                complete("Logout succsess");
                return True;
            else:
                return False;

#================================================
#  Ocugine Advertisments Module
#================================================       
class Ads(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #================================================
    # @class        Ads
    # @method       __init__  
    # @usage        Constructor
    # @args         (Ocugine) instance - SDK instance
    #================================================   
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance  

#================================================
#  Ocugine Analytics Module
#================================================
class Analytics(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #================================================
    # @class        Analytics
    # @method       __init__  
    # @usage        Constructor
    # @args         (Ocugine) instance - SDK instance
    #================================================    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance

#================================================
#  Ocugine Backend Module
#================================================ 
class Backend(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #================================================
    # @class        Backend
    # @method       __init__  
    # @usage        Constructor
    # @args         (Ocugine) instance - SDK instance
    #================================================   
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance       
 
#================================================
#  Ocugine Backoffice Module
#================================================
class Backoffice(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #================================================
    # @class        Backoffice
    # @method       __init__  
    # @usage        Constructor
    # @args         (Ocugine) instance - SDK instance
    #================================================    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance    

#================================================
#  Ocugine Game Services Module
#================================================
class GameServices(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #================================================
    # @class        GameServices
    # @method       __init__  
    # @usage        Constructor
    # @args         (Ocugine) instance - SDK instance
    #================================================   
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance         
    
#================================================
#  Ocugine Localization Module
#================================================
class Localization(object):

    # Private Class Params
    _sdk_instance : Ocugine;
    _LangInfoCache = {};
    _LocInfoCache = {};

    #================================================
    # @class        Localization
    # @method       __init__  
    # @usage        Constructor
    # @args         (Ocugine) instance - SDK instance
    #================================================    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance    

    #=================================================
    # @class        Localization
    # @method       GetLang 
    # @usage        Gets language info
    # @args         (string) lang_code - Language code 
    #               (def) complete - succsess callback 
    #               (def) error - error callback
    #=================================================
    def GetLang(self, lang_code, complete, error):
        if(self._LangInfoCache.get(lang_code, None) != None):
            complete(self._LangInfoCache[lang_code]);
            return True;
        else:
            url = self._sdk_instance.PROTOCOL+self._sdk_instance.SERVER+self._sdk_instance.API_GATE+self._sdk_instance.LOCALE_OBJECT+'/get_lang';
            data = {
                "app_id": self._sdk_instance.application.app_id, 
                "app_key": self._sdk_instance.application.app_key, 
                "code": lang_code};  
            response = {};
            self._sdk_instance.utils.SendRequest(url, data, lambda suc : response.update(suc), lambda err : error(err));
            if(response):
                self._LangInfoCache[lang_code] = response;
                complete(response);
                return True;
            else:
                return False;

    #=================================================
    # @class        Localization
    # @method       GetLocale  
    # @usage        Gets locale info
    # @args         (string) lang_code - Language code 
    #               (def) complete - succsess callback 
    #               (def) error - error callback
    #=================================================
    def GetLocale(self, lang_code, locale_code, complete, error):
        if(self._LocInfoCache.get(lang_code, None) != None and self._LocInfoCache.get(lang_code, None).get(locale_code, None) != None):
            complete(self._LocInfoCache[lang_code][locale_code]);
            return True;
        else:
            url = self._sdk_instance.PROTOCOL+self._sdk_instance.SERVER+self._sdk_instance.API_GATE+self._sdk_instance.LOCALE_OBJECT+'/get_locale';
            data = {
                "app_id": self._sdk_instance.application.app_id, 
                "app_key": self._sdk_instance.application.app_key, 
                "lang": lang_code,
                "code": locale_code};  
            response = {};
            self._sdk_instance.utils.SendRequest(url, data, lambda suc : response.update(suc), lambda err : error(err));
            if(response):
                if(self._LocInfoCache.get(lang_code, None) == None):
                    self._LocInfoCache[lang_code] = {};
                self._LocInfoCache[lang_code][locale_code] = response;
                complete(response);
                return True;
            else:
                return False;  

#================================================
#  Ocugine Marketing Module
#================================================
class Marketing(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #================================================
    # @class        Marketing
    # @method       __init__  
    # @usage        Constructor
    # @args         (Ocugine) instance - SDK instance
    #================================================   
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance   

#================================================
#  Ocugine Notifications Module
#================================================        
class Notifications(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #================================================
    # @class        Notifications
    # @method       __init__  
    # @usage        Constructor
    # @args         (Ocugine) instance - SDK instance
    #================================================   
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance          
            
#================================================
#  Ocugine Payments Module
#================================================
class Payments(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #================================================
    # @class        Payments
    # @method       __init__  
    # @usage        Constructor
    # @args         (Ocugine) instance - SDK instance
    #================================================   
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance             

#================================================
#  Ocugine Performance Module
#================================================
class Performance(object):

    # Private Class Params
    _sdk_instance : Ocugine;
    #================================================
    # @class        Performance
    # @method       __init__  
    # @usage        Constructor
    # @args         (Ocugine) instance - SDK instance
    #================================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance    

#================================================
#  Ocugine Reporting Module
#================================================
class Reporting(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #================================================
    # @class        Reporting
    # @method       __init__  
    # @usage        Constructor
    # @args         (Ocugine) instance - SDK instance
    #================================================   
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance    

#================================================
#  Ocugine Users Module
#================================================
class Users(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #================================================
    # @class        Users
    # @method       __init__  
    # @usage        Constructor
    # @args         (Ocugine) instance - SDK instance
    #================================================ 
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance    

    #=================================================
    # @class        Users
    # @method       GetPolicyList 
    # @usage        Gets policy info
    # @args         (def) complete - succsess callback 
    #               (def) error - error callback
    #=================================================
    def GetPolicyList(self, complete, error):  
        url = self._sdk_instance.PROTOCOL+self._sdk_instance.SERVER+self._sdk_instance.API_GATE+self._sdk_instance.USERS_OBJECT+'/get_policy_list';
        data = {
            "app_id": self._sdk_instance.application.app_id, 
            "app_key": self._sdk_instance.application.app_key, 
            "lang": self._sdk_instance.settings.language};  
        response = {};
        self._sdk_instance.utils.SendRequest(url, data, lambda suc : response.update(suc), lambda err : error(err));
        if(response):
            complete(response);
            return True;
        else:
            return False;

    #=================================================
    # @class        Users
    # @method       GetPolicyInfo
    # @usage        Gets policy info
    # @args         (string) pid - policy id
    #               (def) complete - succsess callback 
    #               (def) error - error callback
    #=================================================
    def GetPolicyInfo(self, pid, complete, error):  
        url = self._sdk_instance.PROTOCOL+self._sdk_instance.SERVER+self._sdk_instance.API_GATE+self._sdk_instance.USERS_OBJECT+'/get_policy_info';
        data = {
            "app_id": self._sdk_instance.application.app_id, 
            "app_key": self._sdk_instance.application.app_key, 
            "pid": pid, 
            "lang": self._sdk_instance.settings.language};  
        response = {};
        self._sdk_instance.utils.SendRequest(url, data, lambda suc : response.update(suc), lambda err : error(err));
        if(response):
            complete(response);
            return True;
        else:
            return False;

#================================================
#  Ocugine UI Module
#================================================
class UI(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #================================================
    # @class        UI
    # @method       __init__  
    # @usage        Constructor
    # @args         (Ocugine) instance - SDK instance
    #================================================   
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance    

    #================================================
    # @class        UI
    # @method       GetAuthForm  
    # @usage        Get token by Oauth protocol
    # @args         (dictionary) grants - permissions
    #               (def) complete - succsess callback 
    #               (def) error - error callback
    #================================================
    def GetAuthForm(self, grants, complete, error):
        if(self._sdk_instance.auth == None):
            if(self._sdk_instance.settings.language == "RU"): 
                error("Для использования метода GetAuthForm необходимо подключить модуль Auth");
            else: 
                error("Method GetAuthForm requires Auth module");
            return False
        else:
            if(not self._sdk_instance.auth.GetLink(grants, lambda s:webbrowser.open(s['auth_url'], new=2), lambda e: error(e))):
                return False;
            else:
                timeout = 0; GotToken = False; lasterror = {};
                while (not GotToken and timeout != self._sdk_instance.settings.auth_timeout):
                    GotToken = self._sdk_instance.auth.GetToken(lambda s: complete(s), lambda e: lasterror.update({'error':e}));
                    timeout+=1; time.sleep(1);
                if(GotToken):
                    return True;
                else:
                    if(self._sdk_instance.settings.language == "RU"): 
                        error("Время на аутентификацию вышло\n" + lasterror['error']);
                    else: 
                        error("Authefication timed out\n" + lasterror['error']);
                    return False;

#================================================
#  Ocugine Utils Module
#================================================
class Utils(object):

    # Private Class Params
    _sdk_instance : Ocugine;

    #================================================
    # @class        Utils
    # @method       __init__  
    # @usage        Constructor
    # @args         (Ocugine) instance - SDK instance
    #================================================
    
    def __init__(self, instance : Ocugine):
        self._sdk_instance = instance    

    #=================================================
    # @class        Utils
    # @method       SendRequest  
    # @usage        Send POST request
    # @args         (string) url - request url
    #               (list) data - json request body
    #               (def) complete - succsess callback 
    #               (def) error - error callback
    #=================================================
    def SendRequest(self, url, data, complete, error): 
        try:                                            # Try to send request
            response = requests.post(url, data=data);   # Send request
            if(response.json()['complete']):            # All Right, Server returns Complete Flag
                complete(response.json()['data']);      # Show Complete text.replace('\\', '')
                return True;                            # Return result
            else:                                       # Server Returns Error
                error(response.json()['message'])       # Show Error         
                return False;                           # Return result
        except Exception as ex:                         # Failed to send request
            error(traceback.format_exc())               # Show Error         
            return False;                               # Return result

    #=================================================
    # @class        Utils
    # @method       GetSettings 
    # @usage        Get settings info
    # @args         (def) complete - succsess callback 
    #               (def) error - error callback
    #=================================================
    def GetSettings(self, complete, error):  
        url = self._sdk_instance.PROTOCOL+self._sdk_instance.SERVER+self._sdk_instance.API_GATE+self._sdk_instance.SETTINGS_OBJECT+'/get_settings';
        data = {
            "app_id": self._sdk_instance.application.app_id, 
            "app_key": self._sdk_instance.application.app_key, 
            "lang": self._sdk_instance.settings.language};  
        response = {};
        self._sdk_instance.utils.SendRequest(url, data, lambda suc : response.update(suc), lambda err : error(err));
        if(response):
            complete(response);
            return True;
        else:
            return False;