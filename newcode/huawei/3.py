while True:
    try:
        n = int(input())
        array = []
        for i in range(n):
            array.append(int(input()))
        temp = list(set(array))
        print(temp)
        temp.sort()
        for i in temp:
            print(i)
    except:

        break



# while True:
#     try:
#         n=int(input())
#         res=[]
#         for i in range(n):
#             res.append(int(input()))
#         for i in sorted(set(res)):
#             print (i)
#     except:
#         break