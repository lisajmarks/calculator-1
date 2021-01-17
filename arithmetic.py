"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    add_num = num1 + num2
    return add_num


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    sub_num = num1 - num2
    return sub_num

def multiply(num1, num2):
    """Multiply the two inputs together."""
    multiply_num = num1 * num2
    return multiply_num


def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    divide_num = num1//num2
    return divide_num


def square(num1):
    """Return the square of the input."""
    square_num = num1**2
    return square_num


def cube(num1):
    """Return the cube of the input."""
    cube_num = num1**3
    return cube_num


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    pow_num = num1**num2
    return pow_num


def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    modnum = num1%num2
    return modnum
