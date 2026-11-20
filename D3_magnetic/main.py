"""
Args:
100
1 0 0 0 0 0 0 0 2 0 0 0 1 0 1 1 0 2 0 0 1 0 2 0 2 2 1 0 0 0 0 0 1 0 0 2 0 0 0 0 0 1 2 0 0 0 1 1...
0 0 0 0 0 0 0 0 0 0 1 0 0 2 0 0 0 0 0 2 0 0 1 0 0 0 0 0 1 2 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0...
0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 2 2 0 2 0 0 0 0 0 1 0 0...
0 0 0 2 0 0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 0 0 1 0 1 0 0 0 0 0 0 2 0 2 0...
0 0 0 0 2 0 2 0 0 0 2 0 0 0 0 0 0 2 1 1 0 2 0 0 0 1 2 2 2 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0...
0 0 2 0 0 0 1 1 1 0 0 0 0 0 0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0...
    n: 배열의 칸 수
    list_: 자석 놓이는 2차원 배열

Returns:
#1 471
    answer: 교착 상태에 빠지는 자석 개수

제약사항:
    python 30초
    테스트케이스 10개
    2차원 배열은 100 * 100의 크기(고정)

규칙:
    N극은 1
    S극은 2로 표현
    N극은 위로 움직이고
    S극은 아래로 움직일 때
    서로 부딪치는 교착 상태의 자석 개수 구하기

가정:
    사실 N극이 중요
    탐색하면서 N극 만나면 switch 키고(그 다음 만나던 말던은 중요 x)
    S극 이후에 만나면 cnt ++
    열탐색을 끝까지 해야 함. 도중에 만났다고 끝나면 안 됨

의사코드:
    cnt = 0
    list_tmp = [row[:] for row in list_]
    for i in range(100): # 행
        for j in range(100): # 열
            if list_tmp[i][j] == 1: # N극 찾았다면?
                if switch_1 == 0: # 스위치가 0이라면?
                    switch_1 = 1

                else: # 0이 아니라면?
                    continue

            elif list_tmp[i][j] == 2:
                if switch_1 == 1:
                    cnt += 1
                    switch_1 = 0 # 스위치 초기화 서로 충돌했으니
                else:
                    continue

    return cnt

회고:
    확실히 시간이 걸리더라도 문제 이해를 하고,
    의사코드까지 써야 제대로 된 로직이 나옴
    그리고 구하려는 것을 명확히 해야 함
    보통이라면 문제 보고 아 어떻게 저걸 다 구현하나 싶지만
    이번 문제처럼 무엇을 기준으로 결과값이 쌓여야 하는지만 명료하면
    굳이 빈공간이나 위치나, 그런 쓸데없는 부분은 구현에 필요없다는 것을 알 수 있음

"""


import sys
sys.stdin = open("./input.txt", "r")


def main(list_: list) -> int:
    """

    :param list_: 2차원 배열
    :return: cnt 수
    """
    cnt = 0
    switch_1 = 0
    list_tmp = [row[:] for row in list_] # 혹시 모르니 깊은 복사
    for i in range(100):  # 행
        switch_1 = 0
        for j in range(100):  # 열
            if list_tmp[j][i] == 1:  # N극 찾았다면?
                if switch_1 == 0:  # 스위치가 0이라면?
                    switch_1 = 1

                else:  # 0이 아니라면?
                    pass

            elif list_tmp[j][i] == 2: # S극 찾았다면?
                if switch_1 == 1: # 이전에 N극을 찾았다면?
                    cnt += 1
                    switch_1 = 0  # 스위치 초기화 서로 충돌했으니
                    # print(f"cnt: {cnt}, i: {i}, j: {j}")
                else:
                    pass

    return cnt


test_case = 1

while True:
    try:
        line = input()

    except EOFError:
        break

    n = int(line)
    list_ = [list(map(int, input().split())) for i in range(n)]

    print(f"#{test_case} {main(list_)}")

    test_case += 1