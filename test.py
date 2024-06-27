"""
Question: 
Write a function to find the minimum element in an unsorted array of integers.
"""
arr = [3,4,1,6]
target = 1
output = 1

test = {
    'input' : {
        'arr' : [9, 2, 3, 6, 1, 8]
    },
    'output' : 1
}

from jovian.pythondsa import evaluate_test_case

def check_min(arr):
    if len(arr) != 0:
        minimum= min(arr)
        return minimum


evaluate_test_case(check_min,test)

