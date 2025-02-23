def sublists_sum(list, target):
    result = []
    for i in range(len(list)):
        sum = 0
        for j in range(i, len(list)):
            sum += list[j]
            if sum == target:
                result.append(list[i:j+1])  
    return result
print(sublists_sum([1, 2, 3, 4, 5], 5))
