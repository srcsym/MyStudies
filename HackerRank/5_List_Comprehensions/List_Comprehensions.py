x = int(input())
y = int(input())
z = int(input())
n = int(input())

from itertools import combinations

"""print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
"""

array = []

for i in range(0, x + 1):
    for j in range(0, y + 1):
        for k in range(0, z + 1):
            array.append([i, j, k])

array2 = []
for i in range(0, x + 1):
    for j in range(0, y + 1):
        for k in range(0, z + 1):
            if i + j + k != n:
                array2.append([i, j, k])
print(array2)
