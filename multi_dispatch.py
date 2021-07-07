from multipledispatch import dispatch

@dispatch(list, str)
def concatenate(a, b):
  a.append(b)
  return a

@dispatch(str, str)
def concatenate(a, b):
  return a + b

@dispatch(str, int)
def concatenate(a, b):
  return a + str(b)

print(concatenate(["a", "b"], "c"))
# ['a', 'b', 'c']
print(concatenate("Hello", "World"))
# HelloWorld
print(concatenate("a", 1))
# a1

'''
use @dispatch decorator to overload multiple arguments, for example to implement concatenation of various types

with multipledispatch library we didn't need to define and register base function, rather we created multiple functions with same name. If we wanted to provide base implementation, we could use @dispatch(object, object) which would catch any non-specific argument types.
'''
