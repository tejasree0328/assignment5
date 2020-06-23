Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
n = float(input("number of sides: "))
s= float(input("length of a side: "))
p = n * (s** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is: ",p)
