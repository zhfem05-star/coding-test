"""
Args:
    T(str): 테스트 케이스 개수
    N(str): 가로 세로 길이
    list_(str): 2차원리스트 지도
Returns:
    answer(int): 최소 누적치
제약조건:
    python만 30초 -> 생각보다 시간이 오래 걸릴 수 있음
    2차원 배열(지도) 크기 -> 최대 100 * 100
    bfs로 가면 뭔 레벨이 너무 깊음. 모든 경우의 수에 대해 계산이 필요하다고 봄
    따라서 그리디 알고리즘으로 최대한 조건에 맞는 노드로만 진행하는 것이 맞다고 봄 -> 다익스트라로 진행

규칙:
    단순하게 매 칸 가중치를 누적하면서 heapq에 push하고 가장 작은 값만 빼내면서 해당 노드 근처만 탐색
    앞으로 진전은 우선 범위 체크, 진행한 적이 없으면 진행하고 heappush로 해당 노드 push(?)
    아니 근데 가장 작은 값이 heapq에 들어가는데, 그 값으로 탐색하면 결국 같은 값을 같는 노드가 2개 이상이면?
    이러면 나가리임. 따라서 heapq에 전진한 노드의 키(x,y)와 값이 둘 다 들어가야 함

의사코드:
    direction = [
        (1, 0), # 아래
        (0, 1), # 오른쪽
        (-1, 0), # 위
        (0, -1) # 왼쪽
    ]
    heapq = [0, (0,0)]
    route_check = [[0] * n for _ in range(n)]
    while heapq:
        a_val, a_idx = heapq.heappop()
        row, col = a_idx.split() # 현재 row, col
        route_check[row][col] = 1
        for drow, dcol in direction:
            if 0 <= row + drow <= n and 0 <= col + dcol <= n and route_check == 0:
                heapq에 이 위치에 있는 애들 누적치 값을 heapq에 push하기
"""
import sys
sys.stdin = open("./input.txt", "r")

import heapq

def main(n: int, list_: list) -> int:
    """

    Args:
        n (int): 가로 세로 길이
        list_ (list(list)): 실제 2차원 리스트 좌표

    Returns:
        int: 최소 누적치
    """
    if n == 1:
        return 0
    direction = [
            (1, 0), # 아래
            (0, 1), # 오른쪽
            (-1, 0), # 위
            (0, -1) # 왼쪽
        ]
    heapq_ = [[0, (0,0)]]
    route_check = [[0] * n for _ in range(n)]
    while heapq_:
        a_val, a_idx = heapq.heappop(heapq_)
        row, col = a_idx # 현재 row, col
        if row == n-1 and col == n-1:
            return a_val
        if route_check[row][col] != 0:
            continue
        else:
            route_check[row][col] = 1
        for drow, dcol in direction:
            if 0 <= row + drow <= n-1 and 0 <= col + dcol <= n-1 and route_check[row + drow][col + dcol] == 0:
                heapq.heappush(heapq_, [a_val + list_[row + drow][col + dcol], (row + drow, col + dcol)])
                
                

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = int(input())
    b = [list(map(int, input().strip())) for _ in range(a)]
    print(f"#{test_case} {main(a, b)}")
    
