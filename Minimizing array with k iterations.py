n, k = map(int,input("enter elements") .split())
print("Enter the elements:")
arr = list(map(int, input().split()))
for j in range (0,k):
    arr.sort()
    arr[n-1]=int(arr[n-1]/2)
result = sum(arr)
print(result)    
