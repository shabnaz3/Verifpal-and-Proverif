import string
from base64 import encode
from neuropil import NeuropilNode, NeuropilCluster, neuropil, np_token, np_message

port_index=1
log_file_prefix = "logs/smoke_test_msg_delivery" 
np_1 = NeuropilNode(4002 + port_index,log_file=f"{log_file_prefix}_sender.log") #Neuropil node as sender log
np_2 = NeuropilNode(4003 + port_index, log_file=f"{log_file_prefix}_receiver1.log") #neuropilNode as reciverlog
np_3 = NeuropilNode(4004 + port_index, log_file=f"{log_file_prefix}_receiver2.log") #neuropilNode as reciverlog

subject1 = b"NP.TEST.msg_delivery" # messenge protocol

mxp1 = np_1.get_mx_properties(subject1)
mxp1.role = neuropil.NP_MX_PROVIDER
mxp1.ackmode = neuropil.NP_MX_ACK_DESTINATION # get acknowlegement from  neuropil destination so mxp1 = np_1
mxp1.apply()

mxp2 = np_2.get_mx_properties(subject1)
mxp2.role = neuropil.NP_MX_CONSUMER
mxp2.ackmode = neuropil.NP_MX_ACK_DESTINATION
mxp2.apply()


subject2=b"NP.TEST.msg_delivery"
mxp0 =  np_1.get_mx_properties(subject2)
mxp0.role = neuropil.NP_MX_PROVIDER
mxp0.ackmode = neuropil.NP_MX_ACK_DESTINATION
mxp0.apply()

mxp3 = np_3.get_mx_properties(subject2)
mxp3.role = neuropil.NP_MX_CONSUMER
mxp3.ackmode = neuropil.NP_MX_ACK_DESTINATION

mxp3.apply()


def authz_cb(node:NeuropilNode, token:np_token): #create_authorization_method_Suppose_You_enter_the_resurant_you_are_authorized_check_kora_k_bujhay
    print("authorizing")
    return True

np_1.set_authorize_cb(authz_cb)
np_2.set_authorize_cb(authz_cb)
np_3.set_authorize_cb(authz_cb)


np1_addr = np_1.get_address()  # resurant a number  diye identify kore
np2_addr = np_2.get_address()
np3_addr = np_3.get_address()                         
                              
                              



d1= "rain"
d4="sun"
d = np_2.join(np1_addr)
d2=str(d)
d3=(d1+(d2)).encode()
d5=np_3.join(np1_addr)
d6=(str(d5)+d4).encode()
#this_for_like_you_are_enter_the_resturent_you_cannot_eat_without_this
np_1.run(1) 
np_2.run(1)
np_3.run(1)

def msg_received( node:NeuropilNode, message:np_message): #create recive msg_function
    print(message.raw())
    return True

np_2.set_receive_cb(subject1, msg_received) # recive_function np_2  er upor set korar jonno karon o message recive korbe 
np_3.set_receive_cb(subject2, msg_received)


if np_1.send(subject1, d3) != neuropil.np_ok:
     print("ERROR sending Data")
else :
  print( np_1.send(subject1, d3))

if np_1.send(subject2, d6) != neuropil.np_ok:
     print("ERROR sending Data")
else :
  print("s=", np_1.send(subject2, d6))     
 

while np_1.run(0.2) == neuropil.np_ok:
  np_1.send(subject1, d3)
  np_1.send(subject2, d6)
  np_2.run(0.2)
  np_3.run(0.2)
