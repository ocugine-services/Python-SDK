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
#  Ocugine SDKs Authentification Model
#================================================
class AuthentificationModel(object):
     Uid = 0;              # Authentication UID
     Is_auth = False;      # Authentication Status
     Login = "";           # User Login
     Token = "";           # User Token
     From = "";            # Authentication Method
     Action_time = 0;      # Last Action Time (Unix)
     Profile_uid = 0;      # Profile (Account) UID  

#================================================
# Ocugine Application Profile Model
#================================================
class ProfileModel(object):
    uid = 0;              # Profile (Account) UID
    first_name = "";      # First Name
    last_name = "";       # Last Name
    avatar = "";          # Avatar (Photo) URL
    email = "";           # User Email
    profile_data = None;  # Profile Data
    profile_type = 0;     # Profile Type

class profileData(object):
    field = None;

#================================================
# Ocugine Application Viewer Model
#================================================
class ViewerModel(object):
    uid = 0;              # Viewer UID
    ip = "";              # Viewer IP
    profile_uid = 0;      # Profile (Account) UID
    user_agent = "";      # User Agent
    hash = "";            # User Hash
    location = "";        # User Location
    device = "";          # User Device
    time = 0;             # Last Action Time (Unix)


