#-*- coding : utf-8 -*-

"""
Question : Given a sorted array and a target value, 
write a function to determine if the target exists in the array.
If it exists, return its index; otherwise, return -1.

"""


"""
Problem Statement : 
1. Have to Write a function to check target exists in array. if yes, then return index position
if not , then return -1
"""


# %%
input = [2,3,4,5,7]
target= 4
output = 2


test = {
    'input' : {
        'array' : [2,3,4,5,6,7,8],
        'target' : 4
    },
    'output' : 2
}


"""
Create Test cases
1. in the list array target could be in middle element.
2. in the list array target could be last element
3. in the list array target could be first element
4. in the list array contains only element , which is target
5. list array is empty
"""


# %%
tests = []

#testcase 1
tests.append({
    'input' : {
        'array' : [11,13,14,17,18,19],
        'target' : 14
    },
    'output' : 2
})

#testcase 2
tests.append({
    'input' : {
        'array' : [15,17,18,19],
        'target' : 15
    },
    'output' : 0
})


#testcase 3
tests.append({
    'input' : {
        'array' : [21,23,24,27,28,29],
        'target' : 29
    },
    'output' : 5
})


#testcase 4
tests.append({
    'input' : {
        'array' : [19],
        'target' : 19
    },
    'output' : 0
})


#testcase 5
tests.append({
    'input' : {
        'array' : [],
        'target' : 11
    },
    'output' : -1
})



# %%
"""
Create Solution :
1. use binary search approach with time complexity O(log N)
"""


def check_target(array, target):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2
        mid_number = array[mid]

        if mid_number == target:
            return mid  # Return the index instead of mid_number
        
        elif mid_number < target:
            low = mid + 1

        else:  # No need to check again, the only possibility left is mid_number > target
            high = mid - 1

    return -1

# Example Usage
array1 = [2, 3, 4, 5, 6, 7, 8]
target1 = 4
print(check_target(array1, target1))  # Output: 2

array2 = [1, 3, 5, 7, 9]
target2 = 4
print(check_target(array2, target2))  # Output: -1


from jovian.pythondsa import evaluate_test_case , evaluate_test_cases
evaluate_test_case(check_target,test)
evaluate_test_cases(check_target , tests)