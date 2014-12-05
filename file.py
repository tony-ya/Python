#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Tony'

myFile = open('静夜思.txt', 'w')
myFile.write('静夜思\n窗前明月光，\n疑是地上霜。\n')
myFile.close()

myFile = open('静夜思.txt', 'a')
myFile.write('举头望明月，\n我叫郭德纲。\n')  
myFile.close()

myFile = open('静夜思.txt', 'r')
for line in myFile.readlines():
    print line

myFile.seek(0)
print len(myFile.readlines())
myFile.close()
