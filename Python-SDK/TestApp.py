# -*- coding: utf-8 -*-
from OcugineSDK import Ocugine                  # import SDK
from Models import SDKModules as SDKModules     # import Modules
import Models                                   # import Object models
import webbrowser
#from OcugineSDK import Ads, Analytics


if __name__ == '__main__':
    #web = webbrowser.open('http://google.co.kr', new=2)

    #print( lambda x: 'a' if(3<2) else 'b' ) # condition ? consequent : alternative

    SDK = Ocugine(
        Models.SDKSettings.AppSettings(1, 'c46361ae80c1679d637c2f23968a4dc5d5ea2a65'),
        Models.SDKSettings.SDKSettings("RU", [SDKModules.SDKModules.All], 10)        
    )

    url = SDK.PROTOCOL+SDK.SERVER+SDK.API_GATE+SDK.OAUTH_OBJECT+'/get_link'
    data = {"app_id": SDK.application.app_id, "app_key": SDK.application.app_key, "grants": "all"}  

    SDK.utils.SendRequest(url, data, lambda suc : print(suc), lambda err : print(err));

