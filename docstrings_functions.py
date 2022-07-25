# Builtin functions
# a = 9
# b = 4
# # c = (a + b)
# c = sum((a, b)) #tap ctrl + use mouse on "sum" for builtins
# print(c)
# User Defined functions
"""
def function1():

    print("Hello you are in function 1")
function1()
"""


# def function1(a, b):
#     print("I LOVE YOU", a + b )
#
# function1(2100, 900)


def function(a, b):
    """This is a docstring"""

    average= (a + b)/2
    print(average)
    return average
# function(8, 9)
v = function(8, 9)
print(v)

print(function.__doc__)
