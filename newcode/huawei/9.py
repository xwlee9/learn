a = input()
b = list(a)
b.reverse()
ls = []
for i in b:
    if i not in ls:
        ls.append(i)
        print(i,end='')



    




