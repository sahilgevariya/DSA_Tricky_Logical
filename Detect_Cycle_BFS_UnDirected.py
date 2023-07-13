# For directed graph we can use Topological sort which is using BFS.

# BFS - for UnDirected graph
def cycleDetected(start_node):
    parent = -1
    visited[start_node] = True
    q = deque()
    
    q.append((start_node, parent))
    while q:
        cur_node, parent = q.popleft()
        
        for nei in graph[cur_node]:
            if not visited[nei]:
                visited[nei] =  True
                q.append((nei, cur_node))
            elif  parent != nei:              # if visited[nei]
                return True
                
    return False

visited = [False]*n
for src in range(n):
    if not visited[src]:
        if cycleDetected(src):
            # there is cycle in graph

# there is no cycle in graph
    
