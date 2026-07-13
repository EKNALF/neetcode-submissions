class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for index, num in enumerate(nums):
            a[num] = index
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in a and a[diff] != i:
                pair = [i, a[diff]]
                pair = sorted(pair)
                return pair
        
        return []