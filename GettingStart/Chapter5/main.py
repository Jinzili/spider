#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# author:zili.jin

import urllib2


def build_request_with_exception():
    request = urllib2.Request('http://www.xxxxxasdfasdfadfdof,iaxxxxxx.com')
    try:
        response = urllib2.urlopen(request)
        print response.read()
    except urllib2.URLError, e:
        print e.reason
    else:
        print 'success'


if __name__ == '__main__':
    build_request_with_exception()

