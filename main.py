#!/usr/bin/env python3
"""FastApi to return a JSON for telex integration"""

from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests
from typing import List, Dict

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
                        "default": False
                    }
                ],
                "target_url": "http://toluairbnb.tech/targetUrl",
                "tick_url": "http://toluairbnb.tech/get_nginx_5xx"
            }
        }
    )


@app.post("/target_url")
async def targetUrl(message: str, settings: List[Dict] = [], channel_id: str):
    """The target url for the telex integration"""

    if len(settings) == 0:
        return JSONResponse(
            status_code=400,
            content={
                "error": "No setting was found for your message"""
            }
        )
    for setting in settings:
        if setting.get('default') is True:
            return JSONResponse(
                status_code=200,
                content={
                    "event_name": "message_formatted",
                    "message": "This is a view once message, Contact the \
sender for further clarifications",
                    "status": "success",
                    "username": "VeiwOnce-bot"
                }
            )
    return JSONResponse(
        status_code=200,
        content={
            "event_name": "message_ not_formatted",
            "message": "message",
            "status": "success",
            "username": "VeiwOnce-bot"
        }
    )
