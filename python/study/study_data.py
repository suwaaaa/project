# 001:
# class person:
#     __slots__ = ["age", "name"]
#      # 这里限定类所创建的对象只能是列表里面的属性
# one = person()
# one.age = 18
# one.name = "a"

# 002:
class Person:
    def fun1(self):
        print(self)

    @classmethod
    def fun2(cls):
        print(cls)

    @staticmethod
    def fun3():
        print("静态方法")


# Person.fun1()   这个是错误的
Person.fun1(666)

fun = Person()
fun.fun1()
Person.fun2()
Person.fun3()
