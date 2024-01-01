class Arithmetic():
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def display(self):
        print('The sum of two numbers:',self.x+self.y)
x=int(input())
y=int(input())
j=Arithmetic(x,y)
j.display()