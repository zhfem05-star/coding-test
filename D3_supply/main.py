"""
Args:
10
4
0100
1110
1011
1010
6
011001
010100
010011
101001
010101
111010
    test_case_cnt: 테스트케이스의 수
    n: 배열의 칸 수
    list_: 2차원 배열. 공백 구분자 x

Returns:
#1 2
    answer: 가장 작은 가중치 경로의 가중치 합

제약사항:
    python으로 30초
    배열의 최대 크기는 100 * 100
    시간으로 0은 할 필요가 없는 곳 -> 음수는 정의하지 않음

가정:
    다익스트라로 풀이. 가중치에 음수가 없고 heap 자료 구조 안에 넣고 최소 가중치만 골라서 가면 됨
    directions로 4방향 탐색 -> 4방향 중 가장 작은 가중치만 heappush -> heappop 반복
    route_check 넣어서 갔던 곳 또 안 가게 방지
    목적지인 (n-1, n-1)에 도착하면 return 가중치
"""

import sys

sys.stdin = open("./input.txt", 'r')

import heapq


def main(n: int, list_: list) -> int:
    """

    Args:
        n: 배열의 크기
        list_: 2차원 배열

    Returns:
        answer: 가중치 합
    """
    route_check = [[0] * n for i in range(n)]
    directions = [
        (1, 0),  # 밑
        (0, 1),  # 오른쪽
        (-1, 0),  # 위
        (0, -1)  # 왼쪽
    ]
    heap_ = [[0, (0, 0)]]

    a_val: int
    a_idx: tuple

    while True:
        a_val, a_idx = heapq.heappop(heap_)
        row, col = a_idx

        if row == n - 1 and col == n - 1:
            return a_val

        for d_row, d_col in directions:
            cur_row = row + d_row
            cur_col = col + d_col
            if 0 <= cur_row < n and 0 <= cur_col < n and route_check[cur_row][cur_col] == 0:
                heapq.heappush(heap_, [a_val + list_[cur_row][cur_col], (cur_row, cur_col)])
                route_check[cur_row][cur_col] = 1

    return -1


T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    list_ = [list(map(int, input().strip())) for i in range(n)]

    print(f"#{test_case} {main(n, list_)}")
