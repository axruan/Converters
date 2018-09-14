# Alex Ruan
#Ascend-Descend
#14 September 2018

import sys
import math as m
import random as r

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

if x < y < z or x > y > z:
    print("True")
    print(x, y, z)

else:
    print("False")
    print(x, y, z)

input()
