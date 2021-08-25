from additional_functions import is_positive_integer


def is_prime(number):
    """
    This function checks if the number is prime
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    divider = 5
    while divider * divider <= number:
        if number % divider == 0 or number % (divider+ 2) == 0:
            return False
        divider += 6
    return True

def is_prime_m(mers, degree):
    """
    This function checks if the Mersenne number is prime.
    According to Luca-Lehmer test.
    """

    mod = 4
    for index in range(degree - 2):
        l = mod**2 - 2
        mod = l % mers
    return not mod

def get_perfect_numbers(limit):
    """
    This function returns all perfect numbers less limit
    """

    if limit < 7:
        return []
    degree = 0
    perfect_numbers = [6]
    while True:
        degree += 1
        if not is_prime(degree):
            continue
        mers = 2**degree - 1
        suggested_perfect = 2**(degree-1) * mers
        if suggested_perfect >= limit:
            break
        if is_prime_m(mers, degree):
            perfect_numbers.append(suggested_perfect)

    return perfect_numbers


def task_330():
    """
    This function prints perfect numbers less limit
    """

    print(task_330.__doc__.strip())
    positive_integer_input = input('Enter positive integer (limit): ')

    if not positive_integer_input:
        print('You entered no characters.')
    elif is_positive_integer(positive_integer_input):
        perfect_numbers = get_perfect_numbers(int(positive_integer_input))
        print(f'All perfect numbers less {positive_integer_input}:\n{perfect_numbers}')
    else:
        print(f'"{positive_integer_input}" is not positive integer.')