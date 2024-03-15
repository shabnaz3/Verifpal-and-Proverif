#import model
'''from model import Protocol
#print(Selfdescription["id"])

protocol=Protocol(id="s17")
print(protocol)'''
import model

import dic_config
from pprint import pprint
from model import Selfdescription
#test=Title(value="a",language="b")
#title=test

t=model.Title(value="c",language="d")
#p=[]
p1=model.Protocol(id="str")
#p2=p.append(p1)

des=model.Description(value="d1",language="d2")
key=model.Keyword(value="v",language="l")
endp=model.EndpointHost(type="ay",id="az",protocol=p1,accessUrl="ad")
res=model.ResourceEndpoint(type="str",id="s12",path="s32",endpointArtifact=None,endpointHost=endp)
stand=model.StandardLicense(id="ar")


ofr=model.Offer(type="o",id="o2",version="o3",title=[t],description=[des],customLicense="str",
                keyword=[key],resourceEndpoint=[res],standardLicense=stand)

t2=model.Catalog(type="a",id="b",title=t,offer=[ofr],protocol=[p1])


#pprint(t2)

t3=dic_config.Selfdescription(type="s",title=[t],context="s1",catalog=t2,outboundModelVersion="de",
                          inboundModelVersion=["a","b","d"],curator="rr",maintainer="dd",id="fe",)


print(t3)
