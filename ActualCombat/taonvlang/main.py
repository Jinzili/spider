# !/usr/bin/env python
# -*- coding:UTF-8 -*-
# author: zili

import urllib
import urllib2
import json
import file_util
import threading

class TNL:
    def __init__(self, threads_num):
        self.root_url = 'https://mm.taobao.com/search_tstar_model.htm'
        self.post_url = 'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8'
        self.total_page = 0
        self.root_dir = 'images'
        self.threads_num = threads_num

    def get_total_page(self, mm_info_per_page):
        # 返回数据 totalPage 是假的 fuck
        # self.total_page = mm_info_per_page['data']['totalPage']
        # total = 166
        self.total_page = 50

    def get_per_page_info(self, page_num):
        data = {
            'q': '',
            'viewFlag': 'A',
            'sortType': 'default',
            'searchStyle': '',
            'searchRegion': 'city:',
            'searchFansNum': '',
            'currentPage': page_num,
            'pageSize': '100'
        }
        print data
        values = urllib.urlencode(data)
        try:
            request = urllib2.Request(self.post_url, values)
            response = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            if hasattr(e, 'reason'):
                print e.reason
        mm_info_per_page = json.loads(response.read().decode('GBK').encode('utf-8'))
        if page_num == 1:
            self.get_total_page(mm_info_per_page)
        return mm_info_per_page

    def get_per_page_info_temp(self, page_num):
        data = {
            'q': '',
            'viewFlag': 'A',
            'sortType': 'default',
            'searchStyle': '',
            'searchRegion': 'city:',
            'searchFansNum': '',
            'currentPage': page_num,
            'pageSize': 100
        }
        print data
        values = urllib.urlencode(data)
        try:
            request = urllib2.Request(self.post_url, values)
            response = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            if hasattr(e, 'reason'):
                print e.reason
        mm_info_per_page = json.loads(response.read().decode('GBK').encode('utf-8'))
        if page_num == 1:
            self.get_total_page(mm_info_per_page)
        return mm_info_per_page

    def save_per_page_info(self, mm_info_per_page):
        print mm_info_per_page
        mm_info_list = mm_info_per_page['data']['searchDOList']
        for each_mm in mm_info_list:
            if each_mm['cardUrl'] == '':
                continue
            image_url = 'http:' + each_mm['cardUrl']
            real_name = each_mm['realName'] if each_mm['realName'] != '' else 'default'
            height = each_mm['height'] if each_mm['height'] != '' else 'default'
            weight = each_mm['weight'] if each_mm['weight'] != '' else 'default'
            file_name = '%s/%s-%s-%s.jpg' % (self.root_dir, real_name, height, weight)
            file_util.save_image(image_url, file_name)

    def start(self):
        # 为了获取total_page
        page_num = 1
        print self.get_per_page_info(page_num)
        page_list = [i for i in xrange(self.total_page)]
        limit_list = file_util.limit_list(page_list, self.threads_num)
        for each_list in limit_list:
            t = threading.Thread(target=self.thread_action, args=(each_list,))
            t.start()

    def thread_action(self, args):
        for i in args:
            print i
            self.save_per_page_info(self.get_per_page_info(i))
spider = TNL(5)
spider.start()