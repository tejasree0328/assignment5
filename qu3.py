Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> r=int(input('Radius:'))
from math import pi
x=float(input('Angle:'))
area=(pi*r**2)*(x/360)
print('Area of segment of a circle :',area