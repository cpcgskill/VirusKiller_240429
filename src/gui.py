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

import json
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


def batch_clear_maya_file_ma():
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
            kill_mayafile.process_ma_file(os.path.abspath(file))
        except Exception as e:
            import traceback
            traceback.print_exc()
            cmds.warning('处理文件{}失败: {}'.format(file, e))
        else:
            cmds.warning('处理文件{}成功'.format(file))
    cmds.warning('批量处理完成')


def batch_clear_maya_file_mb():
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
            kill_mayafile.process_mb_file(os.path.abspath(file))
        except Exception as e:
            import traceback
            traceback.print_exc()
            cmds.warning('处理文件{}失败: {}'.format(file, e))
        else:
            cmds.warning('处理文件{}成功'.format(file))
    cmds.warning('批量处理完成')


def batch_check_maya_file():
    """
    批量检查Maya文件.
    """
    # 是否启用谨慎模式
    result = cmds.confirmDialog(
        title='警告',
        message='是否启用谨慎模式, 谨慎模式会检查文件中是否存在病毒代码, 但可能会误报',
        button=['Yes', 'No'],
        defaultButton='No',
        cancelButton='No',
        dismissString='No',
    )

    is_cautious = result == 'Yes'

    #
    cmds.warning('开始批量处理...')
    root_dir = cmds.fileDialog2(fileMode=3, dialogStyle=2)
    if not root_dir:
        cmds.warning('未选择文件')
        return

    warning_files = []
    for root, dirs, files in os.walk(os.path.abspath(root_dir[0])):
        for file in files:
            if file.endswith('.ma'):
                cmds.warning('检查文件: {}'.format(os.path.join(root, file)))
                has_virus = kill_mayafile.check_ma_file(os.path.join(root, file), is_cautious=is_cautious)
                if has_virus:
                    warning_files.append(os.path.join(root, file).replace('\\', '/'))
            if file.endswith('.mb'):
                cmds.warning('检查文件: {}'.format(os.path.join(root, file)))
                has_virus = kill_mayafile.check_mb_file(os.path.join(root, file), is_cautious=is_cautious)
                if has_virus:
                    warning_files.append(os.path.join(root, file).replace('\\', '/'))

    # show
    if warning_files:
        warning_text = '以下文件可能存在病毒代码:\n{}\n{}\n{}'.format(
            '=' * 20,
            '\n'.join(warning_files),
            '=' * 20
        )
        cmds.warning(warning_text)
    else:
        cmds.warning('未发现病毒代码')


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
    cmds.button(label='批量清理Maya文件(.ma)', command=lambda *args: batch_clear_maya_file_ma())
    cmds.button(label='批量清理Maya文件(.mb)', command=lambda *args: batch_clear_maya_file_mb())
    cmds.button(label='批量检查Maya文件', command=lambda *args: batch_check_maya_file())

    cmds.showWindow('VirusKiller_240429')


if __name__ == '__main__':
    create_gui()
