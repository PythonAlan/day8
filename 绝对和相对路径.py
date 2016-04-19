#!/usr/bin/env python3
#antuor:Alan


import os
path = os.getcwd() #获取当前工作目录，即当前python脚本工作的目录绝对路径
print(path)
输出  '''/Users/Alan/Desktop/AlanProject/day5'''
path_a = os.path.dirname(os.path.abspath(__file__))
#获取当前工作目录，即当前python脚本工作的目录绝对路径
print (path_a)
输出  '''/Users/Alan/Desktop/AlanProject/day5'''
print(__file__)
输出  '''绝对和相对路径.py''' #得出绝对路径