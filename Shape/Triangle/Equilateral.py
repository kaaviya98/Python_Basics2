from main1 import Triangle
class Equilateral(Triangle):
    def __init__(self,sides,base,hei,angles):
        super().__init__(sides,base,hei)
        self.angles=angles
    def is_Equilateral(self):
        flag =0
        flag1=0
        for i in range (len(self.sides)-1):
            if self.sides[i-1]==self.sides[i]:
                flag=flag+1
        for i in range (len(self.angles)-1):
            if self.angles[i-1]==self.angles[i]:
                flag1=flag1+1
        if flag>1 and flag1>1:
            return True
        else :
            return False

angles=[];sides=[];base=0;height=0
# n=int(input("Enter no of items: "))
# for i in range (0,n):
#     e=int(input("Enter the side"))
#     sides.append(e)
# base=int(input("Enter the base: "))
# hei=int(input("Enter the per_height")) 
# n=int(input("Enter no of items: "))
# for i in range (0,n):
#     e=int(input("Enter the angle"))
#     angles.append(e)          
e=Equilateral(sides,base,height,angles)
# print(e.area())
# print(e.perimeter())

# value=e.is_Equilateral()
# if value == 1:
#     print("Yes")
# else:
#     print("No")