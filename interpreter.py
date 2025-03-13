# user input for x y z
expression = input("Expression: ")
expression_split = expression.split(' ', 2)

# assign x and z to int, then y to operator
x = float(expression_split[0])
z = float(expression_split[2])
y = (expression_split[1])

# do the math
if y == '+':
    print(x + z)

elif y == '-':
    print(x - z)

elif y == '*':
    print(x * z)

elif y == '/':
    print(x / z)
