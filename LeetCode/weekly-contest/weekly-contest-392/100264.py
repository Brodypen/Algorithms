class Solution:
    # Solve by "sliding window"
    # You move this pointer until its stop being descending or ascending
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        r = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                r = i + 1
                while r < len(nums) - 1 and nums[r] < nums[r + 1]:
                    r += 1
                res = max(res, r - i + 1)
                i = r
            elif nums[i] > nums[i + 1]:
                r = i + 1
                while r < len(nums) - 1 and nums[r] > nums[r + 1]:
                    r += 1
                res = max(res, r - i + 1)
                i = r
        return res
