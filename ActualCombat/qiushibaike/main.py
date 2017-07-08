#!/usr/bin/env python
# --*-- coding:utf-8 --*--
# author:zili.jin

import urllib2
from bs4 import BeautifulSoup


class QSBK():
    def __init__(self):
        self.page = 1
        self.story_num = 0
        self.storys = []

    def load_page(self):
        print u'加载第 %d 页' % self.page
        url = 'http://www.qiushibaike.com/hot/page/' + str(self.page)
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        try:
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            soup = BeautifulSoup(content, 'lxml')
            wrap = soup.find_all('div', class_='article block untagged mb15')
            storys = []
            for each in wrap:
                author = each.select('div > a > h2')[0].string
                content = each.select('a.contentHerf div.content span')[0].string
                praise = each.select('div.stats span.stats-vote i.number')[0].string
                comment = each.select('div.stats span.stats-comments a i')[0].string
                thumb = each.select('div.thumb a img')
                each_story = dict()
                each_story['author'] = author
                each_story['content'] = content
                each_story['praise'] = praise
                each_story['comment'] = comment
                each_story['thumb'] = thumb[0].attrs['src'] if len(thumb) > 0 else ''
                storys.append(each_story)
            return storys
        except urllib2.URLError, e:
            if hasattr(e, 'code'):
                print e.code
            if hasattr(e, 'reason'):
                print e.reason

    def get_one_story(self):
        self.story_num = self.story_num + 1
        if self.story_num == len(self.storys):
            self.story_num = 0
            self.page = self.page + 1
            self.storys = self.load_page()
        next_story = self.storys[self.story_num]
        print u'author: %s' % next_story['author']
        print u'content: %s' % next_story['content']
        print u'praise: %s, comment: %s' % (next_story['praise'], next_story['comment'])
        print u'thumb: %s' % next_story['thumb']
        print '\n' * 2

    def start(self):
        self.storys = self.load_page()
        while 1:
            print u'正在读取糗事百科, 回车查看新段子, Q退出...'
            input_keyword = raw_input()
            if input_keyword == 'Q':
                return
            self.get_one_story()

spider = QSBK()
spider.start()