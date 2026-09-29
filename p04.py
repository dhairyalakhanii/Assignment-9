num=[5, 2, 8, 1, 9]
num.sort()
n=len(num)
if n%2==0:
    median=(num[n//2-1]+num[n//2])/2
else:
    median=num[n//2]
print("Median:", median)