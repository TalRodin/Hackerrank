def func(list):
    list_=[list[i][0] for i in range(len(list)) ]
    list_names=[list[i][1]  for i in range(len(list))  if list[i][0]==sorted(set(list_))[1]]

    for i in sorted(list_names):
         print(i)


if __name__ == '__main__':
    list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([score,name])
    func(list)



