#User function Template for python3

class Solution:
    def longestSubstring(self, s , n):
        # code here 
        maxlen=0
        res="-1"
        i,j=0,0
        while i<n and j<n:
            ss=s[i:j+1]
            if s.find(ss,j+1)!=-1:
                sslen=len(ss)
                if sslen>maxlen:
                    res=ss
                    maxlen=sslen
            else:
                i+=1
            j+=1
        return res
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        S=input()
        
        ob = Solution()
        print(ob.longestSubstring(S , N))
# } Driver Code Ends