def output_result(result, log=None):
  if log is not None:
    log.debug(f"Result is: {result}")

def concat(a, b):
  return a + b

import logging
from multiprocessing import Pool
from functools import partial

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("default")

p = Pool()

p.apply_async(concat, ("Hello ", "World"), callback=partial(output_result, log=logger))
p.close()
p.join()
