# File: Iterations_Functions_Sequences_in_Python.py
# Description: Iterations, Functions and Sequences in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Iterations, Functions and Sequences in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Iterations_Functions_Sequences_in_Python (date of access: XX.XX.XXXX)


# Defining the functions which we will use inside the list


def plus(x):
    return x + 2


def multiply(x):
    return 3 * x


def subtract(x):
    return x - 1


# Defining the list
three_functions = [plus, multiply, subtract]


# Reorganizing the list
y = three_functions[::-1]
# We read the structure [::-1] as - from beginning to end and just change the direction
# The third parameter '-1' means that we need to read in the opposite direction
# As the result we will have y = [subtract, multiply, plus]


# Defining the variable
t = 1


# Iterating
for f in y:
    t = f(t)


# Showing the result
print(t)
