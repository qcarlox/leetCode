class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for i in range(len(nums)):
            position = abs(nums[i])-1
            if nums[position] > 0:
                nums[position] *= -1
            else:
                output.append(position+1)
                
        return output
        