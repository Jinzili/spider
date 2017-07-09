#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# author:zili.jin

import urllib2
import urllib


def build_request():
    request = urllib2.Request('http://www.baidu.com')
    response = urllib2.urlopen(request)
    print response.read()


def build_request_post():
    values = {'username': 'jinzili777', 'password': 'jinzili373690'}
    data = urllib.urlencode(values)
    url = 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    print response.read()


def taonvlang():
    url = 'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'
    data = {
        'q': '',
        'viewFlag': 'A',
        'sortType': 'default',
        'searchStyle': '',
        'searchRegion': 'city:',
        'searchFansNum': '',
        'currentPage': 2,
        'pageSize': '100'
    }
    values = urllib.urlencode(data)
    request = urllib2.Request(url, values)
    response = urllib2.urlopen(request)
    print response.read()


def build_request_get():
    values = dict()
    values['username'] = 'jinzili777'
    values['password'] = 'jinzili373690'
    data = urllib.urlencode(values)
    url = "http://passport.csdn.net/account/login"
    geturl = url + '?' + data
    request = urllib2.Request(geturl)
    response = urllib2.urlopen(request)
    print response.read()

if __name__ == '__main__':
    # build_request()
    # build_request_post()
    # build_request_get()
    taonvlang()