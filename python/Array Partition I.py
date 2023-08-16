class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            total += nums[i]
        return total