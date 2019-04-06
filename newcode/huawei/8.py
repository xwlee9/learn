while True:
    try:
        n = int(input())
        dic = {}
        for i in range(n):
            k, v = map(int, input().split())

            if dic != None:
                if k in dic.keys() :
                    dic.update({k:int(dic.get(k)+v)})
                else:
                    dic.setdefault(k,v)
            else:
                dic.setdefault(k,v)

        for i,j in dic.items():
            print(i,j)

    except:
        break
        
        