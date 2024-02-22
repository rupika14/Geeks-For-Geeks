#User function Template for python3

class Solution:

    def Count(self, S):
        # code here
        count=0
        for i in range(len(S)):
            if S[i].isalpha():
                count+=1
            
            
            
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        print(solObj.Count(S))
# } Driver Code Ends