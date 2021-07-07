'''
lru_cache provides least recently used cache of function results or in other words - memoization of results
'''

from functools import lru_cache
import requests

@lru_cache(maxsize=32)
def get_with_cache(url):
  try:
    r = requests(url)
    return r.text
  except:
    return "Not found"

for url in ["https://google.com",
            "https://reddit.com",
            "https://medium.com",
            "https://dev.to",
            "https://google.com"
            ]:
  get_with_cache(url)

print(get_with_cache.cache_info())
# CacheInfo(hits=1, misses=4, maxsize=32, currsize=4)
print(get_with_cache.cache_parameters())
# {'maxsize': 32, 'typed': False}
