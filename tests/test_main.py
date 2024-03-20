#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simple_calculator.main import SimpleCalculator

def test_add_many_numbers():
    numbers = range(100)
    calculator = SimpleCalculator()
    result = calculator.add(*numbers)
    assert result == 4950

def test_subtract_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.subtract(6,4)
    assert result == 2