# !/usr/bin/env python
# -*- coding:UTF-8 -*-
# author: zili

import os
import urllib

def mkdir(path):
    path = path.strip()
    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)

def save_image(image_url, file_name):
    u = urllib.urlopen(image_url)
    data = u.read()
    f = open(file_name, 'wb')
    f.write(data)
    f.close()
