def valid_row(row):
    return isinstance(row, dict) and len(row) > 0

assert valid_row({'name': 'A'})
assert not valid_row({})
