from collections import deque 

def bfs(adj,src):
    n = len(adj)
    visited = [False] * n 
    res = []
    q = deque()
    q.append(src)
    visited[src] = True 
    while q:
        curr = q.popleft()
        visited[curr] = True
        res.append(curr)
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True 
                q.append(x)
    return res
def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

if __name__ == "__main__":
    n = eval(input("Enter the number of nodes: "))
    adj = []
    for i in range(0,n):
        adj.append([])
    for i in range(0,n):
        # u,v = eval(input())
        u,v = map(int, input().split(' '))
        addEdge(adj,u,v)
    src = eval(input("Enter source: "))
    res = bfs(adj,src)
    
    for node in res:
        print(node,end=" ")