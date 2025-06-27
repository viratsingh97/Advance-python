'''a=2
b=4
s=a+b
print(s)
name="Satyam"
age=21
print(name)
print("My name is %s and i am %d year old"%(name,age))
#str.formate
print("my name is {}  and i am {} years old".format(name,age))
print("roll no: {0}, name:{1}".format(101,"satyam"))
marks=92.4567
print("marks: {:.2f}".format(marks))
print(f"name:{name},age: {age}")
with open("output.txt","w") as file:
         print("Hello file my name is virat",file=file)'''


'''
#combined example
print("hello ",end="")#the next output print in same line
print("world")
#type casting
a="10"
b=int(a)
print(b+5)
print(type(b+5))'''
'''
print("my","name","is","Virat",sep="~")#seperator
per=int(input("Enter your marks"))
if per>33:
         print("pass")
else:
        print("fail")         '''
'''
marks=int(input("Enter marks"))
if marks>=90:
         print("grade a")
elif marks>=75:
        print("grade b")
elif marks>=60:
        print("grade c")
else:
        print("grade f")        '''
'''
a=int(input("first no:"))
b=int(input("second no:"))
c=int(input("third no:"))
if a>b:
         if a>c:
                 print("a is greatest")
         else:
                 print(b,"is greatest")        
else:
        if b>c:
                print(b,"is greatest")
        else:
                print(c,"is greatest")                        '''
'''
y=int(input("enter the year"))
if (y%4==0 and y%100!=0) or y%400==0:
         print("leap year")
else:
        print("not leap year")         '''


'''
i=5
while i>=0:
         print(i)
         i-=1

#sum till n 
num=int(input("Enter num"))
sum=0
while num>0:
        sum=sum+num
        num=num-1  
print("the sum is ",sum)      
'''
'''
#for loop
for i in range (1,11,2):
        print(i)'''

'''
for i in range (1,11):
         print("2 * ",i,"=",2*i)'''
'''
l=[1,2,5,8]
sum=0
for val in l:
         sum+=val
print("The sum is ",sum)         '''
'''
for i in range (1,10,2):
        print(i)'''
'''
for i in range(1,5):
        for j in range(i):
                print(i,end=" ")
        print()        '''

'''
for i in range(1,5):
        for j in range(i):
                print(i,end=" ")
                i+=1
        print()  '''
'''
for i in range (1,6):
         if i==3:
                 continue
         print(i)'''
'''
number=[1,2,3,4,5,6,7,8,9]
num_sum=0
count=0
for x in number:
         num_sum+=x
         count+=1
         if count==5:
                 break       
print("sum of first",count,"inte is: ",num_sum)     '''


'''
c="Noida"
print(c[0])#N
for i in c:
         print(i,end="")
print()         
print(c[::-1])   #reverse
'''
'''
str="pyThOn"
print(str[-6:-2])
print(str.capitalize())
print(str.split())
l=[1,2,3,4]
sq=[x**2 for x in range(1,6)]
print(sq)

l[0]="one"
print(l)
t=(1,2,3,4)
print(t[::2])
print(t[:1])
print(t[-3:-1])
l=list(t)
l[0]="one"
t=tuple(l)
print(t)
'''
'''
t=("virat","varchasva","vivek")
if "satyam" in t:
         print("yes")
else:
        print("no")         
thisdict={"brand":"maruti","model":"swift","year":1987}
print(thisdict)
print(thisdict["brand"])
print(thisdict.get("brand"))#same as above'''


'''
name,age,marks=["virat",10,24]
print(F"my name is {name} and i am {age} years old. i got {marks} marks")
def func(a,b,c,d):
         print(a,b,c,d)
l=[1,2,3,4]
func(*l)

def stu(*args):#when no. of input is undefined then we use *
        print(args)
stu("alice",20,"cse")        

data=("virat",67,"cse ds")
name,roll_no,branch=data#unpacking
print(name,roll_no,branch)


a,*b=data
print(a)
print(b)#print rest of them

def fsum(a,b):
        result=a+b
        return result
x=5
y=6
z=fsum(x,y)
print(z)
'''

'''
def add(a,b):
         return a+b
result=add(5,3)
print("sum is", result)


def stud(name,age):
        print("name:",name)
        print("age:",age)
stud(age=20,name="virat") 
'''  

'''
#variable length positional argument
def sum(num1,*num):
         result=num1
         for i in num:
                 result+=1
         return result
r=sum(10,20,30)
print(f"The sum of number is {r}")
r=sum(10,20,30,40,50)
print(f"The sum of number is {r}")

#variable length keyword argument
def my_fun(**name):#number of keyword is not defined
        print(f"the first name is {name['fname']} and last name is {name['lname']}")
my_fun(fname="virat",lname="singh")        
'''

'''
def tot(*marks):
        print("total:",sum(marks))
tot(90,20,34)        
'''

'''
#recursion
def fact(num):
         if num==0:
                 return 1
         else:
                 return num*fact(num-1)
n=int(input("Enter the number:"))
f=fact(n)
print("the factorial of",n,"is",f)  

'''


'''
#lambda function(naless function used for short time)
result=lambda n1,n2,n3:n1+n2+n3
print(result(10,20,30))
print(result(5,1,4))
#filter() map()
num=[10,20,30,40,50]
x=list(filter(lambda x:x>20,num))
print(x)
def square(x):
         return x*x
y=list(map(square,num))
print(y)
def cube(x):
        return x**3
z=list(map(cube,num))
print(z) '''       



