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


#evaluate_test_case(check_min,test)



"""
Ques: Find the sum maxinum and minimum in an given array with exactly four out of 5 elements in array
"""
arr1 = [1,3,5,7,9]
def miniMaxSum(arr):
    sum_  = 0
    scores = []
    for i in range(len(arr)):
        sum_ += arr[i]
        for j in range(i+1,len(arr)-1):
            sum_ += arr[j]
            scores.append(sum_)
            
    min_ = min(scores)
    max_ = max(scores)
    
    print(min_ , max_)

miniMaxSum(arr1)
            