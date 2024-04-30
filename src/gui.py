# -*-coding:utf-8 -*-
"""
:PROJECT_NAME: VirusKiller_240429
:File: gui.py
:Time: 2024/4/29 下午3:16
:Author: 张隆鑫
"""
from __future__ import unicode_literals, print_function, division

import os
import re

if False:
    from typing import *

import maya.cmds as cmds
import kill
import subprocess


def clear_virus():
    kill.kill_virus()


def restore_UAC():
    subprocess.Popen(
        ['powershell', os.path.join(os.path.dirname(__file__), 'restore_UAC.ps1')],
    )


def clear_virus_script_node():
    script_node = cmds.ls(type='script')
    if script_node:
        virus_script_node = []
        for node in script_node:
            script = cmds.scriptNode(node, q=True, bs=True)
            if re.findall(r'import base64;\s*_pycode\s*=\s*base64\.urlsafe_b64decode\([\'\"](.*?)[\"\']\)', script):
                virus_script_node.append(node)
        if virus_script_node:
            for node in virus_script_node:
                cmds.delete(node)
            cmds.warning('病毒脚本节点清理完成')
        else:
            cmds.warning('未发现病毒脚本节点')
    else:
        cmds.warning('未发现病毒脚本节点')

# 从上到下三个按钮
def create_gui():
    # type: () -> None
    """
    创建 GUI.
    """
    if cmds.window('VirusKiller_240429', exists=True):
        cmds.deleteUI('VirusKiller_240429')

    cmds.window('VirusKiller_240429', title='VirusKiller_240429', widthHeight=(200, 200))

    cmds.columnLayout(adjustableColumn=True)

    cmds.button(label='清除病毒本体', command=lambda *args: clear_virus())
    cmds.button(label='恢复UAC设置', command=lambda *args: restore_UAC())
    cmds.button(label='清除病毒脚本节点', command=lambda *args: clear_virus_script_node())

    cmds.showWindow('VirusKiller_240429')


if __name__ == '__main__':
    create_gui()
