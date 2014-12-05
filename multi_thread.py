#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Tony"

import threading
from time import ctime, sleep

def music(music_name, length):
    for i in range(4):
        print "I was listening to %s" % music_name, ctime()
        sleep(length)

def movie(movie_name, length):
    for i in range(2):
        print "I was at the movie %s" % movie_name, ctime()
        sleep(length)

th1 = threading.Thread(target=music, args=('风起时，想你', 2))
th2 = threading.Thread(target=movie, args=('变形金刚', 4))
threads = [th1, th2]    #将两个线程放入一个列表中

if __name__ == '__main__':
    #最后使用一个for循环，依次将列表中的线程开启
    for t in threads:
        t.setDaemon(True)   #设置守护线程
        t.start()
    t.join()    #join()方法，用于等待线程终止。join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直等待。
print "all over %s" % ctime()
