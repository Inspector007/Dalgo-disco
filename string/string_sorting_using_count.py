#Problem Description
#Given an array A. Sort this array using Count Sort Algorithm and return the sorted array.
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        mx = max(A)
        freq = [0 for j in range(mx + 1)]
        for x in A:
            freq[x] += 1
        ans = []
        for i in range(mx + 1):
            for j in range(freq[i]):
                ans.append(i)
        return ans

