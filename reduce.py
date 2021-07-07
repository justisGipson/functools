from functools import reduce
import operator

def product(iterable):
  return reduce(operator.mul, iterable, 1)

def factorial(n):
  return reduce(operator.mul, range(1, n))

def sum(numbers): # use `sum` function from std-lib instead
  return reduce(operator.add, numbers, 1)

def reverse(iterable):
  return reduce(lambda x, y: y + x, iterable)

print(product([1, 2, 3]))
# 6
print(factorial(5))
# 24
print(sum([2, 6, 8, 3]))
# 20
print(reverse("hello"))
# olleh
