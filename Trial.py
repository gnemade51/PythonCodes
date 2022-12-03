# A Python program to print all combinations
# of given length with unsorted input.
from itertools import combinations

# Get all combinations of [2, 1, 3]
# and length 2
# li = list(input())
# print(li)
# comb = combinations(li,2)
li = [1,2,3]
print(li)
for i in range(2,len(li)+1):
    print(list(combinations(li,i)))

# Print the obtained combinations
# print(comb)