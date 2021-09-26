# Python program to display platform information
# # -------------------- 
import platform
info = platform.platform()
print('Platform info:', info)



# # -------------------- 
# You can import the whole random module and call its different functions
import random
print(random.randint(0,100))
print(random.random())


# # -------------------- 
# Or you can import the only function you need from a module
from random import randint
random_integer = randint(0,100)
print(random_integer)


# # --------------------
# Similarly you can import the whole math module and call its functions
import math
print(math.ceil(4.1))
print(math.floor(4.1))


# # ----------------
# or you can only import the ones you need, by separating them with a comma
from math import ceil, floor
print(ceil(4.1))
print(floor(4.1))

