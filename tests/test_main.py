#!/usr/bin/env python
# -*- coding: utf-8 -*-

from simple_calculator.main import SimpleCalculator
import pytest

def test_add_many_numbers():
    numbers = range(100)
    calculator = SimpleCalculator()
    result = calculator.add(*numbers)
    assert result == 4950

def test_subtract_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.subtract(6,4)
    assert result == 2

def test_multiply_many_numbers():
    numbers = range(1,10)
    calculator = SimpleCalculator()
    result = calculator.multiply(*numbers)
    assert result == 362880

def test_divide_two_float_numbers():
    calculator = SimpleCalculator()
    result = calculator.div(3,2)
    assert result == 1.5

def test_divide_by_zero_returns_inf():
    calculator = SimpleCalculator()
    result = calculator.div(5,0)
    assert result == float('inf')

def test_mul_by_zero_raises_exception():
    calculator = SimpleCalculator()

    with pytest.raises(ValueError):
        calculator.multiply(5,0)

def test_compute_average_of_iterable():
    calculator = SimpleCalculator()
    result = calculator.avg([1,2,3,4])
    assert result == 2.5

def test_function_accepts_optional_upper_treshold():
    calculator = SimpleCalculator()
    result = calculator.avg([1,2,4,3],ut=3)
    assert result == 2

def test_function_accepts_optional_lower_treshold():
    calculator = SimpleCalculator()
    result = calculator.avg([1,2,4,3],lt=2)
    assert result == 3

def test_function_work_with_empty_list():
    calculator = SimpleCalculator()
    result = calculator.avg([])
    assert result == 0

def test_function_work_after_outlier_removal():
    calculator = SimpleCalculator()
    result = calculator.avg([2,5],4,3)
    assert result == 0

def test_outriel_removal_work_when_list_is_empty():
    calculator = SimpleCalculator()
    result = calculator.avg([],4,3)
    assert result == 0

def test_avg_manages_zero_value_lower_outlier():
    calculator = SimpleCalculator()
    result = calculator.avg([-1, 0, 1], lt=0)
    assert result == 0.5

def test_avg_manages_zero_value_upper_outlier():
    calculator = SimpleCalculator()
    result = calculator.avg([-1, 0, 1], ut=0)
    assert result == -0.5

def test_avg_accepts_generators():
    calculator = SimpleCalculator()
    result = calculator.avg(i for i in [2, 5, 12, 98])
    assert result == 29.25