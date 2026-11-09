"""
Args:
    test_case(str): 테스트 케이스 넘버
    str_list(str): " "로 나뉘어져 있는 배열을 줌

Returns:
    answer(int): 최대 값이 되는 집합

제약사항:
    python만 30초
    100*100의 배열
    integer의 범위를 넘어가지 않음
    테스트 케이스 10
규칙:
    배열의 행, 열, 대각선 중 가장 합이 큰 집합을 구하라
    같은 합이면 둘 중 하나만 출력

가정:
    각 집합의 값은 어떻게 계산하는가?
    행으로 모두 계산하면 100 * 100번 순횐 = 10000
    각 열로 모두 계산하면 100 * 100번 순환 = 10000
    대각선은 두 번 100 * 2 = 200
    최대 테스트 케이스 1번당 20200 연산
    그냥 max로 구하면 되겠는데? 20만번 연산 밖에 안 되네
    대각선 연산은 각 순회마다 i를 대각선 연산에 쓰고(for문마다 대각선1 += i, 대각선2 += list_[n - i]
    우선 각 집합의 합은 list나 set에 넣어두고 max(set_)으로 계산하면 되지 않을까?

의사 코드:
    loop strat:
    각 행 for문으로 읽기 -> 합하기(겸사 대각선 값도 매번 갱신해주기) -> 집합에 넣기
    각 행 마지막 체크하고 지금까지 더한 대각선 합도 같이 set에 넣어주기
    loop end

    집합에서 가장 큰 값 max(set_)으로 꺼내기

"""

import sys
sys.stdin = open("./input.txt", "r")


def main(list_: list) -> int:
    """
    Args:
        list_(list(list(int))): 2차원 리스트 값

    Returns:
        answer(int): 최댓값

    variables:
        set_(set): 집합의 합에 대한 집합
        daegak_1(int): 왼쪽 대각선 값
        daegak_2(int): 오른쪽 대각선 값
    """
    daegak_1 = 0
    daegak_2 = 0
    list_selo = [0] * 100
    cnt = 0
    set_ = set()
    for i in range(len(list_)): # 가로 계산 + 대각선 계산. 시간복잡도 O(N)
        set_.add(sum(list_[i]))
        daegak_1 += list_[i][i]
        daegak_2 += list_[i][-(i+1)]

    for j in range(len(list_selo)): # 세로 계산. 시간복잡도 O(N^2) 하지만 그래봤자 100 * 100 이라 괜찮음
        for x in range(len(list_)):
            list_selo[j] += list_[x][j]
            cnt += 1
        set_.add(list_selo[j])

    set_.add(daegak_1)
    set_.add(daegak_2)
    return max(set_)


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
while True:
    try:
        line = int(input())

    except EOFError:
        break

    a = int(line)
    b = [list(map(int,input().split())) for row in range(100)]

    print(f"#{a} {main(b)}")

    # print(f"{a}")
    
