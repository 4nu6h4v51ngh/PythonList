num=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l=len(num)
for i in range(int(l/2)):
    n=num[i]
    num[i] = num[l-i-1]
    num[l-i-1] = n
print(num)