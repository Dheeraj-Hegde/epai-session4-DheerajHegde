### Assignment 4 - EPAi

#### This repository consists of code and test cases as part of Assignment 4 EPAi.

#### This assignment covers the below major topics
    1. Numeric Types
    2. Decimal precision changes                       
    3. Working with PEP8 Style guide
    4. Handling README.md file on GitHub

#### The repository consists of 2 main python scripts

    1. session4.py - contains the actual code 
    2. test_session4.py - contaiSession4 objectives

#### session4.py has below objects which performs actions as detailed below

    1. Class Qualean methods
    __init__(self, val)
    Initialize the Qualean object
     : param val : 

    2. __and__(self, other)
    Bitwise `&` (__and__) operator between two Qualeans
    : param other :  Qualean
    : return :  Qualean

    3. __or__(self, other)
    Bitwise `|` (__or__) operator between two Qualeans
    : param other :  Qualean
    : return :  Qualean

    4. __repr__(self)
    String representation of the object of the Qualean class
    : return :  string

    5. __str__(self)
    Readable string representation of the qualean
    : return :  string    

    6. __add__(self, other)
    Adds two outputs from the class Qualean

    7. __eq__(self, other)
    Checks for equality of two different outputs from Qualean

    8. __float__(self)
    Creates a floating value for the imaginary output from Qualean
    
    9. __ge__(self, other)
    Checks for greater than or equality of two different outputs from Qualean

    10. __gt__(self, other)
    Checks for greater than of two different outputs from Qualean

    11. __invertsign__(self)
    Changes the sign of the imaginary part of Qualean class input

    12. __sqrt__(self)
    Provides square root of the imaginary number stored as part of Qualean input
    
    13. __le__(self, other)
    Checks for lesser than or equality of two different outputs from Qualean
    
    14. __lt__(self, other)
    Checks for lesser than of two different outputs from Qualean
    
    15. __mul__(self, other)
    Multiples two Qualeans
    
    16. __bool__(self)
    Checks for boolean

#### test_session3.py file contains the below unit test cases along with their descriptions

    1. test_readme_exists
    Check if the README file exists
    : return :  None

    2. test_readme_contents
    Test the length of the README file
    : return :  None

    3. test_readme_file_for_formatting
    Tests the formatting for the README file
    : return :  None

    4.test_function_name_had_cap_letter
    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
    : return :  None

    5. test_indentations
    Checks if PEP-8 style indentations of 4 spaces has been followed
     : return : None

    6. test_and_function, 7. test_or_function and 8. test_or_short_circuit
    checks for short circuiting conditions
     : return : None

    9. test_sqrt_function
    Checks if square root of the imaginary number is implemented correctly
    : return : None

    10. test_add_100_times
    Checks if adding the imaginary number 100 times and multiplying the same with 100 gives the same output
    : return : None

    11. test_isclose_function
    Checks if by executing the class Qualean for 1million times returns the sum of 1 million outputs is nearing to zero
    : return : None

    12. test_ten_digit_check_function
    Checks if the precision of decimal is set to 10
    : return : None

    13. test_class_repr
    Checks if __repr__ is implemented or not
    : return : None

    14. test_class_str
    Checks if __str__ is implemented or not
    : return : None

    15. test_lt_function
    Checks if __lt__ function is working for < operator
     : return : None

    16. test_gt_function
    Checks if __gt__ function is working for > operator
    : return : None

    17. test_ge_function
    Checks if __ge__ function is working for >= operator
    : return : None

    18. test_le_function
    Checks if __le__ function is working for <= operator
    : return : None

    19. test_float_function
    Checks if __float__ retuns a float type
    : return : None

    20. test_mul_function
    Checks if __mul__ is implemented correctly to provide an multiplicative output
    : return : None

    21. test_bool_function
    Checks if __bool__ returns bool type
    : return : None

    22. test_eq_function
    Checks if __eq__ function is working for == operator
    : return : None

    23. test_invertsign_function
    Checks if the sign of the imaginary number generated is inverted or not
    : return : None
    
    24. test_readme_proper_description 
    Checks if all the functions have been covered within the README.md file
    
    25. test_for_cmath 
    Checks if cmath module was imported to perform square root operation