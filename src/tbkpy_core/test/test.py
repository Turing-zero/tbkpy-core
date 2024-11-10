import time
import tbkpy._core as tbkpy

tbkpy.init("test_node")
data = tbkpy.Data()
print("data: ", data)
ep = tbkpy.EPInfo()
print("ep: ", ep)
print("ep.ns: ", ep.ns)
print("ep.name: ", ep.name)
print("ep.msg_name: ", ep.msg_name)
print("ep.msg_type: ", ep.msg_type)
print("ep.msg_type_url: ", ep.msg_type_url)