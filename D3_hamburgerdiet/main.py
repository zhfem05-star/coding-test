"""
Args:
1
5 1000
100 200
300 500
250 300
500 1000
400 400
    test_case(str): 첫 줄에 나오는 테스트 케이스 넘버
    list_1(str): 공백으로 구분된 숫자. 첫 번째 줄에는 재료의 수(N), 목적 칼로리(L)가 나옴
    list_2(str): 두 번째 줄 이후에는 N개의 행만큼 맛에 대한 [점수, 칼로리]가 나옴
Returns:
#1 750	//Test Case #1의 정답
    answer(int) = 제한된 칼로리 이하를 만족하며 N개의 조합 중 맛 점수가 가장 높은 조합의 맛 점수 출력

제약사항:
    python 16초
    테스트케이스 20개
    1 ≤ N ≤ 20, 1 ≤ L ≤ 10^4
    Ti, Ki(1 ≤ Ti ≤ 10^3, 1 ≤ Ki ≤ 10^3)

규칙:
    우선 칼로리가 우선, 1000 칼로리 이하라는 조건을 만족해야 하고
    그 중에서 가장 맛 점수가 높은 놈을 갱신해야 함
    조합 개수의 제한은 없음

가정:
    16초면 꽤나 넉넉함 20개를 완전탐색한다고 해도 순서가 없고 각기 다른 애들임
    갱신해야할 값은 조건에 맞는 애들을 찾고 그 최댓값을 비교하는 과정이 필요
    즉 taste_score를 전달하고, 칼로리도 전달 넘지 않는지 체크하고 둘 다 맞으면
    return taste_score를 하기
    재귀문은 return max(dfs(), taste_score)

의사코드:
    남은 리스트, 목표 칼로리, 현재 칼로리, 맛 점수

    for 문
        dfs(list_tmp[1:], goal_cal, cur_cal + list_tmp[0][1], taste_score + list_tmp[0][0])
"""
# import math
# print(math.comb(20, 5) * 20) #견적 내보기

import sys

sys.stdin = open("./input.txt", "r")


def dfs(list_: list, goal_cal: int, cur_cal: int, taste_score: int, answer: list) -> int:
    if cur_cal > goal_cal:  # 목표 칼로리를 넘어섰다면
        return 0

    if list_:
        list_tmp = [row[:] for row in list_]
    else:
        return taste_score

    for i in range(len(list_tmp)):
        answer.append(max(dfs(list_tmp[1:], goal_cal, cur_cal + list_tmp[0][1], taste_score + list_tmp[0][0], answer), taste_score))

    return max(answer)
# def main(b: int, list_: list) -> int:
#     answer = []
#
#     for i in range(len(list_)):
#         answer.append(dfs(list_, b, ))
#
#     return max(answer)


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
while True:
    try:
        line = input()

    except EOFError:
        break

    test_case = line
    a, b = map(int, input().split())

    list_ = [list(map(int, input().split())) for _ in range(a)]

    answer = []
    # print(f"test_case: {test_case}, a, b: {a}, {b}\nlist_: {list_} ")
    print(dfs(list_, b, 0, 0, answer))