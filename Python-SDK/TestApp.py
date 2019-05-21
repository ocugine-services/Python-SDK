# -*- coding: utf-8 -*-
import OcugineSDK                       # import SDK
import Models.SDKSettings               # import Models


if __name__ == '__main__':
    test = Models.SDKSettings.SDKSettings() # test object
    test.modules = [Models.SDKModules.SDKModules.Localization, Models.SDKModules.SDKModules.Analytics]
    print(test.modules)
    print( lambda x: 'a' if(3<2) else 'b' ) # condition ? consequent : alternative