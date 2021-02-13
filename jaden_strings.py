## Jaden Case StringsS

quote = "Connor is a man from newcastle, united kingdom"

def my_function(quote):
    return ' '.join(i.capitalize() for i in quote.split(" "))

# Square Numbers

import math

num = -1

def is_square(n):
    if n<0:
        return False
    n = math.sqrt(n)
    if n.is_integer():
        return True
    return False


print(is_square(num))