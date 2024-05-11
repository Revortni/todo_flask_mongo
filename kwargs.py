def test(e, b, c, a, f):
    print(e, a, b, c, f)


k = {'a': 1, 'b': 2, 'c': 3}

test(1, **k, f=4)
