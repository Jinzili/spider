# !/usr/bin/env python
# -*- coding:UTF-8 -*-
# author: zili

import os
import urllib
import sys


def mkdir(path):
    path = path.strip()
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)


def save_image(image_url, file_name):
    print 'saving: %s' % image_url
    u = urllib.urlopen(image_url)
    data = u.read()
    f = open(file_name, 'wb')
    f.write(data)
    f.close()


def limit_list(list, num):
    length = len(list)
    if length == 0:
        return []
    per_num = length / num
    left = length % num
    i = 0
    resp_list = []
    while i < num - 1:
        start = i * per_num
        i = i + 1
        end = i * per_num
        sub_list = list[start:end]
        resp_list.append(sub_list)
    else:
        resp_list.append(list[i * per_num:length])
    return resp_list

def LongToInt(value):
    assert isinstance(value, (int, long))
    return int(value & sys.maxint)