'''
#reduce function
from functools import reduce
def add(x,y):
         return x+y
num=[1,2,3,4,5]
result=reduce(add,num)
print("sum is: ",result)
print(reduce(lambda x,y:x if x>y else y,num))
'''


'''

#advanced python
#class and object
class greeting:
         message="Hello world"
         def say_hello(self):
                 print(self.message)
greet=greeting()#object
greet.say_hello()   

#__init__() method used to intialized the variable
class person:
        def __init__(self,name,age,gender):
                self.name=name
                self.age=age
                self.gender=gender
        def show_details(self):
                print("the name is {} age is {}  and gender is {}".format(self.name,self.age,self.gender))
p1=person("nitin",35,"male")
p1.show_details()                        


#
class car:
        wheel=4
        def __init__(self,name):
                self.name=name
mercedes=car("mercedes")
print(mercedes.wheel)
print(car.wheel)
print(mercedes.name)

#
class employee:
        office_name="amazon"
        def __init__(self,name,designation):
                self.name=name
                self.designation=designation
        def show_details(self):
                print(F"company name:{employee.office_name}\n name:{self.name}\n designation:{self.designation}") 

p=employee("mohit","developer")
p.show_details()


#
class number:
        even=[]
        odds=[]
        def __init__(self,num):
                self.num=num
                if num%2==0:
                        number.even.append(num)
                else:
                        number.odds.append(num)
n1=number(21)   
n2=number(32)
n3=number(43)
n4=number(54)     
print("Even number are:",number.even)
print("odds number are",number.odds) 

#
class personn:
        def __init__(self,name,age):
                self.name=name
                self.age=age
        def __str__(self):
                return f"The name is {self.name} and age is {self.age} "  
 '''             

#class method
'''
class my_class:
         @classmethod
         def func_name(sls,arguments):
                 return value'''


'''
#
class Student:
    counter = 0  # class variable to count number of objects

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.counter += 1

    def msg(self):
        print("Hello " + self.name + ", you got", self.marks, "% marks")

    @classmethod
    def object_count(cls):
        return cls.counter

# Creating student objects
s1 = Student("Virat", 85)
s2 = Student("Raj", 90)

# Calling instance method
s1.msg()
s2.msg()

# Calling class method
print("Total Student Objects Created:", Student.object_count())'''

'''
class mathoperation:
         @staticmethod
         def add(a,b):
                 return a+b
         @staticmethod
         def sub(a,b):
                 return a-b
obj=mathoperation()
result_add=obj.add(10,5)
result_sub=obj.sub(10,5)
print(f"addition:{result_add}")
print(f"substraction:{result_sub}")


#
class addition:
        first=0
        second=0
        answer=0
        def __init__(self,f,s):
                self.first=f
                self.second=s
        def display(self):
                print("First number = ",self.first)
                print("seconf number =",self.second)
                print("addition of two numbers = ",self.answer)
        def calculated(self):
                self.answer=self.first+self.second
obj=addition(1000,2000)
obj.calculated()
obj.display()'''           


'''
class person:
         def __init__(self,name,age):
                 self.name=name
                 self.age=age
         def display(self):
                 print("name is {} and age is {}".format(self.name,self.age))
o=person("virat",20)
o.display()                         


class car:
        def __init__(self,brand,price):
                self.brand=brand
                self.price=price
        def display(self):
                print("the car brand is {} and price is {}".format(self.brand,self.price))
o1=car("maruti",999999)
o2=car("tata",88888)
o1.display()
o2.display()                        

class bank_account:
        def __init__(self,name,balance):
                self.name=name
                self.balance=balance
        def display(self):
                print("the acooutant name is {} and balance is {}".format(self.name,self.balance)) 
o3=bank_account("virat",9999)
o3.display()  ''' 
'''
class rectangle:
        def __init__(self,len,bre):
                self.len=len
                self.bre=bre
        def area(self):
                print("the area is {}".format(self.len*self.bre))
re=rectangle(5,4)
re.area()'''
'''
class circle:
        def __init__(self,radius):
                self.radius=radius
        def area(self):
                print("the area is {}".format(3.14*self.radius*self.radius))
        def circum(self):
                print("the circumerence is {}".format(2*3.14*self.radius))
ar=circle(5)
ar.area()
ar.circum()                                
'''


#mAGIC  method or dunder
'''
class mass:
         def __init__(self,kg=0,g=0):
                 self.kg=kg+g//1000
                 self.g=g%1000
         def __add__(self,other):
                 tkg=self.kg+other.kg
                 tg=self.g+other.g

                 if tg>=1000:
                         tkg+=tg//1000
                         tg=tg%1000
                 return mass(tkg,tg)
         def __repr__(self):
                 return f"{self.kg} kg and {self.g} g"
mass1=mass(2,500)
mass2=mass(1,600)
m=mass1+mass2
print(m)  



class student:
        def __init__(self,m1,m2):
                self.m1=m1
                self.m2=m2
        def __gt__(self,other):
                r1=self.m1 + self.m2
                r2=other.m1 + other.m2 
                if r1>r2:
                        return True  
                else:
                        return False
s1=student(20,60)
s2=student(100,509)
if s1>s2:
        print("s1 is greater") 
else:
        print("s2 is greater") '''  

