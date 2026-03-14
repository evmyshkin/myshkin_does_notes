def connector(vals: list[int]) -> str:
    """Connector
    
    >>> connector([1, 4, 5, 2, 3, 9, 8, 11, 0])
    '0-5,8-9,11'
    
    >>> connector([1, 4, 3, 2])
    '1-4'
    
    >>> connector([1, 4])
    '1,4'
    
    """
    seq = sorted(set(vals))
    intervals: list[tuple[int, int]] = []

    start = end = seq[0]

    for x in seq[1:]:
        if x == end + 1:
            end = x
        else:
            intervals.append((start, end))
            start = end = x
    intervals.append((start, end))

    return ','.join(f'{a}-{b}' if a != b else str(a) for a, b in intervals)
