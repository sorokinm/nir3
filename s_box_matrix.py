perm=[2,6,1,7,3,0,4,5]
r = perm
power=len(perm)

matr=[[0 for i in range(len(r))] for i in range(len(r))]


for e in range(0,len(r)):
    for a in range (0,len(r)):
        s=perm[a^e]^perm[a]
        matr[e][s]+=1

print("Division by: "+str(power))
for i in range(0,len(r)):
    print(matr[i])
