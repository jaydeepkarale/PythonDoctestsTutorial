def return_sum_of_two_numbers(a: int, b: int):
    """
    :param a:
    :param b:
    :return:

    # our function works for postive numbers
    >>> return_sum_of_two_numbers(10, 20)
    30

    >>> return_sum_of_two_numbers(1000, 2000)
    3000

    >>> return_sum_of_two_numbers(1000, -2000)
    -1000

    # our function works for negative numbers
    >>> return_sum_of_two_numbers(-1000, -2000)
    -3000

    >>> return_sum_of_two_numbers(10, 'b')
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'int' and





    """
    return a + b


if __name__ == '__main__':
    print(return_sum_of_two_numbers(10, 20))


