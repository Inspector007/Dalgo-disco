#Sum of N natural numberr using rrecursive number

def sum(n):
    if n == 1:
        return 1
    else:
        return n+sum(n-1)

print(sum(5))
print("time complexity o(n) and space complexity o(n)")
