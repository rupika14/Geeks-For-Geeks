#User function Template for python3

import math

class Solution:
    def countSquares(self, N):
        # code here
        
        n= math.sqrt(N)
        return math.ceil(n)-1
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countSquares(N))
# } Driver Code Ends