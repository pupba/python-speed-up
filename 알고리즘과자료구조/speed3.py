import time
from collections import deque

# BFS 구현
def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])  # (현재 노드, 경로)
    
    while queue:
        current_node, path = queue.popleft()
        time.sleep(0.1)
        if current_node == goal:
            return path
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None  # 경로를 찾지 못한 경우

# DFS 구현
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path.append(start)
    time.sleep(0.1)
    if start == goal:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in path:
            result = dfs(graph, neighbor, goal, path)
            if result is not None:
                return result
    
    path.pop()
    return None

if __name__ =="__main__":
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'E', 'F'],
        'C': ['A', 'G', 'H'],
        'D': ['A', 'I', 'J'],
        'E': ['B', 'K', 'L'],
        'F': ['B'],
        'G': ['C'],
        'H': ['C', 'M', 'N'],
        'I': ['D'],
        'J': ['D'],
        'K': ['E'],
        'L': ['E'],
        'M': ['H'],
        'N': ['H'],
    }

    # 더 많은 노드를 추가하여 그래프를 복잡하게 만듭니다.
    for i in range(15, 30):
        graph[chr(65 + i)] = [chr(65 + i - 1), chr(65 + i - 2)]  # A-Z까지 노드 추가

    # 경로 찾기와 시간 측정
    start_node = 'A'
    goal_node = 'N'

    # BFS 시간 측정
    start_time_bfs = time.time()
    bfs_path = bfs(graph, start_node, goal_node)
    end_time_bfs = time.time()
    bfs_time = end_time_bfs - start_time_bfs

    # DFS 시간 측정
    start_time_dfs = time.time()
    dfs_path = dfs(graph, start_node, goal_node)
    end_time_dfs = time.time()
    dfs_time = end_time_dfs - start_time_dfs

    # 결과 출력
    print("BFS로 찾은 A에서 N로 가는 경로:", bfs_path)
    print(f"BFS 실행 시간:{bfs_time:.7f}")

    print("DFS로 찾은 A에서 N로 가는 경로:", dfs_path)
    print(f"DFS 실행 시간:{dfs_time:.7f}")
