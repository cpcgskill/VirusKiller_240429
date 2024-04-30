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
import kill_mayafile
import subprocess


def clear_virus():
    kill.kill_virus()


def alone_clear_hik_virus():
    kill.kill_hik()


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


def batch_clear_maya_file():
    """
    批量清理Maya文件.
    """
    # 弹窗警告
    result = cmds.confirmDialog(
        title='警告',
        message='正则批量清理Maya文件, 可能会导致文件损坏, 请注意备份',
        button=['Ok', 'Cancel'],
        defaultButton='Cancel',
        cancelButton='Cancel',
        dismissString='Cancel',
    )
    if result == 'Cancel':
        cmds.warning('已取消')
        return

    #
    cmds.warning('开始批量处理...')
    files = cmds.fileDialog2(fileMode=4, dialogStyle=2)
    if not files:
        cmds.warning('未选择文件')
        return
    for file in files:
        try:
            kill_mayafile.process_file(os.path.abspath(file))
        except Exception as e:
            import traceback
            traceback.print_exc()
            cmds.warning('处理文件{}失败: {}'.format(file, e))
        else:
            cmds.warning('处理文件{}成功'.format(file))
    cmds.warning('批量处理完成')


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
    cmds.button(label='单独清除HIK病毒', command=lambda *args: alone_clear_hik_virus())
    cmds.button(label='恢复UAC设置', command=lambda *args: restore_UAC())
    cmds.button(label='清除病毒脚本节点', command=lambda *args: clear_virus_script_node())
    cmds.button(label='批量清理Maya文件', command=lambda *args: batch_clear_maya_file())

    cmds.showWindow('VirusKiller_240429')


if __name__ == '__main__':
    create_gui()
