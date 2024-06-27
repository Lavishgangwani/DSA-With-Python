# -*- coding : utf-8 -*-

"""
Question: Given an array of integers and a target value, 
write a function to find the first and last position of the target in the array. 
If the target is not found, return [-1, -1].
"""


"""
Problem Statement:
1. we have to find first and last position of target
2. if the array is empty then?
"""


# %%
#sample example test
input = [2,3,4,3,5,6]
target = 3
output = [1,3]

test = {
    'input' : {
        'array' : [2,3,4,5,5,6,7],
        'target' : 5
    },
    'output' : [3,4]
}



"""
Create Test Cases:
1. the list array have first and last position of target at any position
2. the list array have one after another target position
3. the list array is empty
4. the list contain only one element
5. the list contains two element which is target
"""


# %%
tests = []
tests.append({
    'input' : {
        'array' : [1,3,5,6,6,8,9],
        'target' : 6
    },
    'output' : [3,4]
})


tests.append({
    'input' : {
        'array' : [2,2,3,4,5,6],
        'target' : 2
    },
    'output' : [0,1]
})


tests.append({
    'input' : {
        'array' : [],
        'target' : 11
    },
    'output' : [-1,-1]
})


tests.append({
    'input' : {
        'array' : [3,4,5,6,7,6],
        'target' : 0
    },
    'output' : [-1,-1]
})


tests.append({
    'input' : {
        'array' : [5],
        'target' : 5
    },
    'output' : [0,0]
})


tests.append({
    'input' : {
        'array' : [2,2],
        'target' : 2
    },
    'output' : [0,1]
})

"""
Create Solution :
1. Run a nested loop use Quadratic Algorithm (O(n^2))
"""

# %%
def first_and_last_position(array,target):
    for i in range(len(array)):
        if array[i] == target:
            for j in range(i+1,len(array)):
                if array[j] == target:
                    return [i,j]
    return [-1,-1]

# %%
"""
Now Optimizing it through binary search O(log n)Algorithim approach

Here's how binary search can be applied to our problem:

1. Find the middle element of the list.
2. If it matches queried number, return the middle position as the answer.
3. If it is less than the queried number, then search the first half of the list
3. If it is greater than the queried number, then search the second half of the list
4. If no more elements remain, return [-1,-1].
"""


def binarysearch(array,target):
    #define first position function
    def first_position(array,target):
        #define variable
        low , high = 0 , len(array) - 1

        #run repetative loop
        while low <= high:
            
            #find mid element
            mid = (low + high) // 2
            #check mid element is less than target value
            if array[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
    

    #define last position function
    def last_position(array,target):
        #define variable
        low , high = 0 , len(array) - 1

        #run repetative loop
        while low <= high:
            
            #find mid element
            mid = (low + high) // 2
            #check mid element is less than target value
            if array[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        return high
    
    first_index = first_position(array,target)
    last_index = last_position(array,target)

    #check if target is not in array
    if first_index <= last_index and 0 <= first_index < len(array) and array[first_index] == target:
        return [first_index,last_index]
    else:
        return [-1,-1]
    
        


from jovian.pythondsa import evaluate_test_case,evaluate_test_cases
evaluate_test_case(binarysearch,test)
evaluate_test_cases(binarysearch,tests)
