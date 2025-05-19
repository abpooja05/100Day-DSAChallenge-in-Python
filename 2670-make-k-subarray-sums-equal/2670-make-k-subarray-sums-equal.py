class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:

        n = len(arr)
        g = gcd(n, k)  # Number of groups

        res = 0
        for start in range(g):
            group = []
            i = start
            while True:
                group.append(arr[i])
                i = (i + k) % n
                if i == start:
                    break
            group.sort()
            m = group[len(group) // 2]
            res += sum(abs(x - m) for x in group)
        return res