def generate_pairs(lst):
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]

print(generate_pairs([1, 2, 3]))
