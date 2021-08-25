from additional_functions import is_positive_integer


def count_symbols(string):
    """
    This function counts the number of symbols in string.
    """
    return len(str(string))

def task_086a():
    """
    This function prints the number of digits in inputted positive integer.
    """

    print(task_086a.__doc__.strip())
    positive_integer_input = input('Enter positive integer: ')

    if not positive_integer_input:
        print('You entered no characters.')
    elif is_positive_integer(positive_integer_input):
        number_of_digits = count_symbols(positive_integer_input)
        plural = 's' if number_of_digits > 1 else ''
        print(f'It\'s {number_of_digits} digit{plural} in {positive_integer_input}')
    else:
        print(f'"{positive_integer_input}" is not positive integer.')