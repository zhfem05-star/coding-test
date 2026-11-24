"""
Args:
2
3
2 3 5
10
1 1 1 1 1 1 1 1 1 1
    test_case_cnt: 테스트 케이스 수
    n: 문제 개수
    list_: 문제 점수 배점

Returns:
#1 7
#2 11
    answer: 가능한 시험 점수 경우의 수

제약사항:
    python 4초
    1<= n <= 100
    2 ^ 100도 가능한 경우의 수 아마 이 방식은 아닐 듯
    테스트 케이스는 총 40개
    근데 배점이니까 점수가 중복되니 set으로 중복 줄이면?

규칙:
    문제 배점에서 가능한 모든 조합을 찾고, 그 경우의 수를 반환하라

가정:
    level = n
    만약 처음에 모든 어떤 문제 하나를 틀리거나 맞은 점수를 set에 넣고
    그 다음 루프에서 그 점수를 기반으로 또 한 번 모든 문제가 틀리거나 맞을 점수를 또 set에 넣고
    그렇게 모든 경우를 n번 시행 -> 이러면 나올 수 있는 경우의 수의 중복을 제거하면서 총 경우의 수를 확인 가능

의사코드:

    level = {0}

    for _ in range(k): # k 번 만큼
        nxt = set()
        for score in level: # level 안에 있는 원소를 받고
            cur = score
            for i in range(k): # 그 원소를 i 번째 값과 더한 경우의 수를 nxt라는 set에 저장
                nxt.add(list_[i] + cur)
                nxt.add(cur)

        level = nxt

"""

from itertools import combinations

import sys

sys.stdin = open("./input.txt", "r")


def main(list_: list, k: int) -> int:
    level = {0}  # 숫자 합을 넣는 set

    for i in list_:  # list_내의 문제마다 시행
        nxt = set()
        for score in level:
            nxt.add(i + score)
            nxt.add(score)

        level = nxt

    return len(level)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    k = int(input())
    list_ = list(map(int, input().split()))
    print(f"#{test_case} {main(list_, k)}")

# if __name__ == "__main__":
#     a = [str(i) for i in range(100)]
#     print(" ".join(a))

