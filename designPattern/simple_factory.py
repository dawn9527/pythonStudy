#!/usr/bin/python
# -*- coding: UTF-8 -*-

import abc
import six


#

# 简单工厂类 实现

@six.add_metaclass(abc.ABCMeta)
class Product():
    @abc.abstractmethod
    def create(self):
        pass


class ProductA(Product):
    def create(self):
        return "I Am Product A"


class ProductB(Product):
    def create(self):
        return "I Am Product B"


class SimpleFactory():
    def createProduct(self, proname):
        if proname == 'A':
            return ProductA()
        elif proname == 'B':
            return ProductB()


# Test
simpleFactory = SimpleFactory()
print "Create A SimpleFactory"
product = simpleFactory.createProduct('A')
print "Create Product: %s" % (product.__class__.__name__)
product = simpleFactory.createProduct('B')
print "Create Product: %s" % (product.__class__.__name__)

'''
输出结果：
    Create A SimpleFactory
    Create Product: ProductA
    Create Product: ProductB
'''