'''
class person:
         def __init__(self,name,age):
                 self.name=name
                 self.age=age
         def __str__(self):
                 return F"The name is {self.name} and age is {self.age}"
p=person("mohit",54)
print(p)                 

'''
'''
class person:
         def __new__(self):#assign before init method
                 print("this is new mwthod")
                 self.__init__(self)
         def __init__(self):
                 print("init method")
p=person()     '''

'''fraction class with custom magic method . we will create
a fumction class that support addition, comarion
and string representation'''

'''
import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def simplify(self):
        common_divisor = math.gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __repr__(self):
        return f'{self.numerator}/{self.denominator}'

# Example usage
f1 = Fraction(1, 2)
f2 = Fraction(2, 3)
f3 = f1 + f2

print(f3)         # Output: 7/6
print(f1 == f2)   # Output: False
print(f1 < f2)    # Output: True
'''
'''
class myclass:
    def __init__(self,value):
        self.value=value
def create_obj(value):
    return myclass(value)
obj=create_obj(10)
print(obj.value)    
'''
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def combine(self, other):
        total_area = self.area() + other.area()
        new_width = self.width  # keeping width same as self
        new_height = total_area / new_width
        return Rectangle(new_width, new_height)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# Example usage
r1 = Rectangle(4, 5)   # Area = 20
r2 = Rectangle(3, 6)  # Area = 20
r3 = r1.combine(r2)    # Area = 40, width = 4 → height = 40 / 4 = 10

