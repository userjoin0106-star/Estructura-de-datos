M = [[1,2,3],[4,5,6],[7,8,9]]

#print("Primera forma de recorrer")
#for i in range(len(M)):
#    print((M[i]))
#    for f in range(len(M[i])):
#        print(M[i][f])

#print("segunda forma de recorrer")
#for i in M:
#    print(i)
#    for f in i:
#        print(f)

print("tercera forma de recorrer")
i=0
while i < len(M):
    print(M)
    f=0
    while f < i:
        print(f)
        f+=1