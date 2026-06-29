class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)

        for i in range(n):
            seen = set()
            target = -nums[i]

            for j in range(i + 1, n):
                complement = target - nums[j]

                if complement in seen:
                    triplet = tuple(sorted((nums[i], nums[j], complement)))
                    res.add(triplet)

                seen.add(nums[j])

        return [list(x) for x in res]