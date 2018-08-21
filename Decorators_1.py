def wrapper(f):
    def fun(l):
         decorated_list = ['+91 {} {}'.format(n[-10: -5], n[-5:]) for n in l]
         return f(decorated_list)
    return (fun)

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    #print(l)
    sort_phone(l) 