class Triangle:
    def __init__(self,sides,base,per_height):
        self.sides=sides
        self.base=base
        self.per_height=per_height
    def area(self):
        area=(1/2)*self.base *self.per_height
        return area
    def perimeter(self):
        sum =0
        for i in self.sides:
            sum =sum +i
        return sum
# sides=[]
# n=int(input("Enter no of items: "))
# for i in range (0,n):
#     e=int(input("Enter the number"))
#     sides.append(e)
# base=int(input("Enter the base: "))
# hei=int(input("Enter the per_height"))
# t=Triangle(sides,base,hei)
# area=t.area()
# perimeter=t.perimeter()
# # print("Area of the triangle is :",area)
# # print("Perimeter of the triangle is :",perimeter)

