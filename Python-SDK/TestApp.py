# -*- coding: utf-8 -*-
from OcugineSDK import Ocugine                  # import SDK
from Models import SDKModules as SDKModules     # import Modules
import Models                                   # import Object models
#from OcugineSDK import Ads, Analytics


if __name__ == '__main__':
    print( lambda x: 'a' if(3<2) else 'b' ) # condition ? consequent : alternative

    SDK = Ocugine(
        Models.SDKSettings.AppSettings(1, 'c46361ae80c1679d637c2f23968a4dc5d5ea2a65'),
        Models.SDKSettings.SDKSettings("RU", [SDKModules.SDKModules.All], 10)        
    )

    print(SDK.application.app_id)
    print(SDK.ui)

    