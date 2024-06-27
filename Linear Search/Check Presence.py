# -*- coding : utf-8 -*-


"""
Question: Given an array of integers and a target value, 
write a function to return true if the target exists in the array, 
and false otherwise.

"""

"""
#Problem Statement :
1. find the target value in a particular array if exits retrun true otherwise false
2. Here , It doesn't sepcify that if array is empty then?
"""

"""
Approach :
1. Create some test cases first
2. then state clear solution and implementation
3. analyze the algorithm and fix bugs , if any otherwise Optimize it
"""

# %%
#Example Test Case 

input = [3,4,5,8,9,6,5,4,1]
target = 2
output = False

test = {
    'input' : {
        'array' : [3,4,5,8,9,6,5,4,1],
        'target' : 2
    },
    'output' : False
}


"""
Test Cases :
1. the list array contains target value in middle
2. the list array contains target value at first
3. the list array contains target value at last
4. the list array doesn't have target value
5. the list array contains one element , which is target
6. the list array is empty
"""

# %%
tests = []

#test case 1 - the list array contains target value in middle
tests.append({
    'input' : {
        'array' : [2,3,4,5,8,9,0],
        'target' : 5
    },
    'output' : True
})


#test case 2 - the list array contains target value at first
tests.append({
    'input' : {
        'array' : [4,6,7,8],
        'target' : 4
    },
    'output' : True
})


#test case 3 - the list array contains target value at Last
tests.append({
    'input' : {
        'array' : [6,7,8,9,0],
        'target' : 0
    },
    'output' : True
})


#test case 4 - the list array doesn't have target value
tests.append({
    'input' : {
        'array' : [2,1,3,4,5,6,7],
        'target' : 9
    },
    'output' : False
})


#test case 5 - the list array contains one element , which is target
tests.append({
    'input' : {
        'array' : [3],
        'target' : 3
    },
    'output' : True
})


#test case 6 - the list array is empty
tests.append({
    'input' : {
        'array' : [],
        'target' : 12
    },
    'output' : False
})




"""
Create Solution:
1. create a variable position with start value 0
2. if target is found the array return True
3. If not , then return False
"""


# %%
def find_target(array,target):

    #create a variable position with start value 0
    position = 0

    #run a repetitive loop
    while position < len(array):

        #check target value
        if array[position] == target:
            return True
        
        position+=1
    #otherwise return False    
    return False
    

from jovian.pythondsa import evaluate_test_case,evaluate_test_cases
evaluate_test_case(find_target,test)
evaluate_test_cases(find_target,tests)