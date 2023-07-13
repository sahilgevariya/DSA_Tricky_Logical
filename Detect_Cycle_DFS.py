
# Run this from every node
visited, pathVisited = [False]*n,[False]*n
graph = defaultdict(set)    # fill this graph as adjacency List

def cycleDetected(node):
    visited[node] = True
    pathVisited[node] = True    # add to current path
    
    for nei in graph[node]:
        if not visited[nei]:
            if cycleDetected(nei):
                return True
        elif pathVisited[nei]:  # if nei is visited and its in same path -> cycle
            return True
    
    pathVisited[node] = False   # remove from current path
    return False
