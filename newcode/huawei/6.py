a = int(input())
str = []
def div_demo(n):
    global str
    for i in range(2,n+1):
        if n%i == 0:
            str.append(i)
            m = n//i
            if m == 1:
                break
            div_demo(m)
            break
div_demo(a)
for i in str:
    print(i, end = ' ')