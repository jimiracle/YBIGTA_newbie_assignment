from __future__ import annotations
import copy
from collections import deque
from collections import defaultdict
from typing import DefaultDict, List


"""
TODO:
- __init__ 구현하기
- add_edge 구현하기
- dfs 구현하기 (재귀 또는 스택 방식 선택)
- bfs 구현하기
"""


class Graph:
    def __init__(self, n: int) -> None:
        """
        그래프 초기화
        n: 정점의 개수 (1번부터 n번까지)
        """
        self.n = n
        self.neighbor_list : DefaultDict[int, list[int]] = DefaultDict(list)

    
    def add_edge(self, u: int, v: int) -> None:
        """
        양방향 간선 추가
        """
        # 구현하세요!
        self.neighbor_list[u].append(v)
        self.neighbor_list[v].append(u)
    
    def dfs(self, start: int) -> list[int]:
        """
        깊이 우선 탐색 (DFS)
        
        구현 방법 선택:
        1. 재귀 방식: 함수 내부에서 재귀 함수 정의하여 구현
        2. 스택 방식: 명시적 스택을 사용하여 반복문으로 구현

        스택 방식으로 dfs 구현
        visited : 방문한 노드
        result : dfs 수행 최종 결과
        stack : 인접한 노드 들어갈 순서 정해주는 stack
        """
        # 구현하세요!
        visited = set()
        result = []
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in sorted(self.neighbor_list[node], reverse= True):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result
    
    def bfs(self, start: int) -> list[int]:
        """
        너비 우선 탐색 (BFS)
        큐를 사용하여 구현

        큐 방식으로 bfs 구현
        visited : 방문한 노드
        result : bfs 수행 최종 결과
        queue : 인접한 노드 들어갈 순서 정해주는 queue
        """

        queue = [start]
        visited = set()
        result = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in sorted(self.neighbor_list[node], reverse= False):
                    if neighbor not in visited:
                        #result.append(neighbor)
                        queue.append(neighbor)
        return result
            
    
    def search_and_print(self, start: int) -> None:
        """
        DFS와 BFS 결과를 출력
        """
        dfs_result = self.dfs(start)
        bfs_result = self.bfs(start)
        
        print(' '.join(map(str, dfs_result)))
        print(' '.join(map(str, bfs_result)))
