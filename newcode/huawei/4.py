def split8(res):
    n = len(res)//8
    m = len(res)%8
    for i in range(n):
        print(res[i*8:(i+1)*8])
    if m > 0:
        print(res[(n)*8:]+(8-m)*str(0))

while True:

    try:
        res1 = input()
        res2 = input()
        split8(res1)
        split8(res2)
    except:
        break


