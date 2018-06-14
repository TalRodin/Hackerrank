def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        if year%100!=0:
            return (True)
        else:           
            if year%400==0:
                return (True)
            else:
                return(False)
    else:
        return(leap)
 
 


year = int(input())
print(is_leap(year))
