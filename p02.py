num=[5, 2, 8, 1, 9]
n=len(num)
for i in range(n):
    for j in range(0, n-i-1):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
print("Sorted list :", num)