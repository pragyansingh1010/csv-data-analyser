def average(values):
    return sum(values) / len(values) if values else 0

assert average([]) == 0
assert average([10, 20]) == 15
assert average([5]) == 5
print('CSV empty-data rules passed')
