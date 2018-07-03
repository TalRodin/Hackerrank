def count_substring(string, sub_string):
    #print(string)
    #print(sub_string)
    total=0
    
    for i in range(0, len(string)):
        if string[i]==sub_string[0]:
            j=i+len(sub_string)
            if string[i:j]==sub_string:
                total+=1
    return(total)
        