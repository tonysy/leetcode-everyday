class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        new_digits = digits
        new_digits[-1] += 1
        
        length = len(digits)
        digit = 0
        for i in range(length):
            digit += new_digits[i]*(10 **(length - i - 1))
        
        final_digits = [int(i) for i in str(digit)]
        return final_digits#digit
