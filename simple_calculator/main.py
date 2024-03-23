# -*- coding: utf-8 -*-
from functools import reduce

class SimpleCalculator:
    def add(self,*args):
        return sum(args)
    
    def subtract(self,a,b):
        return a - b
    
    def multiply(self,*args):
        if not all(args):
            raise ValueError
        return reduce(lambda x,y: x*y, args)
    
    def div(self,a,b):
        try:
          return a / b
        except ZeroDivisionError:
            return float('inf')
    
    def avg(self, it, lt=None, ut=None):
        length = 0
        total = 0

        for number in it:
            if lt is not None and number < lt:
                continue
            if ut is not None and number > ut:
                continue
            length += 1
            total += number

        if length == 0:
            return 0

        return total / length