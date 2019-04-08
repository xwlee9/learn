class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ln = len(nums)
        for i in range(ln):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return [j,i]