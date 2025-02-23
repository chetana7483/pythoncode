def cumulative_sum(list):
    result=[]
    total=0
    for num in list:
       total+=num
       result.append(total)
    return result
print(cumulative_sum([1,2,3,4]))    
