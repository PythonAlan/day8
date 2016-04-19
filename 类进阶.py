#!/usr/bin/env python3
#antuor:Alan

class Foo:
    """ 描述类信息，这是用于看片的神奇 """

    def func(self):
        pass

print (Foo.__doc__)

class Foo1:

    def __init__(self, name):
        self.name = name
        self.age = 18


obj = Foo1('wupeiqi') # 自动执行类中的 __init__ 方法
print(obj.name)
