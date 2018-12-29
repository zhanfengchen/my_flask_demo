#!/usr/bin/python
# -*-coding: utf-8-*-
import time


class MessageDecorator(object):
    def __init__(self):
        pass

    def add_message(self, func):
        def fun(*args, **kwargs):
            result_dic = func(*args, **kwargs)
            success = False if result_dic.get('is_label', 1000) == -1 or result_dic.get('isLabel', 1000) == -1 or result_dic.get('success', 1000) == -1 else True
            message = ''
            result = {
                'data': result_dic,
                'success': success,
                'message': message
            }
            return result
        return fun

    def add_new_message(self, func):
        def fun(*args, **kwargs):
            result_dic = func(*args, **kwargs)
            message = ''
            result_dic['message'] = message
            return result_dic
        return fun

msg_dector = MessageDecorator()


class TimeDecrator(object):
    def __init__(self):
        self._stand_time_format = "%Y-%m-%d %H:%M:%S"

    def _timestamp2string(self, timestamp):
        struct_time = time.localtime(timestamp)
        string = time.strftime(self._stand_time_format, struct_time)
        return string

    def _string2timestamp(self, string):
        struct_time = time.strptime(string, self._stand_time_format)
        timestamp = time.mktime(struct_time)
        return timestamp

    def local_time(self):
        return time.strftime(self._stand_time_format)

    def old_add_time(self, func):
        """ 装饰器获得程序执行的耗时和执行完的时间 """
        def fun(*args, **kwargs):
            res = func(*args, **kwargs)
            end_time = time.time()
            time_info = {'startTime': self._timestamp2string(end_time)}
            time_info.update(res)
            return time_info
        return fun

    def new_add_time(self, func):
        """ 装饰器获得程序执行的耗时和执行完的时间 """
        def fun(*args, **kwargs):
            begin_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            time_info = {'start_time': self._timestamp2string(end_time),
                         'cost_time': (end_time - begin_time)*1000}
            time_info.update(res)
            return time_info
        return fun


time_dector = TimeDecrator()