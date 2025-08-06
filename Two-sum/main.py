class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, v in enumerate(nums):
            j= i+1
            while i<j < len(nums):
                if nums[i] + nums[j] == target: 
                    return [i, j]
                j+=1
myOB = Solution()
print(myOB.twoSum([3,5,9], 12))