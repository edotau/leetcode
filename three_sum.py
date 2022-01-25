#!/usr/bin/env python3

def threeSum(nums):
	not_same = []
	zero = []
	
	curr = nums[0]
    mid_idx = len(nums)/2
    
	for i in range(0, len(nums):
	
def findSums(nums, size, target):
    for i in range(0, len(nums)-2):
        sub_arr = []
        total = sub_sum -sub_arr[i]
        for j in range(i+1, size):
            if total == target - nums[j]
                return sub_arr[i], nums[j], target - nums[j]
            else:
                
            
    




def zero(i, j, k):
    if i + j + k == 0:
        return True
    else:
        return False


def not_equal(nums):
    curr = nums[0]
    for i in range(0, len(nums):
        if curr != nums[i]:
            next_num = nums[i]
            for j in range(i+1, idx))
                if curr != next_num and next_num != nums[j]:
                    return zero[curr, next_num, nums[j]]
    return []


nums = [-1,0,1,2,-1,-4]

out =[[-1,-1,2],[-1,0,1]]


ans = threeSum(nums)
print(f"answer is {ans}")
