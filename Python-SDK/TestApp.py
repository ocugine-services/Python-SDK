# -*- coding: utf-8 -*-
#================================================
#  Ocugine Libraries
#================================================
from OcugineSDK.OcugineSDK import Ocugine                  # import SDK
from OcugineSDK.Models import SDKModules as SDKModules     # import Modules
from OcugineSDK import Models                              # import Object models
# from OcugineSDK import Ads, Analytics


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

    if(False): # Тест Logout
        SDK.auth.GetToken(
           lambda suc: SDK.auth.Logout(lambda sucsess : print(sucsess), lambda error : print(error)),
           lambda err : print(err));

    if(False): # Тест GetLang GetLocale
        SDK.locale.GetLang('ru', lambda suc : print(suc), lambda err : print(err));
        SDK.locale.GetLocale('ru', 'test-node', lambda suc : print(suc), lambda err : print(err));

    if(True): # Тест GetPolicyList GetPolicyInfo
        SDK.users.GetPolicyList(lambda suc : print(suc), lambda err : print(err));
        SDK.users.GetPolicyInfo(2, lambda suc : print(suc), lambda err : print(err));

    if(False): # Тест 
        SDK.utils.SendRequest(url, data, lambda suc : print(suc), lambda err : print(err));

    if(False): # Тест 
        SDK.utils.SendRequest(url, data, lambda suc : print(suc), lambda err : print(err));

    if(False): # Тест 
        SDK.utils.SendRequest(url, data, lambda suc : print(suc), lambda err : print(err));

    if(False): # Тест 
        SDK.utils.SendRequest(url, data, lambda suc : print(suc), lambda err : print(err));

    if(False): # Тест 
        SDK.utils.SendRequest(url, data, lambda suc : print(suc), lambda err : print(err));

    