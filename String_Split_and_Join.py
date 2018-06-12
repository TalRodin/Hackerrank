#String_Split_and_Join
def split_and_join(line):
    # write your code here
    a=line.split(' ')
    new_line="-".join(a)
    return(new_line)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)