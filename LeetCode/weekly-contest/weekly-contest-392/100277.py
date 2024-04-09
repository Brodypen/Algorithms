class Solution:
    # Idea
    # This is a frequency problem.
    # Frequency of number
    # Then from there we can see if we need to changes more numbers to equal to k.
    # How many times do we have to do that.

    # How can we have a hashmap that stores frequency and a way to get the highest frequency?

    # We have an array from [0, len(nums) - 1]
    # This array index acts as count of frequency.
    
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        