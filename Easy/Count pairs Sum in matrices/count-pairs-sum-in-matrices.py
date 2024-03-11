#User function Template for python3


class Solution:
    
	def countPairs(self, mat1, mat2, n, x):
	    count=0
        l=(2*(n*n))
        a=0
        b=l-1
        ans=[-1]*(l)
        for i in range(n):
            for j in range(n):
                ans[a]=mat1[i][j]
                a+=1
                ans[b]=mat2[n-i-1][n-j-1]
                b-=1
        a=0
        b=len(ans)-1
        while a<b:
            if ans[a]+ans[b]==x:
                count+=1
                a+=1
                b-=1
            elif ans[a]+ans[b]>x:
                b-=1
            else:
                a+=1
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n , x = input().split()
		n,x = int(n), int(x)
		mat1 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat1.append(a)

		mat2 = []
		for _ in range(n):
			a = [int(x) for x in input().split()]
			mat2.append(a)

		ob = Solution()
		ans = ob.countPairs(mat1, mat2, n, x)
		print(ans)

# } Driver Code Ends