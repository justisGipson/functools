from multipledispatch import AmbiguityWarning

test_multipledispatch:10: AmbiguityWarning:
Ambiguities exist in dispatched function some_func

The following signatures may result in ambiguous behavior:
    [str, object], [object, str]


Consider making the following additions:

@dispatch(str, str)
def some_func(...)
