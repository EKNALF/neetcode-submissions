class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i, num in enumerate(nums):
            if i <= farthest:                       # I can reach index i
                farthest = max(farthest, i + num)   # does it push my reach further?
            else:
                return False                        # gap: can't reach i or anything after
        
        return farthest >= len(nums) - 1