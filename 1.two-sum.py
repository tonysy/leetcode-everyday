#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (38.11%)
# Total Accepted:    898.1K
# Total Submissions: 2.4M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
# 
# 
#
# 双指针法
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        new_list_left = sorted(nums)
        new_list_right = new_list_left #.copy()

        # index_dict = dict(zip(nums, range(len(nums))))
        index_list = []

        pointer_l = 0
        pointer_r = len(nums) - 1
        while True:
            temp_sum = new_list_left[pointer_l] + new_list_right[pointer_r]
            if temp_sum < target:
                pointer_l += 1
            elif temp_sum > target:
                pointer_r -= 1
            elif temp_sum == target:
                break
            else:
                raise ValueError
        
        index_l = nums.index(new_list_left[pointer_l])
        index_list.append(index_l)
        
        nums.pop(index_l) # for some conditional test case '[3,3]\n6', '[-1,-2,-3,-4,-5]\n-8'
        
        index_r = nums.index(new_list_left[pointer_r])
        if index_r >= index_l:
            index_r += 1
        
        index_list.append(index_r)
        # nums.pop(index_r)

        return sorted(index_list)
    