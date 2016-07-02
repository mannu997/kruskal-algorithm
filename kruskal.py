def root(i):
    while(lis[i]!=i):
        lis[i]=lis[lis[i]]
        i=lis[i]
    return i
def Union(u,v):
    rootu=root(u)
    rootv=root(v)
    if size[rootu]<size[rootv]:
        lis[u]=lis[v]
        size[rootv]+=size[rootu]
    else:
        lis[v]=lis[u]
        size[rootu]+=size[rootv]
        
N,M=raw_input().split(" ")
N,M=int(N),int(M)
Graph={}
for i in range(M):
    x,y,r=raw_input().split(" ")
    x,y,r=int(x),int(y),int(r)
    if (x,y) in Graph.keys():
        if Graph[x,y]>r:
            Graph[x,y]=r
    else:
        Graph[x,y]=r
S=input()
t=sorted(Graph.items(),key=lambda x: x[1])
lis=[0]*(N+1)
size=[1]*(N+1)
for i in range(1,N+1):
    lis[i]=i
totalweight=0
for i in t:
    edge,weight=i
    u,v=edge
    if root(u)!=root(v):
        totalweight+=weight
        Union(u,v)
print totalweight   