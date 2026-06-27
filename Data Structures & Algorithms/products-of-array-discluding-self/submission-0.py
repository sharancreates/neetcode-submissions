class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        n = len(nums)
        for i in range(n):
            temp = 1
            for j in range(n):
                if j != i:
                    temp *= nums[j]
            output.append(temp)
        return output