def fibo_sum(number: int):
    """
    Recursively calculates the fibonacci sequence's sum up to a given number.

    :param number: An integer that represents the last fibonacci number.
    :return: The sum of the sequence.
    """

    if number < 2:
        return number

    return fibo_sum(number - 1) + fibo_sum(number - 2) + 1
