#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# author:zili.jin

import urllib2
import urllib
from bs4 import BeautifulSoup


class BDTB:

    def __init__(self, base_url, see_lz):
        self.base_url = base_url
        self.see_lz = '?see_lz=' + str(see_lz)
        self.page_num = 1
        self.total_page = 0

    def get_total_page(self):
        total_page_str = self.soup.select_one('div#thread_theme_5 div.l_thread_info '
                                              'ul.l_posts_num li.l_reply_num span')[1].string
        self.total_page = int(total_page_str)

    def get_page_soup(self, page_num):
        try:
            url = self.base_url + self.see_lz + '&pn=' + str(page_num)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            soup = BeautifulSoup(response.read(), 'lxml')
            if page_num == 1:
                print soup.select('div.wrap1 div.wrap2 div#container div#thread_theme_5 div.l_thread_info ul.l_posts_num').contents[1].select('span')

                total_page_str = soup.select('div#thread_theme_5 div.l_thread_info'
                                             'ul.l_posts_num li.l_reply_num span')[1].string
                self.total_page = int(total_page_str)
            return soup.select('div.content')[0]
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                print e.reason

    def get_core_title_(self):
        return self.soup.select('div#j_core_title_wrap h3.core_title_txt')[0].string

    def get_each_page_info(self):
        items = self.get_page_soup(self.page_num).select('div#j_p_postlist div.l_post')
        page_info = []
        for item in items:
            author = item.select_one('div.d_author ul.p_author li.d_name a').string
            floor = item.select_one('div.d_post_content_main div.core_reply div.core_reply_tail '
                                    'div.post-tail-wrap span.tail-info').string
            timestamp = item.select('div.d_post_content_main div.core_reply div.core_reply_tail '
                                    'div.post-tail-wrap span.tail-info')[1].string
            content = item.select_one('div.p_content div.d_post_content').get_text()
            each_info = dict()
            each_info['author'] = author
            each_info['floor'] = floor
            each_info['timestamp'] = timestamp
            each_info['content'] = content
            page_info.append(each_info)
        return page_info

    def print_page_info(self, page_num):
        self.get_page_soup(page_num)
        infos = self.get_each_page_info()
        for info in infos:
            print u'author: %s  floor: %s' % (info['author'], info['floor'])
            print info['timestamp']
            print info['content']
            print '\n' * 2

    def start(self):
        self.print_page_info(self.page_num)
        while 1:
            print u'回车加载下一页, 按Q退出...'
            input_keyword = raw_input()
            if input_keyword == 'Q':
                return
            if input_keyword == 'n':
                if self.page_num == self.total_page:
                    print u'已经是最后一页啦!'
                    return
                self.page_num = self.page_num + 1
                print u'正在加载第 %d 页数据...' % self.page_num
                self.print_page_info(self.page_num)


spider = BDTB('https://tieba.baidu.com/p/3138733512', 1)
spider.start()
