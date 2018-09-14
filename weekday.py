# Alex Ruan
#Weekday 
#14 September 2018

import sys
import math as m

m = float(sys.argv[1])
d = float(sys.argv[2])
y = float(sys.argv[3])

day1 = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

y0 = y - (14 - m)//12
x = y0 + y0/4 - y0/100 + y0/400
m0 = m + 12 * ((14 - m)//12) - 2
d0 = int((d + x + (31 * m0)//12) % 7)

print(day1[d0])
print(y0, x, m0, d0)

input()
