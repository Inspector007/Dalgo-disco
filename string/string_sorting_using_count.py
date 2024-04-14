#Problem Description
#Given an array A. Sort this array using Count Sort Algorithm and return the sorted array.
A = 'acdgferaaaddffggzz'
freq = [0 for j in range(26)]
# print(freq)
for x in A:
    freq[ord(x)-ord('a')] += 1
print(freq)
ans = []
for i in range(26):
    for j in range(freq[i]):
        ans.append(chr(97+i))
print(''.join(ans))

# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def solve(self, A):
#         mx = max(A)
#         freq = [0 for j in range(mx + 1)]
#         for x in A:
#             freq[x] += 1
#         ans = []
#         for i in range(mx + 1):
#             for j in range(freq[i]):
#                 ans.append(i)
#         return ans

