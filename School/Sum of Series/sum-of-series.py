
class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        a=(n*(n+1))//2
        return a

#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.seriesSum(n)
        
        print(res)
        

# } Driver Code Ends