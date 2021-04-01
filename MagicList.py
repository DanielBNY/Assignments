"""
Magic List
Create a Python class that implements a simplified list by skipping boundary checks when possible
"""
from dataclasses import dataclass


@dataclass
class Person:
    age: int = 1


class WrappedList:
    def __init__(self, cls_type):
        self.cls_type = cls_type
        self._lst = [cls_type]

    def __getitem__(self, item):
        return self._lst[item]

    def __setitem__(self, key, value):
        self._lst.append(self.cls_type)
        self._lst[key] = value
