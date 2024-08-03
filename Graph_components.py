comp=[]

def predst(t):
    global comp
    if t!=comp[t]:
        t=comp[t]
    return t


def joinn(j,k):
    global comp
    j=predst(j)
    k=predst(k)
    if j!=k:
        comp[j]=k


n=int(input('please enter the number of vertices'))
for i in range(0,n):
    comp.append(i)
   

    

print ('please enter adjacency matrix')
for j in range(0,n):
    for k in range(0,n):
        r=int(input())
        if r==1 and j<k:
            joinn(j,k)

count=0
for i in range(0,n):
    if comp[i]==i:
        count+=1

print('The number of graph components is  ')
print(count)
