def km2float(s):

    """
    Changes values considered in millions(M) to thousands.

    """
    S = s.upper()
    if 'K' in S:
        return float(s[:-1])
    elif 'M' in S:
        return float(s[:-1])*1000
    else:
        return 0