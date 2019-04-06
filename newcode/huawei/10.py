a =input()
b = list(a)
ls = []
count = 0
for i in b:
    if i not in ls:
        ls.append(i)
        count += 1
print(count)