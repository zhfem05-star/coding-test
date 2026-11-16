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
    (1 ≤ N ≤ 10)

규칙:
    오른쪽 -> 아래 -> 왼쪽 -> 위의 루프를 갖는 n*n의 2차원 배열을 출력하셈

의사코드:
    list_ = [[0] * n for i in range(n)]
    list_int = [i for i in range(1, n * n + 1)]
    right_stat = 1
    down_stat = 0
    left_stat = 0
    up_stat = 0

    col_left = 0
    col_right = n # n - 1 까지 신경 쓰기
    row_up = 0
    row_down = n # n - 1 까지 신경 쓰기

    # location_row = 0
    # location_col = 0

    while list_int:
        if right_stat == 1:
            for i in range(col_left, col_right): # i는 왼쪽에서 오른쪽으로 가는 col 값
                list_[row_up][i] = list_int.pop(i)

            # # 위치 갱신
            # location_row = row_up
            # location_col = col_right

            # 배열 갱신
            row_up += 1 # 행 생김
            right_stat = 0 # 방향 종료
            down_stat = 1 # 새 방향 시작

        elif down_stat == 1:
            for i in range(row_up, row_down): # i는 위에서 아래로
                list_[i][col_right] = list_int.pop(i)

            col_right -= 1 # 오른쪽 열 생김
            down_stat = 0 # 방향 종료
            left_stat = 1 # 새 방향 시작

        elif left_stat == 1:
            for i in range(col_right, col_left, -1): # i는 오른쪽에서 왼쪽으로
                list_[row_down][i] = list_int.pop(i)

            row_down -= 1 # 맨 밑에 열 생김
            left_stat = 0 # 방향 종료
            up_stat = 1 # 새 방향 시작

        elif up_stat == 1:
            for i in range(row_down, row_up, -1): # i는 아래에서 위로
                list_[i][col_left] = list_int.pop(i)

            col_left += 1 # 왼쪽에 열 생김
            up_stat = 0 # 방향 종료
            right_stat = 1 # 새 방향 시작

        else:
            print("예상치 못한 에러")
            raise

회고:
    구현도 애먹었고, 출력도 애먹음
    출력의 경우 \n하고 공백을 마지막에는 없애야 하고
    main 함수를 return print하면서 print(main())을 해버리면 사이에 None이 나온다는 점을 처음 알게 됨
    구현의 경우에는 직접 디버깅 돌려보면서 틀린 점 찾아보고, 일일히 고쳐나감
    range같은 형식으로도 역순회는 가능하지만 반드시 범위 순서도 반대로 적어야 함
    ex) range(10, 1, -1) -> 10~2 까지 진행
"""


import sys
sys.stdin = open("./input.txt", "r")


def main(n: int) -> str:
    list_ = [[0] * n for i in range(n)]
    list_int = [i for i in range(1, n * n + 1)]
    right_stat = 1
    down_stat = 0
    left_stat = 0
    up_stat = 0

    col_left = 0
    col_right = n - 1  # n - 1 까지 신경 쓰기
    row_up = 0
    row_down = n - 1  # n - 1 까지 신경 쓰기

    # location_row = 0
    # location_col = 0

    while list_int:
        if right_stat == 1:
            for i in range(col_left, col_right + 1):  # i는 왼쪽에서 오른쪽으로 가는 col 값
                list_[row_up][i] = list_int.pop(0)

            # # 위치 갱신
            # location_row = row_up
            # location_col = col_right

            # 배열 갱신
            row_up += 1  # 행 생김
            right_stat = 0  # 방향 종료
            down_stat = 1  # 새 방향 시작

        elif down_stat == 1:
            for i in range(row_up, row_down + 1):  # i는 위에서 아래로
                list_[i][col_right] = list_int.pop(0)

            col_right -= 1  # 오른쪽 열 생김
            down_stat = 0  # 방향 종료
            left_stat = 1  # 새 방향 시작

        elif left_stat == 1:
            for i in range(col_right, col_left - 1, -1):  # i는 오른쪽에서 왼쪽으로
                list_[row_down][i] = list_int.pop(0)

            row_down -= 1  # 맨 밑에 열 생김
            left_stat = 0  # 방향 종료
            up_stat = 1  # 새 방향 시작

        elif up_stat == 1:
            for i in range(row_down, row_up - 1, -1):  # i는 아래에서 위로
                list_[i][col_left] = list_int.pop(0)

            col_left += 1  # 왼쪽에 열 생김
            up_stat = 0  # 방향 종료
            right_stat = 1  # 새 방향 시작

        else:
            print("예상치 못한 에러")
            raise
    answer = ""

    for i in list_:
        for j in i:
            if j == i[len(i) - 1]:
                answer += str(j)
            else:
                answer += str(j) + " "

        if i == list_[len(list_) - 1]:
            continue

        else:
            answer += "\n"

    return answer


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input().strip())
    print(f"#{test_case}\n{main(n)}") # print하고 main함수도 return으로 print하니 #{test_case} 사이에 None이 낌