import random

print(random.randint(1, 5))


n = 10


def add(a, b):
    return a+b


class Father():
    #双下划线开头和结尾,特殊属性方法
    #初始化方法
    def __init__(self, name):
        print(id(self))
        self.name = name

    def __del__(self):
        print('del')

    def show(self):
        print('name:', self.name)


# 双下划线 private 单下划线 protected 无 public
class Son(Father):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        print('name:', self.name, ',age:', self.age)


if __name__ == '__main__':
    s = Son('11', 30)
    s.show()

