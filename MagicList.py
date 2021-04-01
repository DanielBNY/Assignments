"""
Magic List
Create a Python class that implements a simplified list by skipping boundary checks when possible
"""


class WrappedList:
    def __init__(self):
        self._lst = [None]

    def __getitem__(self, item):
        return self._lst[item]

    def __setitem__(self, key, value):
        self._lst[key] = value
