class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = {}
                
        for i in nums:
            numdict[i] = numdict.get(i, 0) + 1

        sorted_numdict = dict(sorted(numdict.items(), key=lambda item: item[1], reverse=True))

        output = []
        count = 0
        for (key, value) in sorted_numdict.items():
            if count == k:
                break
            output.append(key)
            count += 1

        return output

