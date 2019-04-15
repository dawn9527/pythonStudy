#!/usr/bin/python
# -*- coding: UTF-8 -*-

import abc
import six

#six python2&3 兼容


#抽象主题类
@six.add_metaclass(abc.ABCMeta)
class Subject(object):

    @abc.abstractmethod
    def attach(self, observer):
        pass

    @abc.abstractmethod
    def detach(self, observer):
        pass

    @abc.abstractmethod
    def notify(self):
        pass

#抽象观察者类
@six.add_metaclass(abc.ABCMeta)
class Observer(object):
    @abc.abstractmethod
    def update(self, subject):
        pass


#具体主题
class ConcreteSubject(Subject):
    _observers = []
    _data = 0
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, v_data):
        if not isinstance(v_data, int):
            raise ValueError('data must be interger!')
        print "Subject Set Data: " + str(v_data)
        self._data = v_data
        self.notify()

    def attach(self, observer):
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer):
        print("Subject: Detached an observer.")
        self._observers.remove(observer)

    def notify(self):
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)



#具体观察者
class ConcreteObserver(Observer):
    _name = ""
    def __init__(self, name):
        self._name = name

    def update(self, subject):
        print "ConcreteObserver: %s receive data: %d"%(self._name, subject.data)



#test

subject = ConcreteSubject()
observerA = ConcreteObserver('A')
observerB = ConcreteObserver('B')
subject.attach(observerA)
subject.attach(observerB)
subject.data = 9
subject.data = 5
subject.data = 2
subject.data = 7
subject.detach(observerA)
subject.detach(observerB)


'''
输出结果：
    Subject: Attached an observer.
    Subject: Attached an observer.
    Subject Set Data: 9
    Subject: Notifying observers...
    ConcreteObserver: A receive data: 9
    ConcreteObserver: B receive data: 9
    Subject Set Data: 5
    Subject: Notifying observers...
    ConcreteObserver: A receive data: 5
    ConcreteObserver: B receive data: 5
    Subject Set Data: 2
    Subject: Notifying observers...
    ConcreteObserver: A receive data: 2
    ConcreteObserver: B receive data: 2
    Subject Set Data: 7
    Subject: Notifying observers...
    ConcreteObserver: A receive data: 7
    ConcreteObserver: B receive data: 7
    Subject: Detached an observer.
    Subject: Detached an observer.
'''