#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time
import random


# 这里使用方法__new__来实现单例模式
#非线程安全
class Singleton(object):
    def __init__(self):
        time.sleep(1)

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


#线程安全单例
class SingletonMultiThreadSafe(object):
    __singleton_lock = threading.Lock()

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            with cls.__singleton_lock:
                orig = super(SingletonMultiThreadSafe, cls)
                cls._instance = orig.__new__(cls, *args, **kw)

        return cls._instance


def taskSimpleSingleton(arg):
    obj = Singleton()
    print "thread {index}: {objAddr}".format(index=arg, objAddr=obj)


def taskMultiThreadSafelSingleton(arg):
    obj = SingletonMultiThreadSafe()
    print "thread {index}: {objAddr}".format(index=arg, objAddr=obj)


# 简单的 非线程安全的 单例测试
print "=== start simple singleton test ==="

for i in range(10):
    t = threading.Thread(target=taskSimpleSingleton, args=[i, ])
    t.start()

time.sleep(5)

# 线程安全的 单例测试，建议使用
print "=== start safe singleton test ==="

for i in range(10):
    t = threading.Thread(target=taskMultiThreadSafelSingleton, args=[i, ])
    t.start()

'''
输出结果：
=== start simple singleton test ===
thread 2: <__main__.Singleton object at 0x0000000002D2EA90>
thread 1: <__main__.Singleton object at 0x0000000002D2EA90>
thread 0: <__main__.Singleton object at 0x0000000002D2EA90>
thread 6: <__main__.Singleton object at 0x0000000002D2EA90>
thread 5: <__main__.Singleton object at 0x0000000002D2EA90>
thread 4: <__main__.Singleton object at 0x0000000002D2EA90>
thread 3: <__main__.Singleton object at 0x0000000002D2EA90>
thread 8: <__main__.Singleton object at 0x0000000002D2EA90>
thread 7: <__main__.Singleton object at 0x0000000002D2EA90>
thread 9: <__main__.Singleton object at 0x0000000002D2EA90>

=== start safe singleton test ===
thread 0: <__main__.SingletonMultiThreadSafe object at 0x0000000002D2EBE0>
thread 1: <__main__.SingletonMultiThreadSafe object at 0x0000000002D2EBE0>
thread 2: <__main__.SingletonMultiThreadSafe object at 0x0000000002D2EBE0>
thread 3: <__main__.SingletonMultiThreadSafe object at 0x0000000002D2EBE0>
thread 4: <__main__.SingletonMultiThreadSafe object at 0x0000000002D2EBE0>
thread 5: <__main__.SingletonMultiThreadSafe object at 0x0000000002D2EBE0>
thread 6: <__main__.SingletonMultiThreadSafe object at 0x0000000002D2EBE0>
thread 7: <__main__.SingletonMultiThreadSafe object at 0x0000000002D2EBE0>
thread 8: <__main__.SingletonMultiThreadSafe object at 0x0000000002D2EBE0>
thread 9: <__main__.SingletonMultiThreadSafe object at 0x0000000002D2EBE0>
'''

