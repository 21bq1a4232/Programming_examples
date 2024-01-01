class Parent:
    def aaa1(self):
        print("hi iam parent")
class Child1(Parent):
    def aaa2(self):
        print("hi iam first child")
class Child2(Parent):
    def aaa3(self):
        print("hi iam second child")
object1 = Child1()
object2 = Child2()
object1.aaa1()
object1.aaa2()
object2.aaa1()
object2.aaa3()
