def column_count(row):
    return len(row)

assert column_count({'a': 1, 'b': 2}) == 2
assert column_count({}) == 0
