cube = lambda x: x**3

def fibonacci(n):
    list_fib=[]
    a=0
    b=1
    if n==1:
        list_fib.append(a) 
    elif n==2:                
        list_fib.append(a)
        list_fib.append(b)
    elif n>2:
        list_fib.append(a)
        list_fib.append(b)  
        for i in range(n-2):          
            fib=a+b
            list_fib.append(fib)
            a=b
            b=fib
    return(list_fib)
        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube,fibonacci(n))))
