#!/usr/bin/env python3
"""FastApi to return a JSON for telex integration"""

import re
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/get_nginx_5xx")
def nginx_status():
    """ The function for the integration endpoint"""

    return JSONResponse(
        status_code=200,
        content={
            "data": {
                "date": {
                    "created_at": "2025-02-19",
                    "updated_at": "2025-02-19"
                },
                "descriptions": {
                    "app_name": "ViewOnce",
                    "app_description": "Add view once option",
                    "app_logo": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQ4AAACUCAMAAABV5TcGAAAAY1BMVEX39/cAAAD////7+/s2NjbS0tItLS3Kysrw8PC5ubnz8/NbW1spKSng4OCFhYVTU1MdHR3Y2Nifn59qamrp6el7e3tkZGQVFRU+Pj6NjY2zs7OqqqqTk5PBwcFwcHBFRUULCwvsocNqAAAFHklEQVR4nO2c25KyOhCFIRE5yVFARVDf/yk3aOJA0qDOX7WnEtd3NWW8MGs6ne50J44DAAAAAAAAAAAAAAAAAAAAAAAAfCd8gN0Z//rrX/OXjPPnUVX4YTsQ+kUV8W/VZJh1kPRds3Mn7JquTwLn2xThzEn8MnZJ4tJPHPY9inAWLGrxVCT4FkFY1Ka7NTHuyyZtI/bXv/R/gPGwPrwSY+RQh9x2QTjz6u07Yoxsa8/uFcOc8viuGCPH0rHYQFi1/0SMkX1lrR7Mv32qhuvefDv14Pz8uRgjZxujMu6cfqeG654c6/TgQfpbNVw3DSzTg1X179Vw3douh8qrf7CNu31UFtkHj7q3AtFlDl1kjR7DnpL/mxqum9uzvzB/VY34VLb9+VW0mtsSf/DkujjJrE3GRGYg6F7ocU2sMA8eLbrRjk1YEe1BaoX74D09u23JZjivzMPtLZCDV2RCnw+hxJxIRq27LL6Syc3Wgt2Wkf/0Y8tU5GLZnCNWpKTz7Yz3piyh5hX7uhrSw/T3lUNvzYnperALMaummPqMoj+XZdnIVSQ+7ik9LobLQRpHNnEbXldnm6mnOMoR0gMbbh6MyNzy5ClGcdF219tzkCo91EbLwauNPiXvOeGUGP0JRkpicGP05sJKPXU7y+lWGTHfwTxOUixi8FAabB6c6TNuAjFbfzFLiZ37F8ixzOBSA/P11SCXircSk8dJFFHLbGBjcCbH9GOOUyTCjGby4XYzMK1THuKlEu7B3FCMc62sshPx1zStu13CfuBMuxKVvbHnHrzQZlgLzxFOPouTlUBDIytMlYOFavZ2ENtKMHUcUiKP9hYK29DU1aJHDpmIzltlgh/I4Rq71TKt0FSLNGW+xx73+wspx/VCKHQyVA5eqenbTZz4BNocc0oOP4gCPY67GBqY8kLdLTf9Qw69WLsl5HisIc3CYkN9qR5pyVS2UadIyiECFHV3unpmrhbWq9Yfi4ZaTY0VObiq3WBifz2zX8F6tSFuL2b4iRxMDeV2psoRqgdalyVPSsrBaTlyQwMPXQ6xz1bvyRFAjm+U40sXy5Ir/WhnsceVahutlEOvGazIYc1GuxiG6bWXZTm0E1VTwzA9SL+Kk0H9ZIOS43GErCUtpgbpegq3E8cdzltyuOWQwrVawdvUFI5I8FMRlmo1A1ION99blOATxz+NcB7ee3KQmHv8ox0O7sTBl6OZxyjHWzc7zD0cJI6OT44wD9USPMapIqSOuUfHRGHhKPYWrV3/mtbvrRVzCwtU2akT5hGtN2XHVFvIiMFlJ6ooeZNFyUo/EnuSeY4T0YKYXJSkStZ7WbIOFq+OZo86FOlZTS5Zkw0NpchUGUvpy08yswmJMaMbGuh2l582uZbqaZBqsIIYNLvdhWyGcn8a5YI007JbuZj0mNY1vRmKbpXLJ42D1blujrMVJUfIDkzDW+XoRsrNtK2UJ35bluXTjEQDCNkOY3oj5UKb7SZkKoEMSh95fUi2SpluHFRaO7IrA00PYUe3rmJJR75ZYGwy+8NCi/6h8VQ9ZJfDLYuv5F0xG1r0Fy9waHcWWvp7P9hwgWPtes9lKkjw6mqpHdd7Vi9/5V0inkRyXhmHJZe/Xl4NvNbpwEpG9xDO4NxtDi6OzsG14jm4dD4HTxLMwYMVc/CcyRw8dqOAp5Dm4KGsOXhGbQ4e2VPAE4wKeKBzDp5vVcDjvip4+lkFD4Pr4Nl4AAAAAAAAAAAAAAAAAAAAAAAAYOA/OgxLJ5E5lwEAAAAASUVORK5CYII=",
                    "app_url": "http://toluairbnb.tech",
                    "background_color": "#fff"
                },
                "is_active": true,
                "integration_type": "modifier",
                "key_features": [
                    "Checkbox"
                ],
                "author": "TeeCoded",
                "settings": [
                    {
                        "label": "Set view once option",
                        "type": "checkbox",
                        "required": True,
                        "default": "false"
                    }
                ],
                "target_url": "http://toluairbnb.tech/get_nginx_5xx",
                "tick_url": "http://toluairbnb.tech/get_nginx_5xx"
            }
        }
    )
