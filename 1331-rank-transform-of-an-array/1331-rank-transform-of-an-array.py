class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp = arr.copy()
        arr.sort()
        hash_ = {}
        for i in range(len(arr)):
            if arr[i] not in hash_:
                hash_[arr[i]] = len(hash_)+1

        for i in range(len(temp)):
            temp[i] = hash_[temp[i]]

        return temp

