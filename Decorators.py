# fucntions as objects
import re


def tell(txt):
    return txt
s=tell("Hola")
print(s)
talk=tell
s1=talk("Annayasayo")
print(s1)

# passing fn as arg to another fn
def telling(text):
    return text.upper()
def taking(text):
    return text.lower()
def fun(func,x):
    g=func(x)
    return g
x=fun(telling,"How r u")
y=fun(taking,"Stupid")
print(x)
print(y)
# Functions can return another function
def create_adder(x):
	def adder(y):
		return x+y

	return adder

add_15 = create_adder(15)

print(add_15(10))

# #funtion inside another function(nested function)
# def add_welcome():
#     def welcome_to():
#         return "Welcome to"
#     return welcome_to()
# msg=add_welcome()
# print(msg+"TestPress")

#function decorator

def add_welcome(func):
    def inner(args):
        x= "Welcome "+func(args)
        print(x)
        return
    return inner
@add_welcome
def str(name):
    return name
str("Kaaviya")



#Decorator

def dec_div(func):
    def inner(*args,**kwargs):
            return func(*args,**kwargs)
    return inner
@dec_div
def div(a,b):
    if b==0:
            print("Ding!wrong i/p")
            return 
    else:
         return a/b
# obj_dec_div=dec_div(div)
# value1=obj_dec_div(15,3)
# print(value1)
# value=obj_dec_div(15,0)
# print(value)
val=div(15,3)
print(val)

#Chaining decorators
def decorator1(func):
    def inner1():
        print("%"*10)
        x=func()
        return(x*x)
        print("%"*10)
    return inner1

def decorator2(func):
    def inner():
        print("&"*10)
        x=func()
        return(x+x)
        print("&"*10)
    return inner    

@decorator1
@decorator2      
def val():
   return 5
print(val())
def attach_data(func):
       func.data = 4
       return func
  
@attach_data
def add (x, y):
    data=8
    return x + y+data
  
# Driver code
  
# This call is equivalent to attach_data()
# with add() as parameter
print(add(2, 3))
  
print(add.data)
print(add (3,4))