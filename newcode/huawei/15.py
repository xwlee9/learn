a = int (input())
b = list(bin(a))
count = 0
for i in b:
    if i == '1':
        count += 1
print (count)
