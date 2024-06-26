# %%
import sys
print(sys.executable)
print(sys.prefix)

# %%

from jovian.pythondsa import evaluate_test_case , evaluate_test_cases

# %% [markdown]
"""
# ### Question: Given an array of integers, write a function to find the first occurrence of a given target element. If the element is found, return its index; otherwise, return -1.

# %% [markdown]
# #### Here's a systematic strategy we'll apply for solving problems:
# 
# 1. State the problem clearly. Identify the input & output formats.
# 2. Come up with some example inputs & outputs. Try to cover all edge cases.
# 3. Come up with a correct solution for the problem. State it in plain English.
# 4. Implement the solution and test it using example inputs. Fix bugs, if any.
# 5. Analyze the algorithm's complexity and identify inefficiencies, if any.
# 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.

# %%
## Problem statement & approach
#- in this problemit doesn't state that if array is empty then ? 
#- Need to create an array first
"""
# %%
#design signature function 
def locate_array(array , target):
    pass

# %%
'''
##Now Come up with some example inputs & outputs. Try to cover all edge cases.
##Before we start implementing our function,it would be useful to come up with some example inputs and outputs which we can use later to test out problem. 
#We'll refer to them as *test cases*.
'''

array = [2,3,4,5,8,7,6]
target = 8
output= 4

# %%
result = locate_array(array , target)
print(result)

# %%
#checking our function is it working fine or not
result == output

# %%
test = {
    'input' : {
        'array' : [2,3,4,5,8,7,6],
        'target' : 8
    },
    'output' : 4
}

test

# %%
#Now test our function properly
locate_array(test['input']['array'] , test['input']['target']) == test['output']

locate_array(**test['input']) == test['output']

'''
#Now create some test cases
#1. in list array target could be in the middle element
#2. in list array target could be first element
#3. in list array target could be last element
#4. in list array contains only one element, which is target
#5. the list array could be empty
#6. the list card contains repetitive words
#7. the target could appears more than once in list array
'''
# %%
tests = []
#1. in list array target could be in the middle element
tests.append({
    'input' : {
        'array' : [3,4,5,9,7,6,0],
        'target' : 9
    },
    'output' : 3
})

#2. in list array target could be first element
tests.append({
    'input':{
        'array':[4,5,6,7,8,9],
        'target' : 4
    },
    'output' : 0
})

#3. in list array target could be last element
tests.append({
    'input' : {
        'array' : [3,2,6,7,8,9,1],
        'target' : 1
    },
    'output' : 6
})


#4. in list array contains only one element, which is target
tests.append({
    'input' : {
        'array' : [6],
        'target' : 6
    },
    'output' : 0
})


#5. the list array could be empty
tests.append({
    'input' : {
        'array' : [],
        'target' : 4
    },
    'output' : -1
})

#6. the list array contains repetitive words
tests.append({
    'input' : {
        'array' : [3,4,7,7,7,7,8,2],
        'target' : 8
    },
    'output' : 6
})

#7. the target could appears more than once in list array
tests.append({
    'input' : {
        'array' : [8,8,9,9,9,9,2,2,2,2,0,0,0,1],
        'target' : 9
    },
    'output' : 2
})


tests

'''
#now create solution
#1- create a variable 'position' with value 0
#2- then check if position is matches target then simply return position
#3- if not then iterate through the length of array of list
#4- then check end of arrays and if yes, then return -1
'''
# %%
def locate_array(array , target):
    #create a variable 'position with value 0'
    position = 0

    #run the repetative loop
    while True:
        if array[position] == target:
            return position

        position += 1

        #if position reaches end of an array
        if position == len(array):
            return -1 

# %%
locate_array(**test['input']) == test['output']

# %%
#evaluate_test_case(locate_array,test)

# %%
#evaluate_test_cases(locate_array,tests)

# %%
#debug it using 'print' statement

def locate_array(array , target):
    #create a variable 'position with value 0'
    position = 0

    print('array : ',array)
    print('target : ',target)
    
    #run the repetative loop
    while True:
        print('position : ',position)
        
        if array[position] == target:
            return position

        position += 1

        #if position reaches end of an array
        if position == len(array):
            return -1 

# %%
array4 = tests[4]['input']['array']
target4 = tests[4]['input']['target']

#locate_array(array4,target4)

# %%
def locate_array(array,target):
    position=0
    while position < len(array):
        if array[position] == target:
            return position
        position += 1
    return -1

# %%
tests[4]

# %%
locate_array(array4,target4)

# %%
evaluate_test_cases(locate_array,tests)

# %%



