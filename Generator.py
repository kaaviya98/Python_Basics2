#square until secratain num
def square():
    i=1
    while (i*i)<100:   
         yield i*i
         i+=1
x=square()
for num in square():
         print(num)

#infinite sequence
def infinte_sequence():
    a=0
    while a<=100:
        yield a
        a+=1
for i in infinte_sequence():
    # if(i<=100):
         print (i)
#Fibonacci
def fib(maxi):
    a , b= 0 , 1
    while a<max:
         yield a
         a,b=b,a+b
max=50
x=fib(max)
num =fib(50)
# print(next(num))
# print(next(num))
# print(next(num))
for num in fib(max):
         print(num)

#check even or not using generator
list=[1,2,3,4,5,6,7,8,9,10]
def check_even(list):
    for i in list:
        if i%2==0:
            yield i
def check_odd(list):
    for j in list:
        if j%2!=0:
            yield j
print("The original list is : " + str(list))
print("Even are: ")
for i in check_even(list):
    print(i)
print("Odd are: ")
for j in check_odd(list):
    print (j)

#Use as boolen
String1 = " The are many geeks around you, geeks are known for teaching other geeks"
#String1=String1.split()
def check_present(String1):
     for i in String1:
        if i=="e":
                  yield i
c=0
for i in check_present(String1):
    c=c+1
print("The count of e is",c)



           