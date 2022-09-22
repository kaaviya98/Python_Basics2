# # fucntions as objects
# def tell(txt):
#     return txt
# s=tell("Hola")
# print(s)
# talk=tell
# s1=talk("Annayasayo")
# print(s1)

# # passing fn as arg to another fn
# def telling(text):
#     return text.upper()
# def taking(text):
#     return text.lower()
# def fun(func,x):
#     g=func(x)
#     return g
# x=fun(telling,"How r u")
# y=fun(taking,"Stupid")
# print(x)
# print(y)
# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
	def adder(y):
		return x+y

	return adder

add_15 = create_adder(15)

print(add_15(10))

