# -*-coding:utf-8 -*-
"""
:PROJECT_NAME: tee
:File: gui.py
:Time: 2024/4/29 下午3:16
:Author: 张隆鑫


病毒清理程序
"""
from __future__ import unicode_literals, print_function, division

import os
import re
import shutil
import maya.cmds as cmds
import base64;


def kill_virus():
    user_setup_py = cmds.internalVar(userAppDir=True) + '/scripts/userSetup.mel'
    if os.path.exists(user_setup_py):
        with open(user_setup_py, 'rb') as f:
            data = f.read()
        virus_code = re.findall(
            r'import base64;\s*pyCode\s*=\s*base64\.urlsafe_b64decode\([\'\"](.*?)[\"\']\)',
            data,
        )
        if len(virus_code) < 1:
            cmds.warning('未发现病毒')
            return
        virus_code = virus_code[0]
        virus_code = base64.urlsafe_b64decode(virus_code)
        # maya_path_=os.getenv("APPDATA")+'\syssst'
        virus_path = re.findall(
            r'maya_path_\s*=\s*os.getenv\([\'\"]APPDATA[\'\"]\)\+[\'\"]\\([a-zA-Z0-9]+)[\'\"]',
            virus_code,
        )
        if len(virus_path) < 1:
            os.remove(user_setup_py)
            cmds.warning('发现病毒, 但未找到病毒路径')
            return
        virus_path = virus_path[0]
        virus_path = os.getenv('APPDATA') + '\\' + virus_path
        if os.path.isdir(virus_path):
            shutil.rmtree(virus_path)
            cmds.warning('病毒清理完成')
        else:
            cmds.warning('病毒路径不存在')
