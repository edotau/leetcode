#!/usr/bin/env python3


#def twoSum(self, nums: List[int], target: int) -> List[int]:
def allPairs(nums, target):
    for i in range(0, len(nums)):
        for j in range (i+1, len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return None

query = [[2,7,11,15], [3,2,4], [3,3]]
                                                    
targets = [9, 6, 6]

ans = [[0,1], [1,2], [0,1]]

for i in range(0, len(query)):
    if allPairs(query[i], targets[i]) != ans[i]:
        print("Error: There is a bug in your python code")
print("You can submit your code to leet code!")
    
