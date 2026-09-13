def valid_columns(columns):
    return isinstance(columns, list) and len(columns) > 0 and all(isinstance(c, str) and c.strip() for c in columns)

assert valid_columns(['name', 'marks'])
assert valid_columns(['id'])
assert not valid_columns([])
assert not valid_columns([''])
print('CSV column rules passed')
