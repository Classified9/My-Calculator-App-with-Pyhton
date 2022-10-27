from operations import add, mul, div, subt, pi, exp, mod, docpreview,showoperation

print('Welcome to CALC ')
print()

docpreview()

# Accepting very first input from user
#TODO
# 1: INPUT MUST BE AN INTEGER VALUE COLLECTED FROM USER
# 2: COMPARE THE INPUT IF NOT WARN USER AND PROMPT USER TO TRY AGAIN


# def userInput1():
#     global input1
input1 = int(input('What is your first number? '))
#     # if type(user_input1) == int:
#     if input1.isdigit():
#         int(input1)
#     else:
#         print('Wrong Input, Try Again!')
#         userInput1()
#
# userInput1()


print()
showoperation()
print()

# Prompting user to choose an operation
operation = input('Pick an operation: ')

# Accepting second input from user
if operation == 'pi':
    pass
else:
    input2 = int(input('What is your second number? '))

# Performing Addition operation
if operation == '+':
    ans = add(input1, input2)
    print(input1, operation, input2, '=', ans, end='\n')

# Performing Subtraction operation
if operation == '-':
    ans = subt(input1, input2)
    print(input1, operation, input2, '=', ans, end='\n')

# Performing Multiplication operation
if operation == '*':
    ans = mul(input1, input2)
    print(input1, operation, input2, '=', ans, end='\n')

# Performing Division operation
if operation == '/':
    ans = div(input1, input2)
    print(input1, operation, input2, '=', ans, end='\n')

# Performing Floor Division operation
if operation == '//':
    ans = fl(input1, input2)
    print(input1, operation, input2, '=', ans, end='\n')

# Performing Exponential operation
if operation == '**':
    ans = exp(input1, input2)
    print(input1, operation, input2, '=', ans, end='\n')

# Performing Modulo operation
if operation == '%':
    ans = mod(input1, input2)
    print(input1, operation, input2, '=', ans, end='\n')

# Performing Pi operation
if operation == 'pi':
    ans = pi(input1)
    print(operation, input1, '=', ans, end='\n')
