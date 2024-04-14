# ///
# Problem Description
# Given a string A, you are asked to reverse the string and return the reversed string.
# Example Input
# Input 1:

#  A = "Deepak"
# Example Output
# Output 1:

#  "kapeed"
#  ///
A = 'kapeed'
A = [i for i in A]
l,r = 0,len(A)-1
while l < r:
    A[l],A[r] = A[r],A[l]
    l+=1
    r-=1
print(''.join(A))