#!/usr/bin/env python3
"""FastApi to return a JSON for telex integration"""

import re
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/viewOnce")
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
                    "app_logo": "https://imgur.com/a/wOwIpco",
                    "app_url": "http://toluairbnb.tech",
                    "background_color": "#fff"
                },
                "is_active": True,
                "integration_category": "Monitoring & Logging",
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
