def getMinVertex(dist,selected):
    minv=-1
    mindist=INF
    for v in range(len(dist)):
        if not selected[v] and dist[v]<mindist:
            mindist=dist[v]
            minv=v
        return minv

def MSTPrim(vertex,adj):
    vsize=len(vertex)
    dist=[INF]*vsize
    dist[0]=0
    selected=[False]*vsize

    for i in range(vsize):
        u=getMinVertex(dist.selected)
        selected[u]=True
        print(vertex[u], end=':')
        print(dist)

        for v in range(vsize):
            if (adj[u][v]!=None):
                if selected[v]==False and adj[u][v]<dist[v]:
                    dist[v]=adj[u][v]
