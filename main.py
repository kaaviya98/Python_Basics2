import sys
sys.path.insert(0,"/home/kaaviya/Python_packages")
sys.path.insert(1,"/home/kaaviya/Python_packages/Shape/Triangle")
import main1 
from Equilateral import Equilateral
obj=Equilateral([5,5,5],6,8,[2,2,2])
area=obj.area()
perimeter=obj.perimeter()
check_equi=obj.is_Equilateral()
print(area)
print(perimeter)
print(check_equi)

# import os
# #os.mkdir("Shapes/Circle")
# #os.rename("\\wsl$\Ubuntu\home\kaaviya\Python_packages\main.py","\\wsl$\Ubuntu\home\kaaviya\Python_packages\main1.py")
# #os.rename("Equilateral","Equilateral_triangle")
# #Equilateral.is_Equilateral()
####lambda
max=lambda a,b:a if(a>b) else b
res = max(2,3)
print(res)
#non local 

def f():
    x=[]
    def x():
        nonlocal x
        x=[2]
        #print(x)
    x()
    return x
print(f())
#async keyword
import asyncio
from re import I
from unittest import FunctionTestCase

async def main():
    task=asyncio.create_task(next_one())
    return_value=await task
    print("A")
    #await asyncio.sleep(1)
    print("B")
    print(return_value)
    
#asyncio.run(main())
#asyn btw functions
async def next_one():
    #ask=asyncio.create_task(main())
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 10
asyncio.run(main())
#asyncio.run(next_one())
#
#
#
#establishing async between Functions->create task to be performed in the ideal time
#if the called task takes longer time the main task does not wait  but instead we can use await task
#at the end for the completion
## range 
x=['a','a','d','s','w',]
for i in range (1,len(x)):
       x=x.__getitem__(i)
       print(x)




                        

