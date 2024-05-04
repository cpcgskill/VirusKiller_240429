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

ma_find_script_node_regex = re.compile(
    r'\s*createNode\s+script\s+-n\s+\"uifiguration\";\s*.*?setAttr\s*\"\.b\"\s*-type\s*"string".*?\s*setAttr\s*"\.st"\s*1;\s*'.encode(),
    re.DOTALL,
)
cautious_check_regex = re.compile(
    r'\s*import\s*base64;?\s*'.encode(),
    re.DOTALL,
)
mb_regex = re.compile(
    r'\s*?python\s*?\(\s*?\"\s*?import\s+?base64;.*?;\s*?exec\s*?\(\s*?_pycode\s*?\)\s*?\"\s*?\)\s*?;\s*?'.encode(),
    re.DOTALL
)


def _process_ma_content(data):
    for i in reversed(list(ma_find_script_node_regex.finditer(data))):
        start, end = i.span()
        print(data[start:end])
        data = data[:start] + b'\n' + data[end:]

    return data


def check_ma_file(file, is_cautious=False):
    file = os.path.abspath(file).replace('\\', '/')
    with open(file, 'rb') as f:
        # data = _delete_ma_byte(f.read())
        data = f.read()

    if is_cautious and cautious_check_regex.search(data):
        return True
    if ma_find_script_node_regex.search(data):
        return True
    return False


def process_ma_file(file):
    file = os.path.abspath(file).replace('\\', '/')
    with open(file, 'rb') as f:
        # data = _delete_ma_byte(f.read())
        data = f.read()

    new_data = _process_ma_content(data)
    if new_data != data:
        with open(file, 'wb') as f:
            f.write(new_data)
    else:
        cmds.warning('"{}" 未发现病毒'.format(file))


def check_mb_file(file, is_cautious=False):
    file = os.path.abspath(file).replace('\\', '/')
    with open(file, 'rb') as f:
        # data = _delete_ma_byte(f.read())
        data = f.read()
    if is_cautious and cautious_check_regex.search(data):
        return True
    if mb_regex.search(data):
        return True
    return False


def _process_mb_content(data):
    for i in reversed(list(mb_regex.finditer(data))):
        start, end = i.span()
        print(data[start:end])
        data = data[:start] + b'\n' + data[end:]

    return data


def process_mb_file(file):
    file = os.path.abspath(file).replace('\\', '/')
    with open(file, 'rb') as f:
        data = f.read()

    new_data = _process_mb_content(data)
    if new_data != data:
        with open(file, 'wb') as f:
            f.write(new_data)
    else:
        cmds.warning('"{}" 未发现病毒'.format(file))


if __name__ == '__main__':
    with open('./../testfiles/key.ma', 'rb') as f:
        _test_data = f.read()
        assert _process_ma_content(_test_data) != _test_data
    with open('./../testfiles/key.mb', 'rb') as f:
        _test_data = f.read()
        assert _process_mb_content(_test_data) != _test_data
    with open('./../testfiles/normal.ma', 'rb') as f:
        _test_data = f.read()
        assert _process_ma_content(_test_data) == _test_data
    with open('./../testfiles/normal.mb', 'rb') as f:
        _test_data = f.read()
        assert _process_mb_content(_test_data) == _test_data
    assert check_ma_file('./../testfiles/key.ma', is_cautious=True)
    assert check_mb_file('./../testfiles/key.mb', is_cautious=True)
    assert not check_ma_file('./../testfiles/normal.ma', is_cautious=True)
    assert not check_mb_file('./../testfiles/normal.mb', is_cautious=True)
