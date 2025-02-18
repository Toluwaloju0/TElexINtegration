#!/usr/bin/env python3
"""FastApi to return a JSON for telex integration"""

import re
from datetime import datetime
from fastapi import FastApi
from fastapi.responses import JSONResponse

app = FastAPI

@app.get("/get_nginx_5xx")
def nginx_status():
    """ The function for the integration endpoint"""

    return JSONResponse(
        status_code=200,
        content={
            "settings": [
                    {
                        "label": "Add view once option",
                        "type": "checkbox",
                        "description": "to approve view once"
                        "default": False
                    }
                ],
                "target_url": "toluairbnb.tech"
            }
        }
    )
