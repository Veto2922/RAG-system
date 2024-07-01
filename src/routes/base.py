from fastapi import FastAPI , APIRouter , Depends
import os
from helpers.config import get_settings , Settings



base_router = APIRouter(
    prefix = '/api/v1',
    tags=['api_v1']
)

'''
The async keyword in Python signals that the function (welcome() in this case) is asynchronous, allowing it to perform non-blocking operations and integrate seamlessly with FastAPI's asynchronous framework for handling web requests efficiently
In web applications, using asynchronous functions can improve performance by allowing other tasks to execute while waiting for I/O-bound operations to complete..
'''

@base_router.get("/")
async def welcome(app_settings : Settings = Depends(get_settings)):
   
    
    app_name = app_settings.APP_NAME
    app_v = app_settings.APP_VERSION
    
    return {
        "app_name" :app_name,
        'app_v' : app_v 
    }