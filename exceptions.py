n=int(input())
for i in range(n):
    try:    
        m=input().split()   
        print(int(m[0])//int(m[1]))
    except ZeroDivisionError as e:
        print ("Error Code:",e)
    except ValueError as e:
        print ("Error Code:", e) 

