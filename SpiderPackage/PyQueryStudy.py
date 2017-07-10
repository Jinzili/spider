#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# author:zili.jin

from pyquery import PyQuery as pq


def p(e):
    print type(e)

doc = pq(filename='hello.html')
print doc.html()
lis = doc('li')
lis.each(lambda e, item: item.text())


for li in lis.items():
    print type(li)

