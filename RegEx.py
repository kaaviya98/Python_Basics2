# import re
# pattern='ma+n'
# test='manmad'
# res=re.findall(pattern,test)
# print(res)

# string = "Python is fun"

# # check if 'Python' is at the beginning
# match = re.search('\APython', string)
# print(dir(match))

import re

string = '''39801 356, 2102 1111'''

# Three digit number followed by space followed by two digit number
pattern = '(\d{3}) (\d{2})'

# match variable contains a Match object.
match = re.finditer(pattern, string,flags=re.I) 
if match:
     for i in match:
         print(i)
else:
  print("pattern not found")
#   print(dir(re.search))


  