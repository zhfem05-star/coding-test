"""
Args:
1
5 16
1 3 3 5 6
    test_case_cnt(str): 테스트케이스의 수
    n, goal(str): 총 직원 수, 목표로 하는 최소한의 값
    list_(str): 각 직원들의 키

Returns:
#1 1
    answer(int): 직원들의 키 조합 중 goal 이상이면서 가장 작은 값과의 차이

제약사항:
    python 4초
    테스트케이스는 총 10개
    N, B(1 ≤ N ≤ 20, 1 ≤ B ≤ S)
    점원의 키는 1 ~ 10000

규칙:
    N명의 직원들의 키를 합쳐서 B(goal)보다 높은 값 중 가장 작은 값을 구한 다음
    answer - B를 해서 나오는 값을 return

가정:
    문제 자체는 백트래킹 완전탐색 문제
    모든 경우의 수를 구하고 최솟값을 갱신하는 방식으로 가면 됨

회고:
    for i+1로 인덱스 슬라이싱하기 보단 그냥 min이나 max 갱신하는 문제라
    이전에 썻던 첫 원소를 고르냐 마냐의 접근으로 품
    그리고 inf는 그냥 inf쓰면 끝날 줄 알았는데, float('inf')라고 해야 끝남
"""


import sys
sys.stdin = open("./input.txt", "r")

def dfs(list_: list, goal: int, cur_sum: int) -> int:
    """
    이전에 이미 더해서 넘어와졌다는 상황
    :param list_: 남은 리스트
    :param goal: 목표 키
    ;param cur_sum: 지금까지 합친 키
    :return: min(dfs(선택), dfs(미선택))
    """
    # 첫 진입에 체크해야할 사항은?
    if cur_sum >= goal:
        return cur_sum

    if not list_: # 만약 리스트가 남아있지 않다면? 모든 키를 합해도 goal보단 작지만 더할 것도 없음
        return float('inf')

    return min(dfs(list_[1:], goal, cur_sum + list_[0]), dfs(list_[1:], goal, cur_sum))

def main(n: int, b: int, list_: list) -> int:
    """

    :param n: 직원의 수
    :param b: goal
    :param list_: 점원 키 리스트
    :return: b와 answer의 값 차이
    """
    answer = dfs(list_, b, 0)
    return answer - b


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, b = map(int, input().split())
    list_ = list(map(int, input().split()))
    print(f"#{test_case} {main(n, b, list_)}")
    # print(n, b, list_)