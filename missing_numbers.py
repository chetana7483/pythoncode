def missing_numbers(lst):
    return [num for num in range(lst[0], lst[-1] + 1) if num not in lst]

print(missing_numbers([1,2,4,6,7]))
