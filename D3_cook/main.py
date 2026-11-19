"""
Args:
10
4
0 5 3 8
4 0 4 1
2 5 0 3
7 2 3 0
…

// 총 테스트 케이스의 개수 T = 10

// 첫 번째 테스트 케이스, N = 4, 본문 예제

// S11, S12, S13, S14

// S21, S22, S23, S24

// S31, S32, S33, S34

// S41, S42, S43, S44

    test_case_cnt: 테스트 케이스 수
    n: 식재료의 수
    list_: 맛 시너지 배열표 (2차원) 공백으로 구분됨

Returns:
    answer: 음식간의 맛 차이가 가장 작은 케이스(식재료끼리는 서로 달라야 함) 어떤 식재료로 만들건지 안 알려줌

제약사항:
    식재료는 4<= n <= 16
    음식의 식재료가 서로 같은 경우는 값이 없음

규칙:
    식재료 N개가 주어지고 서로 다른 식재료들을 통해 2개의 음식을 만들어 내야 함
    음식에 들어가는 식재료는 N/2개(N은 무조건 짝수). 그런데 문제 설명이 거지 같은 부분이 있음
    우선 음식 식재료는 음식 하나에 i와 j, 즉 두 종류만 들어간다고 가정
    여기서 식재료 아무거나 2개(같으면 x)로 만드는 음식의 맛의 차이가 최소가 될 때 그 차이를 return
    음식의 맛은 (i,j), (j,i) idx에 있는 값을 더해서 산정

가정:
    완전 탐색 문제. 단 음식의 맛 조합은 사실상 순열이 아닌 조합으로 판단해야 함
    조합상 나오는 두 개의 순열 내의 값을 더하고, 그걸 dict에 저장하는 방식으로 계산하면 됨
    우선 조합 배열 ij_list 만들고 리스트를 통해 sij, sji 두 값을 더해서 값 합 구하기
    여기서 나온 음식들 조합으로 차이 최솟값 완전탐색

의사코드:
    조합 다 찾고
    음식 별로 음식 a - b를 최솟값으로 갱신하는 함수가 필요
    즉 comb로 구하는 조합은 사실상 선택, 순서 리스트이고, 여기서 선택하냐 아니냐의 갈림길

회고:
    문제 자체의 이해가 어려웠던 케이스
    설명은 똑바로인데 이해하는데 오래 걸리고 조합이나 이런 도구는 별로 안 써봐서
    AI 사용해서 품


"""

import sys
sys.stdin = open("./input.txt", "r")

from itertools import combinations


def taste(group: tuple, S: list) -> int:
    """그룹 안의 모든 재료 쌍의 시너지 합"""
    total = 0
    for i, j in combinations(group, 2):
        total += S[i][j] + S[j][i]
    return total


def solve(n: int, S: list) -> int:
    answer = float('inf')
    all_set = set(range(n))

    for group_a in combinations(range(n), n // 2):
        if 0 not in group_a:      # A↔B 바뀐 중복 경우 제거
            continue
        group_b = tuple(all_set - set(group_a))

        diff = abs(taste(group_a, S) - taste(group_b, S))
        answer = min(answer, diff)

    return answer


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    S = [list(map(int, input().split())) for _ in range(n)]
    print(f"#{test_case} {solve(n, S)}")