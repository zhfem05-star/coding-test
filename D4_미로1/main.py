"""
Args:
    test_case(str): 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 
    list_(str): 바로 다음 줄에 테스트 케이스가 주어진다. 띄어쓰기가 없는 0,1,2,3으로 이뤄진 숫자 미로


Returns:
    #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도달 가능 여부를 1 또는 0으로 표시한다 (1 - 가능함, 0 - 가능하지 않음)

제약사항:
    python만 30초
    가로 세로 16 * 16의 2차원 배열 미로 전부 탐색
    총 10개의 테스트케이스가 주어진다.
    256칸에 대해서 4번 방문하는 경우 = 약 1000 연산
    BFS를 사용
    
규칙:
    1은 막힌 곳 0은 뚫린 곳, 2는 시작점, 3이 도착점
    도착이 가능하면 1, 아니면 0으로 표시

가정:
    우선 메인 함수 전부 끝내면 0으로 출력하지만, if 3이면 1 출력하는 식으로 구현
    처음에 2찾고, 거기서 갈 수 있는 곳 체크하면서 deque에 넣어서 popleft -> 이동 후 큐에 넣기 반복
    
의사코드:
    list_ = 2차원 리스트. 미로
    route_check = 2차원 0으로 된 리스트, 방문 체크용
    deque_ = deque()
    diretions = [
            (0, 1), # 오른쪽
            (1, 0), # 밑
            (0, -1), # 왼쪽
            (-1, 0) # 위
        ]
        
    for idx, start in enumerate(list_):
        만약 start에 2가 들어 있다면?
            idx_ = start.index(2)
            start_idx = (i, idx_)
    
    a, b = start_idx
    list_[a][b] = 1
    deque_.append((a, b, list_[a][b]))
    
    while deque_:
        cur = deque_.popleft()
        cur_row, cur_col, cur_val = cur
        if cur_val == 3:
            return 1
        
        route_check[cur_row][cur_col] = 1
        
        for d_row, d_col in directions:
            if 1<= cur_row + d_row <= 16 and 1 <= cur_col + d_col <= 16 and route_check[cur_row + d_row][cur_col + d_col] != 0:
                
                deque_.append((cur_row + d_row, cur_col + d_col, list_[cur_row + d_row][cur_col + d_col]))
    
    
    return 0

회고:
    그냥 평범한 BFS 문제. 풀이 시간은 약 30분. 막힌 곳은 4방향 탐색 중 route_check까지만 조건 넣어서
    가야할 방향을 알려주지 않았음. list_안의 값이 0인 곳으로 설정해주니 정상작동
    
"""


import sys
sys.stdin = open("./input.txt", "r")

from collections import deque

def main(list_: list) -> int:
    route_check = [[0] * 16 for i in range(16)]
    deque_ = deque()
    directions = [
            (0, 1), # 오른쪽
            (1, 0), # 밑
            (0, -1), # 왼쪽
            (-1, 0) # 위
        ]
        
    for idx, start in enumerate(list_):
        if 2 in start:
            idx_ = start.index(2)
            start_idx = (idx, idx_)
    
    a, b = start_idx
    list_[a][b] = 1
    deque_.append((a, b, list_[a][b]))
    
    while deque_:
        # print(f"{deque_}")
        cur = deque_.popleft()
        cur_row, cur_col, cur_val = cur
        if cur_val == 3:
            return 1
        
        route_check[cur_row][cur_col] = 1
        
        for d_row, d_col in directions:
            if 1<= cur_row + d_row <= 16 and 1 <= cur_col + d_col <= 16 and route_check[cur_row + d_row][cur_col + d_col] != 1 and list_[cur_row + d_row][cur_col + d_col] != 1:
                
                deque_.append((cur_row + d_row, cur_col + d_col, list_[cur_row + d_row][cur_col + d_col]))
    
    
    return 0


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
while True:
    try:
        line = input()
    
    except EOFError:
        break
    
    a = line
    b = [list(map(int, input())) for _ in range(16)]
    
    print(f"#{a} {main(b)}")
