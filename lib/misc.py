def is_integer(n: any):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()