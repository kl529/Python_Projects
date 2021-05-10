class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable_dict = {}

        for i in range(len(nums)):
            value = target - nums[i]
            if hashtable_dict.get(value) is not None and hashtable_dict[value] != i:
                return [ hashtable_dict[value], i ]

            hashtable_dict[nums[i]] = i
            
#https://leetcode.com/problems/two-sum/
