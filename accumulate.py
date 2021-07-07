"""
 if you need not only the final reduced result, but also intermediate ones, then you can use accumulate instead - function from another great module itertools. This is how you can use it to compute running maximum:
"""

from itertools import accumulate

data = [3, 4, 1, 3, 5, 6, 9, 0, 1]
print(list(accumulate(data, max)))
# [3, 4, 4, 4, 5, 6, 9, 9, 9]
