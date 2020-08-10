import pytest
import random
import string
import session4
import os
import inspect
import re
import cmath
from decimal import Decimal
import decimal
import math
import sys

README_CONTENT_CHECK_FOR = [
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme_words = [word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_and_function():
    f_num = random.randint(1, 10)
    assert session4.Qualean(f_num).__and__() == False, 'Short Circuit logic is not correct'

def test_or_function():
    f_num = random.randint(1, 10)
    assert session4.Qualean(f_num).__or__() == True, 'Short Circuit logic is not correct'

def test_sqrt_function():
    for i in range(50):
        val = random.choice([1,0,-1])
        q = session4.Qualean(val)
        assert (abs(q.__sqrt__())) == cmath.sqrt(abs(q.img_part)), f"sqrt is not working"

def test_add_100_times():
    tot_sum = 0
    q = session4.Qualean(1)
    for i in range(100):
        tot_sum += q.img_part
    assert tot_sum == 100 * q.img_part, "q + q + ... 100 times is not equal to 100 * q"

def test_isclose_function():
    result = 0
    f_num = random.randint(1, 10)
    g_num = random.randint(1, 20)
    for i in range(1000000):
        val = random.choice([1,0,-1])
        q = session4.Qualean(val)
        result += q.img_part

    assert math.isclose(result, 0, abs_tol=1000), 'q+q+q... is not equal to n*q'


def test_ten_digit_check_function():
    f_num = random.randint(1, 10)
    q = session4.Qualean(f_num)
    assert len(str(q.img_part).strip('.')[-1]) <= 10, 'Bankers Rounding off is not done for 10 digits'

def test_class_repr():
    s = session4.Qualean(1)

    assert 'object at' not in s.__repr__()

def test_class_str():
    s = session4.Qualean(1)

    assert 'object at' not in s.__str__()

def test_lt_function():
    for i in range(50):
        val = random.choice([1,0,-1])
        s1 = session4.Qualean(val)
        s2 = session4.Qualean(val)
        assert (s1.__lt__(s2)) == (s1 < s2), f"Your program returned wrong less than comparison"

def test_gt_function():
    for i in range(50):
        val = random.choice([1,0,-1])
        s1 = session4.Qualean(val)
        s2 = session4.Qualean(val)
        assert (s1.__gt__(s2)) == (s1 > s2), f"Your program returned wrong > comparison"

def test_ge_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        s1 = session4.Qualean(val)
        s2 = session4.Qualean(val)
        assert (s1.__ge__(s2)) == (s1 >= s2), f"Your program returned wrong >= comparison"

def test_le_function():
    for _ in range(50):
        val = random.choice([1,0,-1])
        s1 = session4.Qualean(val)
        s2 = session4.Qualean(val)
        assert (s1.__le__(s2)) == (s1 <= s2), f"Your program returned wrong <= comparison"

def test_float_function():
    for i in range(50):
        val = random.choice([1,0,-1])
        s = session4.Qualean(val)
        assert (type(s.__float__())) == float, f"Your program returned wrong float conversion"

def test_mul_function():
    for i in range(50):
        val = random.choice([1,0,-1])
        s1 = session4.Qualean(val)
        s2 = session4.Qualean(val)
        assert (s1.__mul__(s2)) == s1*s2, f"Your program returned wrong multiplication"

def test_bool_function():
    for i in range(50):
        val = random.choice([1,0,-1])
        s = session4.Qualean(val)
        assert (s.__bool__()) == bool(s), f"Your program returned wrong bool"

def test_or_short_circuit():
    for i in range(50):
        value = random.choice([-1,0,1])
        s = session4.Qualean(value)
        s2 = session4.Qualean(value)
        if bool(s) == True:
            assert (s.__or__(s2)) == True, f"Your program returned wrong or"
            assert (s.__or__()) == True, f"Your program returned wrong or"
            assert (s.__and__()) == False, f"Q2 not defined"
        else:
            assert (s.__or__()) == False, f"Q2 not defined"
            assert (s.__and__(s2)) == False, f"Your program returned wrong and"
            assert (s.__and__()) == False, f"Your program returned wrong and"

def test_eq_function():
    for i in range(50):
        val = random.choice([1,0,-1])
        s1 = session4.Qualean(val)
        s2 = session4.Qualean(val)
        assert (s1.__eq__(s2)) == (s1 == s2), f"Your program returned wrong == comparison"

def test_invertsign_function():
    for i in range(50):
        val = random.choice([1, 0, -1])
        s1 = session4.Qualean(val)
        assert (s1.__invertsign__()) == (s1.img_part * -1), f"Your program returned wrong == comparison"

def test_for_cmath():
    READMELOOKSGOOD = True
    f = open("session4.py", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in ["cmath"]:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not imported cmath module for sqrt calculation"
