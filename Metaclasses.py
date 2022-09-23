#metaclass 
class Student:
    def __init__(self,y):
         self.y=y
    def get_values(self):
          return self.y

def __init__(self,y):
    self.y=y
def get_value(self):
    return (self.y)+self.x

p=type('Python',(Student,),{'get_value':get_value,'x':10})
f=p(5)

print(f.get_value())
print(f.get_values())
print(dir(p))
























# #metaclasses creating with base class
# def init(self, ftype):
# 	self.ftype = ftype

# def getFtype(self):
# 	return self.ftype

# FoodType = type('FoodType', (), {
# 	'__init__': init,
# 	'getFtype' : getFtype,
# 	})

# def vegFoods(self):
# 	return {'Spinach', 'Bitter Guard'}

# ## creating subclass using type
# VegType = type('VegType', (FoodType, ), {
# 	'vegFoods' : vegFoods,
# 	})


# vType = VegType('Vegetarian')
# print(vType.getFtype())
# print(vType.vegFoods())
