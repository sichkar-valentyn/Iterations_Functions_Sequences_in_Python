# Iteration, functions and sequences

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
