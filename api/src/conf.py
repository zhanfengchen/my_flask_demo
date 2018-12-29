#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 12/29/18 11:51 AM
# @Author  : zhanfengchen
# @Site    : 
# @File    : conf.py
# @Software: PyCharm
import os


ROOT_PATH = os.path.dirname(__file__)
ROOT_PATH = ROOT_PATH if ROOT_PATH else '.'
DATA_PATH = os.path.join(ROOT_PATH, '/../../data/')


logging_filename = os.path.join(DATA_PATH, 'conf/logger.ini')
conf_filename = os.path.join(DATA_PATH, 'conf/conf.ini')
