from collections.abc import Sequence
from multipledispatch import dispatch

@dispatch(Sequence, (str, int))
def concatenate(a, b):
  return list(a) + [b]

'''
Instead of listing all the possible sequences, we can use Sequence abstract type (assuming that our implementation can handle it) which covers things like list, tuple or range
'''
