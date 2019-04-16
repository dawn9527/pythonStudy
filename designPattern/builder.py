#!/usr/bin/python
# -*- coding: UTF-8 -*-

import abc
import six


# 建造者模式
@six.add_metaclass(abc.ABCMeta)
class Builder():
    @abc.abstractproperty
    def product(self):
        pass

    @abc.abstractmethod
    def produce_part_a(self):
        pass

    @abc.abstractmethod
    def produce_part_b(self):
        pass


class ConcreteBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product()

    @property
    def product(self):
        product = self._product
        self.reset()
        return product

    def produce_part_a(self):
        self._product.add("Part A")

    def produce_part_b(self):
        self._product.add("Part B")


class Product():
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        print "Product parts : " + ", ".join(str(i) for i in self.parts)


class Director():
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, v_builder):
        self._builder = v_builder

    def build_minimal_viable_product(self):
        self.builder.produce_part_a()

    def build_full_featured_product(self):
        self.builder.produce_part_a()
        self.builder.produce_part_b()


# Test
director = Director()
builder = ConcreteBuilder()
director.builder = builder
print "Standard basic product:"
director.build_minimal_viable_product()
builder.product.list_parts()
print("Standard full featured product: ")
director.build_full_featured_product()
builder.product.list_parts()


# 我们现在去麦当劳点餐，并生成一个订单
# 麦当劳 食物主要分类 汉堡，饮料，小食 ，我们以这三类食物为例

@six.add_metaclass(abc.ABCMeta)
class AbstractOrderBuilder():
    @property
    def food(self):
        pass

    @abc.abstractmethod
    def addBurger(self, v_burger):
        pass

    @abc.abstractmethod
    def addSnack(self, v_snack):
        pass

    @abc.abstractmethod
    def addBeverage(self, v_beverage):
        pass


class ConcreteOrderBuilder(AbstractOrderBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._food = FoodProduct()

    @property
    def food(self):
        food = self._food;
        self.reset()
        return food

    def addBurger(self, v_burger):
        self._food.add(v_burger)

    def addSnack(self, v_snack):
        self._food.add(v_snack)

    def addBeverage(self, v_beverage):
        self._food.add(v_beverage)


class FoodProduct():
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def list_parts(self):
        names = []
        price = 0.0
        for part in self.parts:
            names.append(part.name)
            price = price + part.price
        print "I'v got food: " + ", ".join(names)
        print "Total price is: " + str(price)


class Order():
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, v_builder):
        self._builder = v_builder

    def addBurger(self, v_burger):
        self._builder.addBurger(v_burger)

    def addSnack(self, v_snack):
        self._builder.addBurger(v_snack)

    def addBeverage(self, v_beverage):
        self._builder.addBurger(v_beverage)


class Burger():
    def __init__(self, v_name, v_price):
        self.name = v_name
        self.price = v_price


class Snack():
    def __init__(self, v_name, v_price):
        self.name = v_name
        self.price = v_price


class Beverage():
    def __init__(self, v_name, v_price):
        self.name = v_name
        self.price = v_price


# Test
# 价目表
# Burger ---- cheese burger 10.0 ,  spicy chicken burger 15
# Snack ---- chips 6.0, chicken wings 12.0
# Beverage ----  coke 4.0, milk 5.0
order = Order()
orderBuilder = ConcreteOrderBuilder()
order.builder = orderBuilder

print "First time i order"
order.builder.addBurger(Burger("cheese burger", 10.0))
order.builder.addSnack(Snack("chicken wings", 12.0))
order.builder.addBeverage(Beverage("coke", 4.0))
order.builder.food.list_parts()
print "Second time i order"
order.builder.addBurger(Burger("cheese burger", 10.0))
order.builder.addBurger(Burger("spicy chicken burger", 15.0))
order.builder.addBeverage(Beverage("milk", 5.0))
order.builder.addSnack(Snack("chips", 6.0))
order.builder.food.list_parts()

'''
输出结果：
    First time i order
    I'v got food: cheese burger, chicken wings, coke
    Total price is: 26.0
    Second time i order
    I'v got food: cheese burger, spicy chicken burger, milk, chips
    Total price is: 36.0
'''
