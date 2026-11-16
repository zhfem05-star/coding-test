"""
Args:
2
3
4
    test_case_cnt: 테스트 케이스 수
    int_: 달팽이의 크기. 3이면 3*3의 2차원 배열의 달팽이 만들어야 함

Returns:
#1
1 2 3
8 9 4
7 6 5
#2
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
    answer(str): 저런 식으로 달팽이 모양의 2차원 배열을 print 해야 함. 아마 for문으로 하나씩 print할 듯

제약사항:
    테스트케이스 10개
    python 30초

규칙:
    오른쪽 -> 아래 -> 왼쪽 -> 위의 루프를 갖는 n*n의 2차원 배열을 출력하셈

의사코드:
    list_ = [[0] * n for i in range(n)]
    for i in range(n):
        처음엔 n-i로 내려가면서 1이 되면 마지막이 딱 채워지는 구조

"""


import sys
sys.stdin = open("./input.txt", "r")


def main(n: int) -> str:

    pass

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input().strip())
    print(f"#{test_case}\n{n}")