def is_numeric(value):
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False

assert is_numeric('10')
assert is_numeric('10.5')
assert not is_numeric('abc')
assert not is_numeric('')
print('CSV numeric rules passed')
