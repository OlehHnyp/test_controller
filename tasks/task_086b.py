from additional_functions import is_positive_integer


def get_sum_of_digits(number):
    """
    This function calculate the sum of all digits in number
    """
    return sum(int(digit) for digit in str(number))



def task_086b():
    """
    This function print the sum of all digits in inputed positive integer.
    """
    print(task_086b.__doc__.strip())
    positive_integer_input = input('Enter positive integer: ')

    if not positive_integer_input:
        print('You entered no characters.')
    elif is_positive_integer(positive_integer_input):
        digits_sum = get_sum_of_digits(positive_integer_input)
        print(f'The sum of all digits in {positive_integer_input} is {digits_sum}')
    else:
        print(f'"{positive_integer_input}" is not positive integer.')

