#https://practice.geeksforgeeks.org/problems/maximum-sum-rectangle2948/1
#Given a 2D matrix M of dimensions RxC. Find the maximum sum submatrix in it.
import math
import sys


class Solution:
    def maximumSumRectangle(self, r, c, M):
        # code here
        maxx = float("-inf")
        re = []
        for p in range(r):
            re = [0] * c
            for i in range(p, r):
                for j in range(c):
                    re[j] += M[i][j]
                summ = self.kadane(re)
                if summ > maxx:
                    maxx = summ
        return maxx

    def kadane(self, arr):
        cur_sum = 0
        maxx = float('-inf')
        for i in range(len(arr)):
            cur_sum += arr[i]
            if cur_sum > maxx:
                maxx = cur_sum
            if cur_sum < 0:
                cur_sum = 0

        return maxx


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        N, M = map(int, sys.stdin.readline().strip().split())
        a = []
        for i in range(N):
            s = list(map(int, sys.stdin.readline().strip().split()))
            a.append(s)
        ob = Solution()
        print(ob.maximumSumRectangle(N, M, a))  # } Driver Code Ends




