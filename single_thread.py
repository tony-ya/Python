#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Tony"

import thread
from time import ctime, sleep

def music(music_name, length):
    for i in range(4):
        print "I was listening to %s" % music_name, ctime()
        sleep(length)

def movie(movie_name, length):
    for i in range(2):
        print "I was at the movie %s" % movie_name, ctime()
        sleep(length)

if __name__ == '__main__':
    music('风起时，想你', 2)
    movie('变形金刚', 4)
    print "all over %s" % ctime()
