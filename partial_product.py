"""considering that usage of reduce generally produces one-liners it's ideal candidate for partial"""

from functools import reduce, partial
import operator

product = partial(reduce, operator.mul)

print(product([1, 2, 3]))
# 6
