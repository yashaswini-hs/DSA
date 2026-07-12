class Solution(object):
    def arrayRankTransform(self, arr):
        rank = {}
        sorted_arr = sorted(set(arr))

        r = 1
        for num in sorted_arr:
            rank[num] = r
            r += 1

        result = []
        for num in arr:
            result.append(rank[num])

        return result