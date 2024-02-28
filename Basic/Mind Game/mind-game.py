#User function Template for python3

import random
class Solution:
    def mindGame(self, K):
        # code here
        x=random.randint(1,10)
        return (((x*2)+K)//2)-x

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        K=int(input())
        
        ob = Solution()
        print(ob.mindGame(K))
# } Driver Code Ends