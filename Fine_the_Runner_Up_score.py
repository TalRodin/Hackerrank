#Find the Runner-Up score!
if __name__ == '__main__':
    n = int(input())
arr = list(map(int, input().split()))
m=max(arr)
i=0
while (i<n):
    if m==max(arr):
        arr.remove(max(arr))
    i+=1
print(max(arr))