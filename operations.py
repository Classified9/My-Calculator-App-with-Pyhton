def readme():
    print()
    print('CALC is a basic calculator that does several operations')
    print('---' * 15, 'OPERATIONS', '---' * 15)
    print('+', '--', 'ADDITION', 'To ADD')
    print('-', '--', 'SUBTRACTION', 'To SUBTRACT')
    print('/', '--', 'DIVISION', 'To DIVIDE')
    print('*', '--', 'MULTIPLICATION', 'To MULTIPLY')
    print('//', '--', 'FLOOR DIVISION', 'To get the integer value from a division', 'TO USE: ', 'Type: \'f\'')
    print('%', '--', 'MODULO', 'To get the remainder', 'TO USE: ', 'Type: \'mo\'')
    print('^', '--', 'EXPONENTIAL', 'Exponential', 'TO USE: ', 'Type: \'ex\'')
    print('Pie', '--', 'PIE', 'Unary operator; Pie')
    print()
    print('---' * 10, 'BY: AWOFIRANYE SHERIF OLANREWAJU', '---' * 10)
    print()
    print('---' * 15, 'END', '---' * 15)


def add(x, y):
    return x + y


def subt(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def fl(x, y):
    return x // y


def mod(x, y):
    return x % y


def exp(x, y):
    return x ** y


def pi(x):
    return x * 3.1426


# Requesting user for Documentation preview
def docpreview():
    doc = input('Would you like to read the documentation? Type \'y\' for Yes, or , \'n\' for No : ').lower()
    if doc == 'y':
        readme()
    elif doc == 'n':
        pass
    else:
        print('Wrong input, Try again!')
        docpreview()


# Preview for operations to choose by the user
def showoperation():
    print('+', '-', '*', '/', '//', '%', 'pi', sep='\n')
