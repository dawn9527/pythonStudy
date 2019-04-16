#!/usr/bin/python
# -*- coding: UTF-8 -*-

import abc
import six


#

# 工厂类 实现
@six.add_metaclass(abc.ABCMeta)
class Product():
    @abc.abstractmethod
    def create(self):
        pass

@six.add_metaclass(abc.ABCMeta)
class Factory():
    @abc.abstractmethod
    def createProduct(self):
        pass

class ProductA(Product):
    def create(self):
        return "I Am Product A"


class ProductB(Product):
    def create(self):
        return "I Am Product B"

class FactoryA(Factory):
    def createProduct(self):
        return ProductA()

class FactoryB(Factory):
    def createProduct(self):
        return ProductB()

#Test
factoryA = FactoryA()
print "Create FactoryA"
product = factoryA.createProduct()
print "Create Product: %s" % (product.__class__.__name__)
factoryB = FactoryB()
print "Create FactoryB"
product = factoryB.createProduct()
print "Create Product: %s" % (product.__class__.__name__)

'''
输出结果：
    Create FactoryA
    Create Product: ProductA
    Create FactoryB
    Create Product: ProductB
'''