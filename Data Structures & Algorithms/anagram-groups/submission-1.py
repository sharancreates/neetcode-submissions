class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        final = []
        visited = [False] * len(strs)
        for idx, i in enumerate(strs):
            if visited[idx]:
                continue
            else:
                visited[idx] = True
                temp = []
                temp.append(i)
                for j_idx in range(idx + 1, len(strs)):
                    j = strs[j_idx]
                    if not visited[j_idx]:
                        if sorted(i) == sorted(j):
                            temp.append(j)
                            visited[j_idx] = True
                final.append(temp)

        return final