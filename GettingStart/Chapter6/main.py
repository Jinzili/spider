#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# author:zili.jin

import urllib2
import cookielib


def get_cookie():
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    request = urllib2.Request('http://www.baidu.com')
    response = opener.open(request)
    for item in cookie:
        print 'Name = ' + item.name
        print 'Value = ' + item.value


def save_cookie_file():
    filename = '../data/cookie.txt'
    cookie = cookielib.MozillaCookieJar(filename)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    reponse = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)


def get_cookie_from_file():
    cookie = cookielib.MozillaCookieJar()
    cookie.load('../data/cookie.txt', ignore_discard=True, ignore_expires=True)
    request = urllib2.Request('http://www.baidu.com')
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(request)
    print response.read()


if __name__ == '__main__':
    # get_cookie()
    # save_cookie_file()
    get_cookie_from_file()
