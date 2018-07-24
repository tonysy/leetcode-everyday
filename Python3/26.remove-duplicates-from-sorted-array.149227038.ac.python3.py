class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """         
        if len(nums) == 1:
             return 1
        elif nums == []:
             return 0
        else:
            item_first = nums[0]
            pointer = 0
            while True:
                if pointer < len(nums)-1:
                    item_current = nums[pointer]
                    item_next = nums[pointer+1]
                    if item_next == item_current:
                        nums.remove(item_next)
                    else:
                         pointer +=1
                else:
                     break
                    
            return len(nums)
                

