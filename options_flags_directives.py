def return_1_or_true():
    """
        >>> return_1_or_true()
        1

    """
    return True


def return_1_or_true_with_option_flag():
    """
        >>> return_1_or_true() # doctest: +DONT_ACCEPT_TRUE_FOR_1
        True

    """
    return True


if __name__ == '__main__':
    return_1_or_true_with_option_flag()
    # return_1_or_true_with_option_flag()
