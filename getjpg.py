#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import re

class Get_Img:
    def __init__(self, url):
        self.url = url
    def getImg(self, html):
        reg = r'src="(.+?\.jpg)" pic_ext'
        imgre = re.compile(reg)
        imglist = re.findall(imgre, html)
        x = 0
        for imgurl in imglist:
            urllib.urlretrieve(imgurl, '%s.jpg' % x)
            x += 1
    def getHtml(self, url):
        page = urllib.urlopen(url)
        html = page.read()
        return html

getJpg = Get_Img('hello world')
html = getJpg.getHtml("http://tieba.baidu.com/p/3478859625")
getJpg.getImg(html)
