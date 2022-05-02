'''
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n 
and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.

'''
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        current_min = nums[0]
        for i in range(1,len(nums)): 
            if nums[i] < current_min: 
                current_min = nums[i]
                continue
            if nums[i] - current_min > max_diff: 
                max_diff = nums[i] - current_min 
            if min(nums) == nums[-1] and max_diff == 0: 
                max_diff = -1
        return max_diff
        
