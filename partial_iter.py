# use partial to utilize little known feature of iter function - it's possible to create an iterator by passing
# callable and a sentinel value to iter

from functools import partial

RECORD_SIZE = 64

# read binary file
with open("file.data", "rb") as file:
  records = iter(partial(file.read, RECORD_SIZE), b'')
  for r in records:
    # do something with the record
