# caching results of class attributes - like caching rendered HTML pages

from functools import cached_property

class Page:

  @cached_property
  def render(self, value):
    # do something with supplied val
    # long computation that renders html

    return html
