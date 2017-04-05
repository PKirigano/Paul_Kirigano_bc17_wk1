def data_type(n):
    if isinstance(n, int):
        if n>100:
            return 'more than 100'
        elif n<100:
            return'less than 100'
        else:
            return 'equal to 100'
    elif isinstance(n, str):
        return len(n)
    elif n is None:
        return 'no value'
    elif isinstance(n, bool):
        return n
    elif isinstance(n, list):
        try:
            return n[2]
        except Exception as e:
            return None