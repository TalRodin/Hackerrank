def print_f(n,arr):
    print(list(sorted(set(arr)))[-2])
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print_f(n,arr)
