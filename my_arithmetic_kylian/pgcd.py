def pgcd(a, b):
    """
    Return the greatest common divisor of a and b

    Parameters
    ----------
    a : int
        First number
    b : int
        Second number
    Returns
    -------
    int
        The greatest common divisor of a and b
    Examples
    --------
    >>> pgcd(10, 25)
    5
    """

    while b:
        a, b = b, a % b
    return a
