"""
using formatting concaternation instead of using "+"
23.9.20
"""

def helloName(name):
    return f"Hello, {name}"


def sumTwo(a,b):
    return f"{a} added to {b} equals {a+b}"


def longDivision(a,b):
    return f"{a} divided by {b} equals {a//b} remainder {a%b}"


def power(a,b):
    return f"{a} to the power of {b} equals {a**b}"


print(helloName("Eugene"))

print(sumTwo(1,2))

print(longDivision(5,2))

print(power(2,2))