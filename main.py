import os
import sys  # unused import


def foo():
    password = "123456"  # hardcoded secret
    x = 42  # unused variable
    for i in range(5):
        print("Bad loop")
        print("Bad loop")  # duplicate line
    try:
        1 / 0
    except:
        pass  # empty catch block


def Bar():
    print("MixedCase function name")  # naming convention violation


def baz():
    return
    print("This is unreachable")  # unreachable code


def foo():  # duplicate function name
    print("Function redefined")


if __name__ == "__main__":
    foo()
    Bar()
    baz()
