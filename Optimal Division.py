class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])
        
        if len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        
        result = str(nums.pop(0))+'/('
        for num in nums:
            result += str(num) + '/'
            
        result = result[:-1] + ')'
        
        return result