from __init__ import *
class Isosceles():
    def __init__(self,t1,angles):
        self.t1=t1
        self.angles=angles
    def is_Isosceles(self):
        flag =0
        flag1=0
        for i in range (len(self.t1.sides)-1):
            if self.t1.sides[i-1]==self.t1.sides[i]:
                flag=flag+1
        for i in range (len(self.angles)-1):
            if self.angles[i-1]==self.angles[i]:
                flag1=flag1+1
        if flag==1 and flag1==1:
            return 1
        else :
            return 0
        
t1=Triangle([2,2,3],4,5)
i=Isosceles(t1,[30,60,90])
value=i.is_Isosceles()
if value ==1:
    print("Yes")
else :
    print("No")

            
