#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 意图：动态地给一个对象添加一些额外的职责。就增加功能来说，装饰器模式相比生成子类更为灵活。
# 主要解决：一般的，我们为了扩展一个类经常使用继承方式实现，由于继承为类引入静态特征，并且随着扩展功能的增多，子类会很膨胀
import abc
import six


# 组件 抽象类
@six.add_metaclass(abc.ABCMeta)
class Component():
    @abc.abstractmethod
    def operation(self):
        pass


# 具体的组件
class ConcreteComponent(Component):
    def operation(self):
        return "Simple Component"


# 装饰器
class Decorator(Component):
    _component = None

    def __init__(self, component):
        self._component = component

    @property
    def component(self):
        return self._component

    def operation(self):
        self._component.operation()


# 装饰器A
class ConcreteDecoratorA(Decorator):
    def operation(self):
        return "ConcreteDecoratorA(%s)" % (self.component.operation())


# 装饰器B
class ConcreteDecoratorB(Decorator):
    def operation(self):
        return "ConcreteDecoratorB(%s)" % (self.component.operation())


# Test
simple = ConcreteComponent()
print "I've got a simple componnent: " + simple.operation()
decoratorA = ConcreteDecoratorA(simple)
print "I'v got a decoratorA: " + decoratorA.operation()
decoratorB = ConcreteDecoratorB(decoratorA)
print "I'v got a decoratorB: " + decoratorB.operation()

'''
输出结果：
    I've got a simple componnent: Simple Component
    I'v got a decoratorA: ConcreteDecoratorA(Simple Component)
    I'v got a decoratorB: ConcreteDecoratorB(ConcreteDecoratorA(Simple Component))
'''


# 下面 我们以星巴克咖啡 为例
# 原味拿铁 加糖 2元， 加奶3元，升杯3元

@six.add_metaclass(abc.ABCMeta)
class Coffee():
    @property
    def price(self):
        pass

    @price.setter
    def price(self, v_price):
        pass

    @property
    def name(self):
        pass

    @name.setter
    def name(self, v_name):
        pass


class latteCoffee(Coffee):
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, v_price):
        self._price = v_price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v_name):
        self._name = v_name


class coffeeDecorator(Coffee):
    _coffee = None

    def __init__(self, coffee):
        self._coffee = coffee

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, v_price):
        self._price = v_price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v_name):
        self._name = v_name


class sugarLatteeCoffee(coffeeDecorator):
    _price = 2.0
    _name = "sugar"

    @property
    def price(self):
        return self._price + self.coffee.price

    @price.setter
    def price(self, v_price):
        self._price = v_price

    @property
    def name(self):
        return self.coffee.name + "+" + self._name

    @name.setter
    def name(self, v_name):
        self._name = v_name


class biggerLatteeCoffee(coffeeDecorator):
    _price = 3.0
    _name = "bigger"

    @property
    def price(self):
        return self._price + self.coffee.price

    @price.setter
    def price(self, v_price):
        self._price = v_price

    @property
    def name(self):
        return self.coffee.name + "+" + self._name

    @name.setter
    def name(self, v_name):
        self._name = v_name


class milkLatteeCoffee(coffeeDecorator):
    _price = 3.0
    _name = "milk"

    @property
    def price(self):
        return self._price + self.coffee.price

    @price.setter
    def price(self, v_price):
        self._price = v_price

    @property
    def name(self):
        return self.coffee.name + "+" + self._name

    @name.setter
    def name(self, v_name):
        self._name = v_name


# Test
lattee = latteCoffee()
lattee.name = "lattee"
lattee.price = 30.0
print "I'v got a coffee name: %s , price %.2f" % (lattee.name, lattee.price)
sugarLattee = sugarLatteeCoffee(lattee)
print "I'v got a coffee name: %s , price %.2f" % (sugarLattee.name, sugarLattee.price)
milkLattee = milkLatteeCoffee(sugarLattee)
print "I'v got a coffee name: %s , price %.2f" % (milkLattee.name, milkLattee.price)
biggerLattee = biggerLatteeCoffee(milkLattee)
print "I'v got a coffee name: %s , price %.2f" % (biggerLattee.name, biggerLattee.price)

'''
输出结果
    I'v got a coffee name: lattee , price 30.00
    I'v got a coffee name: lattee+sugar , price 32.00
    I'v got a coffee name: lattee+sugar+milk , price 35.00
    I'v got a coffee name: lattee+sugar+milk+bigger , price 38.00
'''
