#User function Template for python3

class Solution:
    def largestSubsquare(self, n, a):
        top = [[0 for _ in range(n)] for _ in range(n)]
        left = [[0 for _ in range(n)] for _ in range(n)]

        # Compute top metric
        for i in range(n):
            for j in range(n):
                if a[i][j] == 'X':
                    top[i][j] = 1 if i == 0 else top[i - 1][j] + 1

        # Compute left metric
        for i in range(n):
            for j in range(n):
                if a[i][j] == 'X':
                    left[i][j] = 1 if j == 0 else left[i][j - 1] + 1

        # Finding the largest subsquare
        maxSubSq = 0
        for i in range(n):
            for j in range(n):
                if top[i][j] == 0 or left[i][j] == 0:
                    continue

                currentValue = min(top[i][j], left[i][j])

                while currentValue > 0:
                    top1 = i - currentValue + 1
                    left1 = j - currentValue + 1

                    if left[top1][j] >= currentValue and top[i][left1] >= currentValue:
                        maxSubSq = max(maxSubSq, currentValue)
                        break

                    currentValue -= 1

        return maxSubSq
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        a=[]
        for i in range(n):
            s=list(map(str,input().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.largestSubsquare(n,a))
# } Driver Code Ends