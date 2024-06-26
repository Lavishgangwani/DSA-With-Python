# -*- coding: utf-8 -*-

'''
Question: Given an array of integers and a target value, 
write a function to count how many times the target appears in the array.
'''

"""
Problem Statement :
1. count the number of times target appears
"""

# %%
#Signature Function
def count_array(array,target):
    pass

# %%
##create input & output Examples
arr = [1,2,3,3,3,3,5]
target = 3
output = 4


# %%
result = count_array(array=arr,target=target)
print(result)

print(result == output)
# %%
#Now create a Dict test
test = {
    'input' : {
        'array' : [1,2,3,3,3,3,6],
        'target' : 3
    },
    'output' : 4
}

# %%
count_array(**test['input']) == test['output']
#It'll show False because we haven't implemented function yet



"""
create Test cases:
1. the count of number in array could be anything
2. multiple number counts in array list
3. if num not found in array list
4. array list contains one element should be the count 1
"""

# %%
tests = []

#test-case 1
tests.append({
    'input' : {
        'array' : [1,2,3,4,4,4,4,4,5],
        'target' : 4
    },
    'output' : 5
})


#test case 2
tests.append({
    'input' : {
        'array' : [1,2,2,2,3,3,3,3,3,5],
        'target' : 2
    },
    'output' : 3
})

#test case 3
tests.append({
    'input' : {
        'array' : [1,2,5,6,7,8,8,8,8,8],
        'target' : 11
    },
    'output' : 0
})

#test case 4
tests.append({
    'input' : {
        'array' : [5],
        'target' : 5
    },
    'output' : 1
})

#testcase 5
tests.append({
    'input' : {
        'array' : [],
        'target' : 1
    },
    'output' : 0
})

# %%
"""
create Solution :
1. create a variable count as start value 0
2. check if number is equal to target then count inc from 0 to 1 
3. if not , then iterate
"""

def count_array(array,target):

    #create a loop repetative
    for i in range(len(array)):
        if array[i] == target:
            count = array.count(target)
            return count
    return 0  
            
# %%
from jovian.pythondsa import evaluate_test_case , evaluate_test_cases
evaluate_test_case(count_array,test_case=test)
evaluate_test_cases(count_array,tests)
         