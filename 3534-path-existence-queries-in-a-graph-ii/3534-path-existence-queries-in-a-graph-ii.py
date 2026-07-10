class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((v, i) for i, v in enumerate(nums))

        vals = [x[0] for x in arr]

        # position of original node in sorted order
        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        # connected component id
        comp = [0] * n
        cid = 0
        comp[0] = 0
        for i in range(1, n):
            if vals[i] - vals[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        # next reachable position in one edge
        nxt = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and vals[j + 1] - vals[i] <= maxDiff:
                j += 1
            nxt[i] = j

        LOG = n.bit_length()

        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[prev[i]]
            up.append(cur)

        ans = []

        for u, v in queries:
            if u == v:
                ans.append(0)
                continue

            a = pos[u]
            b = pos[v]

            if comp[a] != comp[b]:
                ans.append(-1)
                continue

            if a > b:
                a, b = b, a

            cur = a
            jumps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < b:
                    cur = up[k][cur]
                    jumps += 1 << k

            ans.append(jumps + 1)

        return ans