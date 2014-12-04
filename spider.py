#!/usr/bin/env python
 # -*- coding: utf-8 -*-

import urllib2
import urllib
import re
import thread
import time


class Spider_Model:
    
    #初始化 page当前页数, pages存储内容
    def __init__(self):
        self.page = 1
        self.pages = []
        self.enable = False

    #对段子进行筛选
    def GetPage(self, page):
        myUrl = "http://m.qiushibaike.com/hot/page/" + page
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        req = urllib2.Request(myUrl, headers = headers)
        myResponse = urllib2.urlopen(req)
        myPage = myResponse.read()
        unicodePage = myPage.decode("utf-8")
        myItems = re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',unicodePage,re.S)
        items = []
        for item in myItems:
            items.append([item[0].replace("\n",""),item[1].replace("\n","")])
        return items

    #加载新的段子
    def LoadPage(self):
        while self.enable:
            if len(self.pages) < 2:
                try:
                    myPage = self.GetPage(str(self.page))
                    self.page += 1
                    self.pages.append(myPage)
                except:
                    print u"无法链接到糗事百科"
            else:
                time.sleep(1)

    #显示段子
    def ShowPage(self, nowPage, page):
        for items in nowPage:
            print u"第%d页" % page, items[0] , items[1]
            myInput = raw_input()
            if myInput == "quit":
                self.enable = False
                break


    def Start(self):
        self.enable = True
        page = self.page
        print u"正在加载中请稍等......." 
        thread.start_new_thread(self.LoadPage, ())

        while self.enable:
            if self.pages:
                nowPage = self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage, page)
                page += 1


print u"请按下回车浏览今日的糗百内容："
raw_input(' ')
myModel = Spider_Model()
myModel.Start()
