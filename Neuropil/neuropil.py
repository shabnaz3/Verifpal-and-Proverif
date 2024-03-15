#message delivery
import string
from base64 import encode
from neuropil import NeuropilNode, NeuropilCluster, neuropil, np_token, np_message
import sys
port_index=1
#global port_index
log_file_prefix = "logs/smoke_test_msg_delivery" #
np_1 = NeuropilNode(4002 + port_index,log_file=f"{log_file_prefix}_sender.log") #Neuropil node as sender log
np_2 = NeuropilNode(4003 + port_index, log_file=f"{log_file_prefix}_receiver.log") #neuropilNode as reciverlog

subject = b"NP.TEST.msg_delivery" # messenge protocol
mxp1 = np_1.get_mx_properties(subject) # make propertis with subj and node sending to reciver
mxp1.ackmode = neuropil.NP_MX_ACK_DESTINATION # get acknowlegement from  neuropil destination so mxp1 = np_1
mxp1.apply()
mxp2 = np_2.get_mx_properties(subject) #another propertise  sending to reciver mxp2=np_2
mxp2.ackmode = neuropil.NP_MX_ACK_DESTINATION
mxp2.apply()

def authz_cb(node:NeuropilNode, token: np_token): # for data authorization very important
    print("authorizing")
    return True

np_1.set_authorize_cb(authz_cb)
np_2.set_authorize_cb(authz_cb)


np1_addr = np_1.get_address() #the formate with port index,protocol ,message identity 
np2_addr = np_2.get_address()

#np_2.join(np1_addr)

#print(np1_addr,"np1_addr")
#print(np2_addr,"np2_addr")
#print(np_1,"np_1")
#print(np_2,"np_2")
#print(mxp1,"mxp1")
#print(mxp2,"mxp2")

d = np_2.join(np1_addr)

np_1.run(1)
np_2.run(1)


d2=str(d).encode()


def msg_received( node:NeuropilNode, message:np_message): 
    print(message.raw())
    return True

np_2.set_receive_cb(subject, msg_received)

data=("rain")


if np_1.send(subject, d2) != neuropil.np_ok:
     print("ERROR sending Data")
else :
  print("s=", np_1.send(subject, d2))

while np_1.run(0.2) == neuropil.np_ok:
    np_1.send(subject, d2)
    np_2.run(0.2)
