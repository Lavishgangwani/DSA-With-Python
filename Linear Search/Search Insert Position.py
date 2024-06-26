# -*- coding: utf-8 -*-
"""

Question : Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

#### Here's a systematic strategy we'll apply for solving problems:

1. State the problem clearly. Identify the input & output formats.
2. Come up with some example inputs & outputs. Try to cover all edge cases.
3. Come up with a correct solution for the problem. State it in plain English.
4. Implement the solution and test it using example inputs. Fix bugs, if any.
5. Analyze the algorithm's complexity and identify inefficiencies, if any.
6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

#Problem statement
#- need to create a list 
# Not mentioned in sorted whether asc or desc by default we use asc
"""

# %%
#define signature function
def locate_nums(nums , target):
    pass

# %%
#define input & output 
nums = [3,5,6,7,8,9,19]
target = 7
output = 3

result = locate_nums(nums,target)
#print(result)

#print(result == output)

# %%
#creating a manual test
test = {
    'input' : {
        'nums' : [0,5,8,9,17,27],
        'target' : 14
    },
    'output' : 4
}

locate_nums(**test['input']) == test['output']


#define test cases 
#1- in Nums target could be at a middle of the nums
#2- In nums target could be first element
#3 - In nums target could be last element
#4- In nums the only element , which is target
#5 - In nums contains empty list , target would be -1 


# %%
#creating test cases
tests = []

#testcase-1 element should be in middle
tests.append({
    'input' : {
        'nums' : [3,5,6,7,8,9,19],
        'target' : 7
    },
    'output' : 3
})
# %%
#testcase-2 element should be first
tests.append({
    'input' : {
        'nums' : [12,14,17,18],
        'target' : 12
    },
    'output' : 0
})
# %%
#testcase-3 element should be last
tests.append({
    'input' : {
        'nums' : [0,5,7,9],
        'target' : 9
    },
    'output' : 3
})

# %%
#testcase-4 only element should be the target
tests.append({
    'input' : {
        'nums' : [6],
        'target' : 6
    },
    'output' : 0
}) 


# %%
#testcase-5 
tests.append({
    'input' : {
        'nums' : [1,2,4,5,7],
        'target' : 3
    },
    'output' : 2
})

print(tests)

"""
#now create solution
#1- create a variable 'position' with value 0
#2- then check if position is matches target then simply return position
#3- if not then iterate through the length of array of list
#4- then check end of arrays and if yes, then return -1
"""
# %%
#now implement a solution in function
def locate_nums(nums , target):
    #creeate a variable position with value 0
    position = 0

    #creating a loop repetation
    while True:

        if nums[position] == target:
            return position
        
        position += 1

        #checking if position reaches end of an array
        if position == len(nums):
            nums.append(target)
            print('nums : ',nums)

            sorted_nums = sorted(nums)
            print("sorted_nums : ",sorted_nums)
            return sorted_nums.index(target)


#%%
from jovian.pythondsa import evaluate_test_case , evaluate_test_cases
evaluate_test_case(locate_nums,test)
evaluate_test_cases(locate_nums,tests)









# %%
