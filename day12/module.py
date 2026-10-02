# built-in-module (math)

import math
import random
import datetime
from zoneinfo import ZoneInfo
import os
r=math.sqrt(25)
print(round(r,2))
print(math.pow(2,4))
print(round(math.pi,4))
print(abs(-5))
print(divmod(12,7))
print(sum([2,4,3]))
randomNumber=random.randint(1,5)
print(randomNumber)
names=["Marjan","Raj","Mymani"]
ranName=random.choice(names)
print(ranName)

print(datetime.datetime.now().time())

data=datetime.datetime.now(ZoneInfo("Asia/Dhaka"))
date=data.strftime("%d/%m/%Y")
time=data.strftime("%I:%M:%S %p")
print(date)
print(time)

print(os.getcwd())  # current directory  

from math import sqrt,pi
print(sqrt(9))
print(round(pi,4))

import math as m  #module name remname short (m)

print(m.sqrt(25))

from math import *
print(abs(-43))