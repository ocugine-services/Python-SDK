# -*- coding: utf-8 -*-
from OcugineSDK.OcugineSDK import Ocugine                  # import SDK
from OcugineSDK.Models import SDKModules as SDKModules     # import Modules
from OcugineSDK import Models                              # import Object models
import webbrowser
# from OcugineSDK import Ads, Analytics
# webbrowser.open('http://google.co.kr', new=2)


if __name__ == '__main__':

    SDK = Ocugine( 
        Models.SDKSettings.AppSettings(1, 'c46361ae80c1679d637c2f23968a4dc5d5ea2a65'),
        Models.SDKSettings.SDKSettings('RU', [SDKModules.SDKModules.All], 10)        
    )
      
    if(False): # Тест Sendrequest
        url = SDK.PROTOCOL+SDK.SERVER+SDK.API_GATE+SDK.OAUTH_OBJECT+'/get_link'
        data = {"app_id": SDK.application.app_id, "app_key": SDK.application.app_key, "grants": "all"}  
        SDK.utils.SendRequest(url, data, lambda suc : print(suc), lambda err : print(err));

    if(False): # Тест GetLink
        arr = {}
        SDK.auth.GetLink( 'all', lambda suc : arr.update(suc), lambda err : print(err) );
        print(arr)

    if(False): # Тест GetToken
        SDK.auth.GetToken(lambda suc : print(suc), lambda err : print(err));

    if(True): # Тест Logout
        SDK.auth.GetToken(
           lambda suc: SDK.auth.Logout(lambda sucsess : print(sucsess), lambda error : print(error)),
           lambda err : print(err));

    if(True): # Тест GetAuthForm
        SDK.ui.GetAuthForm('all', lambda suc : print(suc), lambda err : print(err));

    if(False): # Тест Sendrequest
        SDK.utils.SendRequest(url, data, lambda suc : print(suc), lambda err : print(err));

    if(False): # Тест Sendrequest
        SDK.utils.SendRequest(url, data, lambda suc : print(suc), lambda err : print(err));

    if(False): # Тест Sendrequest
        SDK.utils.SendRequest(url, data, lambda suc : print(suc), lambda err : print(err));

    if(False): # Тест Sendrequest
        SDK.utils.SendRequest(url, data, lambda suc : print(suc), lambda err : print(err));

    if(False): # Тест Sendrequest
        SDK.utils.SendRequest(url, data, lambda suc : print(suc), lambda err : print(err));

    if(False): # Тест Sendrequest
        SDK.utils.SendRequest(url, data, lambda suc : print(suc), lambda err : print(err));

    