print(r3)  # Output: Rectangle(width=4, height=10.0)
'''

"""count=0        
x=int(input("enter the number"))
for i in range(1,x+1):
         if x%i==0:
                 count+=1
         else:
                 continue        
                     
if count>2:
        print(" not prime no:")
else:
        print(" prime no:")   """  

"""
#oops
#inheritence
class animal:
         def eat(self):
                 print("this animal eat food")
class dog(animal):
        def bark(self):
                print("dog bark")
d=dog()
d.eat()
d.bark()

#multi step
class person:
        def basic_info(self):
                print("This is a person")
class employee(person):
        def job_info(self):
                print("This is an employee")
class manager(employee):
        def manage(self):
                print("This person manages a team")
m=manager()
m.basic_info()
m.job_info()
m.manage() 
               """                                

"""
#multiple inheritence
class father:
         def skills(self):
                 print("knows gardening")
class mother:
        def skills(self):
                print("knows cooking")
class child(father,mother):
        def my_skill(self):
                print("both skills")
c=child()
c.skills()
c.my_skill()    

#hierarichal inherit...
class animal:
        def eat(self):
                print("Eating")
class dog(animal):
        def bark(self):
                print("barking")
class cat(animal):
        def meow(self):
                print("meowuing")
d=dog()
c=cat()
d.eat()
d.bark()
c.eat()                                                


#
class BankAccount:
    def __init__(self, balance):  # ← double-underscore on both sides
        self.balance = balance

    def calculate_interest(self):
        print("No interest for base bank account.")

class SavingAccount(BankAccount):
    def calculate_interest(self):
        interest = self.balance * 0.04  # 4% interest
        print(f"Saving Account Interest: ₹{interest:.2f}")

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        interest = self.balance * 0.02  # 2% interest
        print(f"Current Account Interest: ₹{interest:.2f}")

# Example usage
s = SavingAccount(10000)
s.calculate_interest()  # Output: Saving Account Interest: ₹400.00

c = CurrentAccount(10000)
c.calculate_interest()  # Output: Current Account Interest: ₹200.00
class BankAccount:
    def __init__(self, balance):  # ← double-underscore on both sides
        self.balance = balance

    def calculate_interest(self):
        print("No interest for base bank account.")

class SavingAccount(BankAccount):
    def calculate_interest(self):
        interest = self.balance * 0.04  # 4% interest
        print(f"Saving Account Interest: ₹{interest:.2f}")

class CurrentAccount(BankAccount):
    def calculate_interest(self):
        interest = self.balance * 0.02  # 2% interest
        print(f"Current Account Interest: ₹{interest:.2f}")

# Example usage
s = SavingAccount(10000)
s.calculate_interest()  # Output: Saving Account Interest: ₹400.00

c = CurrentAccount(10000)
c.calculate_interest()  # Output: Current Account Interest: ₹200.00"""

#method and data binding is encapsulation
#access modifier(method of encapsulation)
"""_ protected
__ private (only parent class)"""

#polimorphism
"""method overriding(methode and argument same)
method overloading(method same arg differe)
duck typing(alg alg class k same method)
operator overriding()"""

#protected access modifier
"""class student:
         _name=None
         _roll=None
         _branch=None
         def __init__(self,name,roll,branch):
                 self._name=name
                 self._roll=roll
                 self.branch=branch
         def _displayinfo(self):
                 print("Roll no: ",self._roll)
                 print("branch:",self._branch)
class learnowx(student):
        def __init__(self,name,roll,branch):
                student.__init__(self,name,roll,branch)
        def displaydetaild(self):
                print("Name",self._name)
                self._displayinfo()     
o=learnowx("virat",67,"DS")
o._displayinfo()
o.displaydetaild()"""

#private access modi...
"""class student:
         __name=None
         __package=None
         def __init__(self,name,package):
                 self.__name=name
                 self.__package=package
         def __display(self):
                 print("name: ",self.__name)
                 print("package: ",self.__package)
         def accessprivate(self):
                 self.__display()
o=student("virat","25 LPA")
o.accessprivate()"""  

#abstract class(we hide uneccessary setails)
# it is implement through subclass
# derived from abc module
# @abstractmethod is used

"""from abc import ABC , abstractmethod
class myabstract(ABC):
         @abstractmethod
         def disp(self):
                 pass
         def show(self):
                 print("Concrete Method")                               
"""

"""from abc import ABC , abstractmethod
class computer(ABC):
         @abstractmethod
         def process(self):
                 pass
         def msg(self):
                 print("Computer is an electronic device")
class laptop(computer):
        def process(self):
                print("Executing laptop process")
class desktop(computer):
        def process(self):
                print("Executing desktop process")
c1=laptop()
c2=desktop()
c1.process()
c2.msg()        """   


"""from abc import ABC , abstractmethod
class shape(ABC):
         @abstractmethod
         def __init__(self,radius):
                 self.radius=radius
         def disp(self):
                 pass
class perim(shape):
        def __init__(self,radius):
                shape.__init__(self,radius)
        def disp(self):
                print("the permi is",2*3.14*self.radius)
class area(shape):
        def __init__(self,radius):
                shape.__init__(self,radius)
        def disp(self):
                print("the area is",3.14*self.radius*self.radius)
o=area(4)
o.disp()   
o1=perim(4)
o1.disp() """             


"""class person:
         def __init__(self,walk):
                 self.walk=walk
         def display(self):
                 print("he is walking")
class employee(person):
        def __init__(self,walk,work):
                self.work=work
                person.__init__(self,walk)
        def display(self):
                print("The employee can walk and work")
class manager(employee):
        def __init__(self,walk,work,manage):
                self.manage=manage 
                employee.__init__(self,walk,work)
        def display(self):
                print("manager can walk work and manage")
o=manager("","","")
o.display()   
o1=person("")
o1.display() """     

"""
class shape():
         def __init__(self,rad):
                 self.rad=rad
         def disp(self):
                 print("the area is",self.rad*self.rad*3.14)        
class circle(shape):
        def __init__(self,rad):
                shape.__init__(self,rad)
        def disp(self):
                print("this is child class area",3.14*self.rad,self.rad)
class square(shape):
        def __init__(self,rad):
                shape.__init__(self,rad)
        def disp(self):
                print("this is  square class area")

o=square(5)
o.disp()

o2=shape(7)
o2.disp()"""


#closure function(used in nested func)
"""def outerfunc(text):#inclosing func
         def innerfunc():#closure func
                 print(text)
         return innerfunc
myfunc=outerfunc("Hey! i am virat singh")
myfunc()#variable is used as function  call


def number(x,y):
        def inumber():
                print("addition",x+y)
                print("subtraction",x+y)
                print("multiplication",x*y)
        return inumber
m=number(10,5)
m()

#
def mcount():
        count=0
        def counter():
                nonlocal count
                count+=1
                return count
        return counter
c1=mcount()
print(c1())#1
print(c1())#2
c2=mcount()
print(c2())#1

#decorator(designed pattern in which we add new func in structure without any change)
def decor(func):
        def inner():
                print("________")
                func()
                print("________")
        return inner
def msg():
        print("Python python")
ms=decor(msg)
ms()       """        

"""#or
def decor(func):
        def inner():
                print("________")
                func()
                print("________")
        return inner
@decor
def msg():
        print("Python python")
msg()

"""
#
"""from datetime import datetime
def not_duerung_night(func):
        def inner():
                if 7 <=datetime.now().hour <22:
                        func()
                else:
                        print("Sorry unable to play in night")
        return inner
@not_duerung_night
def music():
        print("playing music")
music()                                
"""


"""
def repeat(n):
         def decor(func):
                 def wrapper():
                         for _ in range(n):
                                 func()
                 return wrapper
         return decor
@repeat(3)
def cheer():
        print("Hurry")
cheer()  """      


"""def decor1(func):
        def inner():
                x=func()
                return inner
def decor(func):
        def inner():
                x=func()
                return 2*x
        return inner
@decor1
@decor
def num():
        return 10"""


#generator
"""def generate_num():
         for i in range(1,11):
                 yield i
#create generator                 
num_gen=generate_num()
print(type(num_gen))#class 'generator'
for i in num_gen:#print number from generator
        print(i)"""


#
"""def is_prime(num):
        if num<2:
                return False
        for i in range(2,int(num**0.5)+1):
                if num%i==0:
                        return False
        return True
def gene_prime(start,end):
        for num in range(start,end+1):
                if is_prime(num):
                        yield num
prime_gener=gene_prime(1,50)
for prime in prime_gener:
        print(prime,end=',') """ 

# 
"""def rev(my_str):
        l=len(my_str)
        for i in range(l -1,-1,-1):
                yield my_str[i]
for char in rev("Hello Virat"):
        print(char,end="")   """


#
"""def my_gen(x):
        while(x>0):
                if x%2==0:
                        yield x,"Even"
                else:
                        yield x,"odd"
                x-=1
for i in my_gen(8):
        print(i)    """

#coroutine
"""def print_name(prefix):
        print("searching prefix {}".format(prefix))
        while True:
                name=(yield)
                if prefix in name:
                        print("{} is present in {}".format(prefix,name))
c=print_name("Dear")
c.__next__()
c.send("Virat")
c.send("Dear virat")"""

#
"""def print_name(prefix):
         print("searching prefix:{}".format(prefix))
         try:
                 while True:
                         name=(yield)
                         if prefix in name:
                                 print("{} is present in {}".format(prefix,name))
         except GeneratorExit:
                 print("closing coroutine!")
c=print_name("Dear")
c.__next__()
c.send("virat")
c.send("dear virat")
c.send("Dear virat")
c.close()  """    

#Iterator
"""class mynum:
         def __iter__(self):
                 self.a=1
                 return self
         def __next__(self):
                 x=self.a
                 self.a+=1
                 return x
ob=mynum()
myiter=iter(ob)
print(next(myiter)) 
print(next(myiter)) 
print(next(myiter)) 
print(next(myiter))"""

#declarative
"""n=[1,2,3,4,5]
even=list(filter(lambda x:x%2==0,n))
print(even) 
"""
"""
from functools import reduce
n=[1,2,3,4,5]
total=reduce(lambda x,y:x+y,n)
print(total) """


#      GUI
"""from tkinter import *
window=Tk()#create main window
window.title("Hello Amazon")
window.geometry('800x600')#width*length
label=Label(window,text="Hello! virat you are hired",font=("Arial Bold",20))
label1=Label(window,text="Congrats for your bright future",font=("Italic",17))
label2=Label(window,text="Your salary is 42 LPA",font=("Italic",15))
label.pack()
label1.pack()
label2.config(bg="pink",fg="red")
label2.pack(pady=5,ipady=15,ipadx=15)#to increase the size of backgroud pady= manage the gapping
label3=Label(window,text=" be happy",font=("Italic",15))
label3.pack(side=LEFT)
window.mainloop()     """  


"""from tkinter import *
import tkinter as tk
window=Tk()
window.title("Hello")
def button_click():
         button.config(text="Khul gya! swagat hai aapka",bg="pink",fg="black")
button=Button(window,text="Khul ja sim sim",command=button_click,font=("Italic",20))
button.pack(padx=20,pady=20)
window.geometry('800x400')
scale=tk.Scale(window,from_=0,to=100,orient=tk.HORIZONTAL)#makes a scale
Spinbox=tk.Spinbox(window,from_=0,to=10)
Spinbox.pack()
scale.pack()
check_var=tk.BooleanVar()
Checkbutton=tk.Checkbutton(window,text="check me",variable=check_var,font=("Bold",20))
Checkbutton.pack()
radio_var=tk.StringVar()
radiobutton1=tk.Radiobutton(window,text="male",variable=radio_var,value="male")
radiobutton2=tk.Radiobutton(window,text="female",variable=radio_var,value="female")
radiobutton1.pack()
radiobutton2.pack()
listbox=tk.Listbox(window)#
listbox.insert(1,"option 1")
listbox.insert(2,"option 2")
listbox.insert(3,"option 3")
listbox.pack()
window.mainloop() 
"""

"""import tkinter as tk
from tkinter.ttk import Combobox

window = tk.Tk()
window.title('Combobox Example')
window.geometry('800x200')

def combobox_selected(event):
    selected_value = combobox.get()
    label.config(text=f"Selected: {selected_value}")
label = tk.Label(window, text="Select an option:")
label.pack(padx=20, pady=10)
options = ["Option 1", "Option 2", "Option 3"]
combobox = Combobox(window, values=options)
combobox.pack(padx=20, pady=10)
combobox.bind("<<ComboboxSelected>>", combobox_selected)

window.mainloop()"""


#
# Program 11: Entry Widget
"""import tkinter as tk

window = tk.Tk()
window.title("Entry Example")
window.geometry('800x200')

entry = tk.Entry(window)
entry.pack()

window.mainloop()"""

#grid
# Example: Create a login sample page using grid.

"""from tkinter import *

# Create the main window
window = Tk()
window.title("Login Example")

def submit_clicked():
    result_label.config(text="Good Job")

# Username label and entry
username_label = Label(window, text="Username")
username_label.grid(row=0, column=0, padx=10, pady=5)

username_entry = Entry(window)
username_entry.grid(row=0, column=1, padx=10, pady=5)

# Password label and entry
password_label = Label(window, text="Password")
password_label.grid(row=1, column=0, padx=10, pady=5)

password_entry = Entry(window)
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Submit button
submit_button = Button(window, text="Submit", command=submit_clicked)
submit_button.grid(row=2, column=0, columnspan=2, pady=20)

# Label to show the result
result_label = Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

window.mainloop()"""

#
# Example: Date Picker
# First, install the tkcalendar module:
"""
from tkinter import *
from tkcalendar import DateEntry

root = Tk()
root.title("Date Picker Example")
root.geometry('800x200')

# Create a DateEntry widget
date_entry = DateEntry(root)
date_entry.pack()

root.mainloop()
"""
#create any shape
"""import tkinter as tk

root = tk.Tk()
root.title("Canvas Example")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

canvas.create_line(0, 0, 200, 100)
canvas.create_rectangle(50, 50, 150, 150, fill="pink")
canvas.create_oval(0,0,100,150,fill="yellow")
root.mainloop()"""

#create calculator
"""from tkinter import *
root = Tk()
root.geometry("400x600")
root.title("Calculator by virat")
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="licita 40 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)
f=Frame(root,bg="grey")
b=Button(f,text="9",padx=28,pady=22,font="lucida 35 bold")
b.bind("<Button-1>",click)
b.pack(side="left",padx=18,pady=12)
b=Button(f,text="8",padx=28,pady=22,font="lucida 35 bold")
b.pack(side="left",padx=18,pady=12)
b=Button(f,text="7",padx=28,pady=22,font="lucida 35 bold")
b.pack(side="left",padx=18,pady=12)
f.pack()
root.mainloop()"""

#numpy
"""import numpy as np
print(np.__version__)
my_list=[1,2,3]
np.array(my_list)
print(np.array(my_list))

l=[[1,2,3],[4,5,6],[7,8,9]]
print(np.array(l))

#arange
x=np.arange(0,10)
print(x)
y=np.arange(0,11,2)
print(y)
#zeros and ones
z=np.zeros(3)
z=np.zeros((5,5))
print(z)
print(np.ones(4))

#line space(print evenly spaced numbered over a specified interval)
x1=np.linspace(0,10,50)
print(x1)

#eye(digonly 1  baki sb zero of n*n)
print(np.eye(5))

#random(return a sample or samples from the standard normal distribution unlike rand which is uniform)
print(np.random.rand(5,5))

#randint
print(np.random.randint(1,100))#return random inte
print(np.random.randint(1,100,15))#return 15 random int

#reshape
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr.reshape(3,3))
print(arr.max())
print(arr.argmax())#max -1
print(arr.min())
print(arr.argmin())#min-1
#dtype
print(arr.dtype)#int 64

#numpy inndexing and selection
print(arr[1:4])#start from 1 index and stop at 3

#broadcasting
#p=arr[0:5]=100 #change the value 0 to 4 index to 100
print(arr)

#slicing 
sc=arr[0:4]
print(sc)

#copy 
cp=arr.copy()
print(cp)

arr3=np.array([[1,2,3],[4,5,6],[7,8,9]])
sc1=arr3[2][2]#nested slicing
print(sc1)

print(arr3>3)
#arithimetic ope"""


#pandas library
#store data in tabular form 2D,
"""import pandas as pd
import numpy as np
label=['a','b','c']
l=[10,20,30]
arr=np.array([10,20,30])
d={'a':10,'b':20,'c':30}
print(pd.Series(d))
se=pd.Series([1,2,3,4],index=['usa','germany','USSR','japan'])
print(se)
se2=pd.Series([1,2,3,4],index=['usa','germany','Italy','japan'])
print(se['japan']) #4
data={
         "roll no":[10,11,12,13,14],
         "name":["virat","varchas","vivek","mohan","sohan"],
         "age":[17,19,18,17,19],
         "marks":[85,92,98,76,72],
         "Grade":["A","C","B","A","B"]

}  
stu=pd.DataFrame(data)
print(stu)   """

"""
  roll no     name  age  marks Grade
0       10    virat   17     85     A
1       11  varchas   19     92     C
2       12    vivek   18     98     B
3       13    mohan   17     76     A
4       14    sohan   19     72     B
"""

"""import pandas as pd
import numpy as np
from numpy.random import randn 
df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(), columns='w x y z'.split())
print(df['w'])#datatype
df['new']=df['w']+df['y']#add
print(df)
df=df.drop('new',axis=1)#remove coloumn
print(df)
print(df.loc['A'])#location and data type
print(df.iloc[2])#index 2 value and data type
print(df.loc[['A','B'],['w','y']])
print(df>0)#return true or false for every value
print(df<0)
print(df[df['w']>0])
print(df.reset_index())
r='CA MY BY OR CO'.split()
x=df['states']=r#add new coloumn
print(df)
df.set_index('states')
print(df)
import pandas as pd

ou = ['G1', 'G2', 'G1', 'G2', 'G2', 'G2']
in_ = [1, 2, 3, 1, 2, 3]  # 'in' is a Python keyword, so use 'in_' instead

hier = list(zip(ou, in_))
index = pd.MultiIndex.from_tuples(hier)

print(index)
#df.index.names=['Group','Num']
df1=pd.DataFrame({'A':[1,2,np.nan],
                  'B':[5,np.nan,np.nan],
                  'C':[1,2,3]})                
print(df1)
df1.dropna(axis=1)#jis coloumn me na hoga remove
#df1.dropna() 
o=df1.fillna(value='FILL VALUE')#fill value at nan
print(o)"""

"""import pandas as pd

data = {
    "company": ["goog", "goog", "msft", "msft", "fb", "fb"],
    "Person": ["sam", "charlie", "amy", "varchita", "carl", "sarah"],
    "sales": [345, 789, 987, 567, 875, 890]
}

df = pd.DataFrame(data)

# Grouping by 'company'
by_comp = df.groupby("company")

# Display the original DataFrame
print(df)

# Applying aggregation functions
print("MAx is:\n",by_comp.max())
print("min is:\n",by_comp.min())
print("\n",by_comp.count())
print("\n",by_comp.describe().transpose())

        """     


#
"""import pandas as pd
import numpy as np
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
}, index=[0, 1, 2, 3])

df2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7']
}, index=[4, 5, 6, 7])

df3 = pd.DataFrame({
    'A': ['A8', 'A9', 'A10', 'A11'],
    'B': ['B8', 'B9', 'B10', 'B11'],
    'C': ['C8', 'C9', 'C10', 'C11'],
    'D': ['D8', 'D9', 'D10', 'D11']
}, index=[8,9,10,11])
print(df1,"\n")
print(df2,"\n")
print(df3,"\n")                          
print(pd.concat([df1,df2,df3]),"\n")
print(pd.concat([df1,df2,df3],axis=1),"\n")
"""


#
"""import pandas as pd

left = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

right = pd.DataFrame({
    'key': ['K0', 'K1', 'K2', 'K3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

print(left, "\n")
print(right, "\n")

# Inner join on 'key'
print(pd.merge(left, right, how='inner', on='key'))  # Merges only matching keys

# Outer join on 'key' (corrected from ['key1','key2'] to 'key')
re = pd.merge(left, right, how='outer', on='key')
print(re)
"""
"""
import pandas as pd

df = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [444, 555, 666, 444],
    'col3': ['abc', 'def', 'ghi', 'xyz']
})

df.head()
print(df['col2'].unique())#display the unique values
print(df['col2'].nunique())#number of different values
print(df['col2'].value_counts())#count perticular values how many times it comes

"""


"""
import pandas as pd

left = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B2', 'B2']
}, index=['K0', 'K1', 'K2'])

right = pd.DataFrame({
    'C': ['C0', 'C2', 'C3'],
    'D': ['D0', 'D2', 'D3']
}, index=['K0', 'K2', 'K3'])

result = left.join(right)
print(result)

print(right.join(left))
print(left.join(right,how='outer'))#combine both
"""
"""

"""

#
"""import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,8])
ypoints=np.array([3,10])
plt.plot(xpoints,ypoints,'o')#"o" remove line only show start and end point
plt.show()"""


#
"""import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,2,6,8,10,15,18,20])
ypoints=np.array([3,8,13,4,32,12,2,4])
plt.plot(xpoints,ypoints)#"o" remove line only show start and end point
plt.show()
"""

#
"""import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10,5,7])
plt.plot(ypoints)#y default it takes 0 for x axis
plt.show()"""

#
"""import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10,5,7])
plt.plot(ypoints,marker='o')#show points
plt.show()
"""

#
"""import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10,5,7])
plt.plot(ypoints,'o:r')#doted line with red color
plt.show()"""

#
"""import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10,5,7])
plt.plot(ypoints,marker='o',ms=20,mec='r')#ms gives the size of point and mec color the outer line
plt.show()
"""

#mfc marker face color mec marker rdge colour
"""import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10,5,7])
plt.plot(ypoints,marker='o',ms=20,mfc='r',mec='r')#mfc cololur the whole point
plt.show()
"""
#
"""import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10,5,7])
plt.plot(ypoints,linestyle="dashed")#mfc cololur the whole point
plt.show()

"""

#
"""import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10,5,7])
plt.plot(ypoints,linestyle="dotted")#mfc cololur the whole point
plt.show()"""

#
"""import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10,5,7])
plt.plot(ypoints,linestyle="dotted",color="r",marker='o',mec='g',mfc='g',ms=10)#dashed line color
plt.show()"""

#
"""import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,8,1,10,5,7])
y1points=np.array([9,10,19,2,12])
plt.plot(ypoints,linewidth=10,color='g')
plt.plot(y1points,linewidth=20,color='r')
plt.show()"""

#labels for x and y axis
"""import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])
y1points = np.array([9, 10, 19, 2, 12, 6])  # Now 6 values

plt.plot(ypoints, y1points)
plt.title("sports watch data",loc="right")#title goes at right by default in center
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()"""

#
"""import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])
y1points = np.array([9, 10, 19, 2, 12, 6])  # Now 6 values

plt.plot(ypoints, y1points)
plt.title("sports watch data",loc="right")#title goes at right by default in center
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.grid(axis='x')#add grid in graph(we give axis if we want in only perticular axis)
plt.show()
"""

#subplot
"""import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([0,1,2,3])
y1points = np.array([3,1,8,10])  # Now 6 values

plt.subplot(1,2,1)
plt.plot(ypoints,y1points)
plt.title("Growth of infosys")
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("Growth of wipro")
plt.suptitle("Growth of compony")
plt.show()"""

#
"""import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])
y1points = np.array([9, 10, 19, 2, 12, 6])  # Now 6 values

plt.scatter(ypoints, y1points)#only show points
plt.title("sports watch data")
plt.ylabel("Calorie Burnage")
plt.show()"""

#two scatter in same fig
"""import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])
y1points = np.array([9, 10, 19, 2, 12, 6])  # Now 6 values

plt.scatter(ypoints, y1points)#only show points
y2points = np.array([3,56,7,4,3])
y3points = np.array([8,5,2,8,5])  # Now 6 values

plt.scatter(y2points, y3points)
plt.title("sports watch data")
plt.show()"""


#color of scatter
"""import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])
y1points = np.array([9, 10, 19, 2, 12, 6])  # Now 6 values
color=np.array(["red","green","blue","grey","pink","black"])
plt.scatter(ypoints, y1points,c=color)#only show points with different colors
plt.title("sports watch data")
plt.ylabel("Calorie Burnage")
plt.show()"""

#size of scat..
"""import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])
y1points = np.array([9, 10, 19, 2, 12, 6])  # Now 6 values
size=np.array([20,10,5,30,50,90])
plt.scatter(ypoints, y1points,s=size)#only show points with different colors
plt.title("sports watch data")
plt.ylabel("Calorie Burnage")
plt.show()"""

#Bar chart
"""import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Apple", "vegetable", "brinjal", "mango"])
y = np.array([3, 8, 1, 10])
colors = np.array(["red", "green", "blue", "yellow"])
plt.title("Consumption of  fruits and vege..")
plt.bar(x, y, color=colors)
plt.show()"""

#bar chart in y axis
"""import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Apple", "vegetable", "brinjal", "mango"])
y = np.array([3, 8, 1, 10])
colors = np.array(["red", "green", "blue", "yellow"])
plt.title("Consumption of  fruits and vege..")
plt.barh(x, y, color=colors)#now it show hor
plt.show()
"""

#
"""import matplotlib.pyplot as plt
import numpy as np

x = np.array(["Apple", "vegetable", "brinjal", "mango"])
y = np.array([3, 8, 1, 10])
colors = np.array(["red", "green", "blue", "yellow"])
plt.title("Consumption of  fruits and vege..")
plt.bar(x, y,color=colors, width=0.1)#now it show hor
plt.show()"""

#histogram graph
"""import matplotlib.pyplot as plt
import numpy as np
x=np.random.normal(170,10,250)
plt.hist(x,color="red")
plt.show()
"""

#pie chart
"""import matplotlib.pyplot as plt
import numpy as np
y = np.array([3, 8, 5, 10])
le=np.array(["apple","strawberry","mango","grapes"])
co=np.array(["red","pink","yellow","green"])
plt.pie(y,labels=le,colors=co)
plt.show()
"""

#
"""import matplotlib.pyplot as plt
import numpy as np
y = np.array([3, 8, 5, 10])
le=np.array(["apple","strawberry","mango","grapes"])
co=np.array(["red","pink","yellow","green"])
myexplode=[0.2,0,0,0]#seperate from chart
plt.pie(y,labels=le,colors=co,explode=myexplode,shadow=True)
plt.show()"""

#legend
"""import matplotlib.pyplot as plt
import numpy as np
y = np.array([3, 8, 5, 10])
le=np.array(["apple","strawberry","mango","grapes"])
co=np.array(["red","pink","yellow","green"])
plt.pie(y,labels=le,colors=co)
plt.legend()#show the description which colors holds what parameter
plt.show()
"""
#nested graph
"""import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y = x ** 2

# Creates blank canvas
fig = plt.figure()

# Main and inset axes
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])  # inset axes

# Larger figure - Axes 1
axes1.plot(x, y, 'b')
axes1.set_xlabel('X_label_axes1')
axes1.set_ylabel('Y_label_axes1')
axes1.set_title('Axes 1 Title')

# Inset figure - Axes 2
axes2.plot(x, np.sqrt(x), 'r')
axes2.set_xlabel('X_label_axes2')
axes2.set_ylabel('Y_label_axes2')
axes2.set_title('Axes 2 Title')

plt.show()"""

#
"""import matplotlib.pyplot as plt
import numpy as np
fig=plt.figure()
x=np.array([0,1,2,3,4,5,6,7,8,9,10])
ax=fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label="x**2")
ax.plot(x,x**3,label="x**3")
ax.legend()
plt.show()"""

#
"""import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])

fig, ax = plt.subplots()

ax.plot(x, x+1, color="blue")       # half-transparent blue
ax.plot(x, x+2, color="purple")               # RGB hex code - purple shade
ax.plot(x, x+3, color="green")               # RGB hex code - yellow shade

plt.show()"""

#
"""import matplotlib.pyplot as plt
import numpy as np

# Define x data
x = np.linspace(0, 10, 100)

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Different Line Widths
ax.plot(x, x+1, color="red", linewidth=0.25)
ax.plot(x, x+2, color="red", linewidth=0.50)
ax.plot(x, x+3, color="red", linewidth=1.00)
ax.plot(x, x+4, color="red", linewidth=2.00)

# Different Line Styles
ax.plot(x, x+5, color="green", linestyle='-')   # solid
ax.plot(x, x+6, color="green", linestyle='-.')  # dash-dot
ax.plot(x, x+7, color="green", linestyle=':')   # dotted



# Custom Dash Pattern
line, = ax.plot(x, x+8, color="black", linewidth=1.50)
line.set_dashes([5, 10, 15, 10])  # [on, off, on, off] pattern

# Markers
ax.plot(x, x+9, color="blue", lw=1, linestyle='', marker='o')
ax.plot(x, x+10, color="blue", lw=1, linestyle='', marker='v')
ax.plot(x, x+11, color="blue", lw=1, linestyle='', marker='s')
ax.plot(x, x+12, color="blue", lw=1, linestyle='-', marker='*')

plt.show()"""


#Axis spines
"""import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6, 2))
ax.spines['bottom'].set_color('blue')
ax.spines['top'].set_color('blue')
ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(2)
ax.spines['right'].set_color("none")
ax.yaxis.tick_left()
plt.show()
"""
#
"""import matplotlib.pyplot as plt
import seaborn as sns
sns.displot([0,1,2,3,4,5])
plt.show()"""

#
