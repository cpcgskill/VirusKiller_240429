# -*-coding:utf-8 -*-
"""
:PROJECT_NAME: tee
:File: kill-mayafile.py
:Time: 2024/4/26 下午11:06
:Author: 张隆鑫
"""
from __future__ import unicode_literals, print_function, division

if False:
    from typing import *

import re
import os
import sys
import maya.cmds as cmds

find_script_node_regex = re.compile(
    r'\s*createNode\s+script\s+-n\s+\"uifiguration\";\s*.*?setAttr\s*\"\.b\"\s*-type\s*"string".*?\s*setAttr\s*"\.st"\s*1;\s*',
    re.DOTALL,
)


def _process_str(data):
    for i in reversed(list(find_script_node_regex.finditer(data))):
        start, end = i.span()
        print(data[start:end])
        data = data[:start] + '\n' + data[end:]

    return data


cautious_check_regex = re.compile(
    r'\s*import\s*base64;?\s*',
    re.DOTALL,
)


def check_file(file, is_cautious=False):
    file = os.path.abspath(file).replace('\\', '/')
    with open(file, 'rb') as f:
        data = _delete_ma_byte(f.read())

    if is_cautious and cautious_check_regex.search(data):
        return True
    if find_script_node_regex.search(data):
        return True
    return False


def _delete_ma_byte(data):
    try:
        data = data.decode('utf-8')
    except UnicodeDecodeError:
        try:
            data = data.decode('gbk')
        except UnicodeDecodeError:
            raise ValueError('无法解码文件')
    return data


def process_file(file):
    file = os.path.abspath(file).replace('\\', '/')
    with open(file, 'rb') as f:
        data = _delete_ma_byte(f.read())

    new_data = _process_str(data)
    if new_data != data:
        with open(file, 'wb') as f:
            f.write(new_data)
    else:
        cmds.warning('"{}" 未发现病毒'.format(file))


if __name__ == '__main__':
    with open('./../testfiles/key.ma', 'rb') as f:
        # print(_process_str(f.read()))
        _test_data = _delete_ma_byte(f.read())
        assert _process_str(_test_data) != _test_data
    assert check_file('./../testfiles/key.ma', is_cautious=True)
