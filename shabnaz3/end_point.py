from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List


class Title(BaseModel):
    value: str
    language: str


class EndpointArtifact(BaseModel):
    type: str
    id: str
    fileName: str
    byteSize: str
    checkSum: str


class Protocol(BaseModel):
    id: str


class EndpointHost(BaseModel):
    type: str
    id: str
    protocol: Protocol
    accessUrl: str


class ResourceEndpoint(BaseModel):
    type: str
    id: str
    path: str
    endpointArtifact: Optional[EndpointArtifact] = None
    endpointHost: EndpointHost


class StandardLicense(BaseModel):
    id: str


class Keyword(BaseModel):
    value: str
    language: str


class Description(BaseModel):
    value: str
    language: str


class Offer(BaseModel):
    type: str
    id: str
    version: str
    title: List[Title]
    description: List[Description]
    customLicense: str
    keyword: List[Keyword]
    resourceEndpoint: List[ResourceEndpoint]
    standardLicense: StandardLicense


class Catalog(BaseModel):
    type: str
    offer: List[Offer]
    id: str


class Selfdescription(BaseModel):
    type: str
    title: List[Title]
    context: str
    catalog: Catalog
    outboundModelVersion: str
    inboundModelVersion: List[str]
    curator: str
    maintainer: str
    id: str
#import fastapi
title = []
inboundModelVersion=[]
title.append(Title(value="jhgjhg", language="en"))
catalog=Catalog(type="ggg",offer=[],id="s1")
t= Selfdescription(title=title,type= "b",context="d",catalog=catalog,outboundModelVersion="de",
                   inboundModelVersion=inboundModelVersion,curator="",maintainer="s",id="j")

t.type="b"
t.context="d"
t.inboundModelVersion="r"
t.outboundModelVersion="de"
t.curator="g"
t.maintainer="s"
t.id="j"

 #{
  # "title":"title", "endp":"endpointArt","protocol":"protocol",
   # "endhost":"endpointhost","resource":"resource","stand":"standard",
    #"key":"keyword","description":"description","offer":"offer",
    #"catalog":"catalog","self":"selfdescription"
    #}'''


app = FastAPI()

@app.get('/test-body-params-in-post')
def test_endpoint1():
    #result={t.value,t.language}
   return t
     #result={"endp":"endpointArt","protocol":"protocol","endhost":"endpointhost", "resource":"resource","stand":"standard","key":"keyword",
             # "description":"description","offer":"offer","catalog":"catalog","self":"selfdescription"}
    #return()
