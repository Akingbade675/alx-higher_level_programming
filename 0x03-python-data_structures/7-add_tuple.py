def add_tuple(tuple_a=(), tuple_b=()):
    aa = (tuple_a[0] if len(tuple_a) > 0 else 0)
    ab = (tuple_b[0] if len(tuple_b) > 0 else 0)
    ba = (tuple_a[1] if len(tuple_a) > 1 else 0)
    bb = (tuple_b[1] if len(tuple_b) > 1 else 0)
    return (aa + ab, ba + bb)