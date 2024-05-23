class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        ans=set()
        repeat=0
        for a in A:
            if a in ans:
                repeat=a
            ans.add(a)
        n=len(A)
        sum_n=n*(n+1)//2
        missing=sum_n-sum(ans)
        
        return [repeat,missing]
        
        
