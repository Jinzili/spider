#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# author:zili.jin

import urllib2
import urllib


def build_request_header():
    url = 'http://www.server.com'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    values = {'username': 'cqc', 'password': 'XXXX'}
    headers = {'User-Agent': user_agent, 'Referer':'http://www.zhihu.com/articles'}
    data = urllib.urlencode(values)
    request = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(request)
    print response.read()


def build_request_proxy():
    enable_proxy = True
    proxy_handler = urllib2.ProxyHandler({'http': 'http://some-proxy.com:8080'})
    null_proxy_handler = urllib2.ProxyHandler({})
    if enable_proxy:
        opener = urllib2.build_opener(proxy_handler)
    else:
        opener = urllib2.build_opener(null_proxy_handler)
    urllib2.install_opener(opener)


def build_request_put_or_delete():
    pass
    # request = urllib2.Request(uri, data=data)
    # request.get_method = lambda: 'PUT'
    # response = urllib2.urlopen(request)


def build_request_with_debug():
    http_handler = urllib2.HTTPHandler(debuglevel=1)
    https_handler = urllib2.HTTPSHandler(debuglevel=1)
    opener = urllib2.build_opener(http_handler, https_handler)
    urllib2.install_opener(opener)
    response = urllib2.urlopen('http://www.baidu.com')
    # print response.read()


if __name__ == '__main__':
    # build_request_header()
    build_request_with_debug()
