# 1. Two Sum: store nums and their indexes into dicts, calculate complement, check if complement already in the dict, then store
# using enumerate when you want both the index and the value of a list 
# Tell: needed to find a pair, second half is computable from given information -> hashmap for O(1) lookup ("two numbers that sum to X", "find pair where a+b=target")


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        seen = {}
        
        numsToReturn = [0,0]
        for index, value in enumerate(nums):
            otherNum = target - value
            if otherNum in seen:
                numsToReturn[0] = index
                numsToReturn[1] = seen[otherNum]
            seen[value] = index
        return numsToReturn

            