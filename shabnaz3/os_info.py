from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import BaseSettings

app = FastAPI()
import os_info
import platform
import socket
from datetime import date
import webbrowser
import httpx
import urllib

class Title(BaseModel):
    os:str
    version:str
    processor:str
    hostname:str
    ip:str
    today:str
    location:str
    city:str


@app.get("/os_info/", response_model=Title,response_model_exclude_unset=True)
async def read_item():
    #response = httpx.get('https://gps-coordinates.org/my-location.php')
    url='http://www.geoplugin.net/json.gp?ip=185.66.194.78'

    params = {'ip': '185.66.194.78', }
    r1 = httpx.get('http://www.geoplugin.net/json.gp', params=params)
    print(r1.text)
    response=httpx.get(url,params=params)
    #print(response.text)
    #location = (r1.url)
    return Title(os=f"{platform.system()}",
                 version=f"{platform.release()}",
                 processor=f"{platform.processor()}",
                 hostname=f"{socket.gethostname()}",
                 ip=f"{socket.gethostbyname(socket.gethostname())}",
                 today=f"{date.today()}",
                 #location="http://www.geoplugin.net/json.gp?ip=185.66.194.78",
                 location= r1.json()['geoplugin_request'],
                 city=r1.json()['geoplugin_city'])



                # location=response{webbrowser.open("https://gps-coordinates.org/what-city-am-i-in.php")})
                 #location={"https://gps-coordinates.org/what-city-am-i-in.php"})


# uname works only on linux
'''import platform

app= FastAPI()
os_info = ['machine', 'version', 'system', 'release']
@app.get("/os_info/")
def index():
    xxx = []
    for item in os_info:
        xxx.append([getattr(platform, item)()])
    return xxx'''
