while 1:
    try:
        ls = []
        n = int(input())
        for i in range(n):
            ls.append(input())
            ls.sort()
        for i in ls:
            print (i)
    except:
        break
