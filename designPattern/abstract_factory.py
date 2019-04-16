#!/usr/bin/python
# -*- coding: UTF-8 -*-

import abc
import six


# 抽象工厂类 实现
@six.add_metaclass(abc.ABCMeta)
class AbstractFactory():
    @abc.abstractmethod
    def createProductA(self):
        pass

    @abc.abstractmethod
    def createProductB(self):
        pass


@six.add_metaclass(abc.ABCMeta)
class AbstractProductA():
    @abc.abstractmethod
    def funA(self):
        pass


@six.add_metaclass(abc.ABCMeta)
class AbstractProductB():
    @abc.abstractmethod
    def funB(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def createProductA(self):
        return ConcreateProductA1()

    def createProductB(self):
        return ConcreateProductB1()


class ConcreteFactory2(AbstractFactory):
    def createProductA(self):
        return ConcreateProductA2()

    def createProductB(self):
        return ConcreateProductB2()


class ConcreateProductA1(AbstractProductA):
    def funA(self):
        return "The result of product A1"


class ConcreateProductA2(AbstractProductA):
    def funA(self):
        return "The result of product A2"


class ConcreateProductB1(AbstractProductB):
    def funB(self):
        return "The result of product B1"


class ConcreateProductB2(AbstractProductB):
    def funB(self):
        return "The result of product B2"


# Test
fc1 = ConcreteFactory1()
print "Create ConcreteFactory1"
pa1 = fc1.createProductA()
print pa1.funA()
pb1 = fc1.createProductB()
print pb1.funB()
fc2 = ConcreteFactory2()
print "Create ConcreteFactory2"
pa2 = fc2.createProductA()
print pa2.funA()
pb2 = fc2.createProductB()
print pb2.funB()

'''
输出结果：
    Create ConcreteFactory1
    The result of product A1
    The result of product B1
    Create ConcreteFactory2
    The result of product A2
    The result of product B2
'''
