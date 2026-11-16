"""
Args:
2
1
2
    test_case_cnt(str): 테스트 케이스의 수
    int_(str): 자연수 1~10

Returns:
#1 1
#2 0
    answer(int): 퀸 N개를 서로 공격할 수 없는 경우의 수

제약사항:
    python 8초
    10개의 테스트 케이스
    체스판은 n*n, 1<=n<=10

규칙:
    n*n의 체스판에서 퀸들이 서로 공격하지 못하는 경우의 수 구하기
    여기서 퀸의 수는 n개

가정:
    체스판 안에 모든 퀸을 넣어야 함
    만약 특정 배열에서 퀸을 i 번째에 골랐다면
    같은 열은 절대 안 되고, 같은 행? 애초에 다른 행으로 넘어가서 의미 없고, 대각선은 어떻게 판별할까?
    각 스택마다 route_check를 갱신하는 방식이 제일 일 듯

의사코드:
    depth를 통해 깊이 탐색
    route_check_tmp = route_check 깊은 복사
    route_check[depth] 안에 0이 없다? -> return 0

    depth가 n이다?
        그런데 route_check 안에 0이 있다? return 1
        아니다? return 0


    for i in rnage(n):
        퀸을 둔 곳 기준으로 못 두는 곳 route_check 로직 시행
        answer += dfs(depth + 1, route_check_tmp)

회고:
    구조화를 해서 풀려했는데, 내 방식은 그것에 잘 안 맞나 봄.
    조건이나 제약, 써야하는 알고리즘을 생각 나는 구현 방법으로 먼저 작성. 거기에 살을 덧붙여서 완성하는 느낌
    결국에는 for문 쓰는 것이 편하다는 의미
    그리고 대각선 루프 구현에서 막힘. 방향성은 알았지만 머리가 안 굴러가서 구현 못함
    변수 초기화 문제로 첫 루프에서의 퀸 위치를 초기화하지 않아서 문제가 생김

"""

import sys
sys.stdin = open("./input.txt", "r")

def dfs(depth: int, route_check: list, goal: int):
    """
    :param depth: 행, 계산의 깊이
    :param route_check: 받는 루트체크 리스트(가지치기 조건)
    :param goal: 종료 조건
    :return: 1
    """
    answer = 0

    if depth > goal - 1: # out of index 방지
        return 0

    if 0 not in route_check[depth]:
        return 0

    if depth == goal - 1:
        return 1

    # 각각 아래 왼쪽 대각선, 오른쪽 대각선, 밑에 열
    directions = [
        (1, -1),
        (1, 1),
        (1, 0)
    ]

    for i in range(goal): # 열 길이 만큼 반복
        if route_check[depth][i] != 0:  # 추가: 막힌 칸이면 건너뜀
            continue
        route_check_tmp = [row[:] for row in route_check]
        # 여기에 route_check를 대각선으로 해야하는데 어떻게 구현하지?
        # while이나 for문으로 재귀적 구현?
        # 퀸의 현재 위치는 route_check[depth][i], 이를 기준으로 대각과 열을 모두 1로 만들어야 함
        for d_row, d_col in directions:
            r = depth + d_row
            c = i + d_col
            while 0 <= r < goal and 0 <= c < goal:
                route_check_tmp[r][c] = 1
                r += d_row
                c += d_col

        answer += dfs(depth + 1, route_check_tmp, goal)

    return answer

def main(n: int) -> int:
    """

    :param n: 칸 수
    :return: 경우의 수
    """
    route_check = [[0] * n for i in range(n)]

    return dfs(0, route_check, n)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())

    print(f"#{test_case} {main(n)}")
