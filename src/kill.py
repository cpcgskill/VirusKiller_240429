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
    user_setup_mel = cmds.internalVar(userAppDir=True) + '/scripts/userSetup.mel'
    if os.path.exists(user_setup_mel):
        with open(user_setup_mel, 'rb') as f:
            data = f.read()
        cmds.warning('搜索病毒userSetup.mel...')
        virus_code = re.findall(
            r'import base64;\s*pyCode\s*=\s*base64\.urlsafe_b64decode\([\'\"](.*?)[\"\']\)',
            data,
        )
        if len(virus_code) < 1:
            cmds.warning('未发现病毒')
            return
        os.remove(user_setup_mel)
        cmds.warning('发现病毒userSetup.mel, 已清理')

        cmds.warning('搜索病毒本体...')
        virus_code = virus_code[0]
        virus_code = base64.urlsafe_b64decode(virus_code)
        virus_path = re.findall(
            r'maya_path_\s*=\s*os.getenv\([\'\"]APPDATA[\'\"]\)\+[\'\"]\\([a-zA-Z0-9]+)[\'\"]',
            virus_code,
        )
        if len(virus_path) < 1:
            cmds.warning('发现病毒userSetup.mel, 但未找到病毒路径')
        else:
            virus_path = virus_path[0]
            virus_path = os.getenv('APPDATA') + '\\' + virus_path
            if os.path.isdir(virus_path):
                os.remove(user_setup_mel)
                shutil.rmtree(virus_path)
                cmds.warning('病毒本体清理完成')
            else:
                cmds.warning('病毒路径不存在')

        cmds.warning('开始清理mayaHIK.pres.mel中的病毒代码')
        hik_mel_list = [
            os.path.join(os.getenv("MAYA_LOCATION"), 'resources/l10n/zh_CN/plug-ins/mayaHIK.pres.mel'),
            os.path.join(os.getenv("MAYA_LOCATION"), 'resources/l10n/ja_JP/plug-ins/mayaHIK.pres.mel'),
        ]
        hik_regex = r'python\(\"import base64;\s*pyCode\s*=\s*base64\.urlsafe_b64decode\([\'\"].*?[\"\']\);\s*exec\s*\(\s*pyCode\s*\)\"\)\s*;'
        for hik_mel in hik_mel_list:
            hik_mel = hik_mel.replace('\\', '/')
            with open(hik_mel, 'rb') as f:
                data = f.read()

            if len(re.findall(hik_regex, data)) > 0:
                cmds.warning('正在清理"{}"文件中的病毒代码'.format(hik_mel))
                with open(hik_mel, 'wb') as f:
                    f.write(re.sub(hik_regex, '', data, ))
                cmds.warning('"{}"文件中病毒代码已清除'.format(hik_mel))
            else:
                cmds.warning('"{}"文件中未发现病毒代码'.format(hik_mel))
        cmds.warning('mayaHIK.pres.mel中的病毒代码清理完成')
    else:
        cmds.warning('你的Maya好像没有被感染')
