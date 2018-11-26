import string
alpha = string.ascii_lowercase
def print_rangoli(size):
    # your code goes here   
    list_= []
    for i in range(size):
        m = "-".join(alpha[i:size])    
        list_.append(m[::-1]+m[1:])
    w= len(list_[0])  
    for i in range(n-1, 0, -1):
        print(list_[i].center(w, "-"))
    for i in range(n):
        print(list_[i].center(w, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
