class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique=sorted(set(arr))
        

        rank={}
        count=1
        for value in unique:
            rank[value]=count
            count+=1
        result=[]
        for x in arr:
            result.append(rank[x])
        return result