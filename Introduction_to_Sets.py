def average(array):
    # your code goes here 
    total=0
    l=list(set(array))   
    sum_=sum(l)    
    return(sum_/len(l))



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)