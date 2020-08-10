'''
    Import cmath for carrying out square root operation
            decimal for changing the default precision for demicals
'''
import cmath
import decimal
from decimal import Decimal
import random

class Qualean:
    '''
        class Qualean(object):
        Accepts one value either 0, 1 or -1 as input.
        Transforms the input to multiple itself with a random uniformly distributed number between
        -1 and 1 to form an imaginary number.
        Further the below magic functions are available for use.
        __and__,  __or__, __repr__, __str__, __add__, __eq__, __float__, __ge__, __gt__,
        __invertsign__, __le__, __lt__, __mul__, __sqrt__, __bool__
    '''

    def __init__(self, val):
        '''
        Initialize the Qualean object
        :param val:
        '''
        self.val = val
        with decimal.localcontext() as ctx:
            ctx.prec = 10 ## Change the precision of decimal to 10
            ctx.rounding = decimal.ROUND_HALF_EVEN
            self.img_part = self.val * Decimal(random.uniform(-1, 1))

    def __and__(self, other=None):
        '''
        Bitwise `&` (__and__) operator between two Qualeans
        :param other:
        :return:
        '''
        if (bool(self.img_part) is False):
            return False
        elif (other is None):
            return False
        else:
            return bool(self.img_part and other.img_part)

    def __or__(self, other=None):
        '''
        Bitwise `|` (__or__) operator between two Qualeans
        :param other:
        :return:
        '''
        if (bool(self.img_part) is False):
            return False
        elif (other is None):
            return True
        else:
            return bool(self.img_part or other.img_part)

    def __repr__(self):
        '''
        String representation of the object of the Qualean class
        :return:
        '''
        return f'{self.__class__.__name__}'

    def __str__(self):
        '''
        Readable string representation of the qualean
        :return:
        '''
        return str(self.val)

    def __add__(self, other):
        '''
        Adds two outputs from the class Qualean
        :param other:
        :return:
        '''
        return Qualean(self.img_part + other.img_part)

    def __eq__(self, other):
        '''
        Checks for equality of two different outputs from Qualean
        :param other:
        :return:
        '''
        return self.img_part == other.img_part

    def __float__(self):
        '''
        Creates a floating value for the imaginary output from Qualean
        :return:
        '''
        return float(self.img_part)

    def __ge__(self, other):
        '''
        Checks for greater than or equality of two different outputs from Qualean
        :param other:
        :return:
        '''
        return self.img_part >= other.img_part

    def __gt__(self, other):
        '''
        Checks for greater than of two different outputs from Qualean
        :param other:
        :return:
        '''
        return self.img_part > other.img_part

    def __invertsign__(self):
        return self.img_part * -1

    def __le__(self, other):
        return self.img_part <= other.img_part

    def __lt__(self, other):
        return self.img_part < other.img_part

    def __mul__(self, other):
        return self.img_part * other.img_part

    def __sqrt__(self):
        return cmath.sqrt(self.img_part)

    def __bool__(self):
        return self.val != 0