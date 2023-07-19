#docstring definition. It can be useful when wrting documentation.

def to_second(hours, minutes, seconds):
    """return the amount of seconds in the given hours, minutes, seconds"""
    return hours * 3600 + minutes * 60 + seconds

help(to_second)