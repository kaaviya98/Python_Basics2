from __init__ import *
class Scalene():
    def __init__(self,t1,angles):
        self.t1=t1
        self.angles=angles
    def is_Scalene(self):
        flag =0
        flag1=0
        for i in range (len(self.t1.sides)-1):
            if self.t1.sides[i-1]==self.t1.sides[i]:
                flag=flag+1
        for i in range (len(self.angles)-1):
            if self.angles[i-1]==self.angles[i]:
                flag1=flag1+1
        if flag==0 and flag1==0:
            return 1
        else :
            return 0
        
t1=Triangle([4,2,3],4,5)
s=Scalene(t1,[30,60,90])
value=s.is_Scalene()
if value ==1:
    print("Yes")
else :
    print("No")
