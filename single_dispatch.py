from functools import singledispatch
from datetime import date, datetime, time

@singledispatch
def format(arg):
    return arg

@format.register
def _(arg: date):
    return f"{arg.day}-{arg.month}-{arg.year}"

@format.register
def _(arg: datetime):
    return f"{arg.day}-{arg.month}-{arg.year} {arg.hour}:{arg.minute}:{arg.second}"

@format.register(time)
def _(arg):
    return f"{arg.hour}:{arg.minute}:{arg.second}"

print(format("today"))
# today
print(format(date(2021, 7, 7)))
# 7-7-2021
print(format(datetime(2021, 7, 7, 10, 41, 50)))
# 7-7-2021 10:41:50
print(format(time(19, 22, 14)))
# 19:22:14
