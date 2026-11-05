"""
Args:
    N(str): 테스트 케이스 수
    list_(str): 사다리를 나타낸 리스트

Returns
    print_(str): "#{N} {목적지에도달하는 X좌표}" 형태로 출력

제약조건:
    python만 30초
    최대 100 * 100의 사다리
    사다리 타기인 만큼 위로는 안 가고, 우선 좌우를 먼저 살피고 밑으로 감
    시작점은 첫 줄이면 됨

문제 설명:
    어느 사다리의 출발점이 목표한 위치(값 2인 곳)로 가는지에 대한 문제
    단순한 사다리 타기 로직으로 결국 값 2인 곳으로 가는 출발점의 x좌표를 구하는 문제

가정:
    우선 100 * 100의 좌표니 BFS는 아니고, 애초에 사다리 타기는 간단한 규칙으로 내려가는 로직임
    그러면 그냥 첫 줄에 있는 애들을 for문 돌려서 하나 씩 연산하면 문제가 없음
    문제는 x값하고 y값이 동일한가? 임 동일하면 도착 판별이 쉽지만 아니면 따로 도착인지 아닌지 확인하는 로직을 따로 넣어야 함
    아 문제에 100 * 100에서를 가정하고 시작하네
    그리고 x의 좌표는 1 부터 시작이 아니라 0부터 시작임

의사코드:
    for i in range(len(list_[0])):
        만약 i 값이 0이면?
            continue
        
        cur_xy = (i, 1)
        깊이_cnt = 1
            
        내려가는 로직
            현재 깊이가 마지막(100)이 맞나?
                맞았는데 2면?
                    return i
                아니면?
                    continue
            좌우에 다른 길 있으면 거길 먼저 가기(범위체크도 해야 함)
                triger = True
                while triger:
                    쭉 갔는데 더 이상 못감
                    triger = False
            없으면 밑 내려가기(범위 체크하기)
                깊이_cnt += 1
                cur_xy 갱신

회고:
    while문에서 continue가 감싸고 있는 가장 안쪽 루프에서만 벗어나게 해주는 건줄 몰름(가장 바깥쪽이라고 거꾸로 착각함)
    -> 따라서 break로 나가야 하거나 while 조건 종료나 상태 조건문으로 안전하게 나가는 것이 좋음

    얕은 복사라는 취약점에 처음 걸려봄. 2차원 리스트는 list_[:] 복사하면 바깥 리스트는 복사가 되는데, 안쪽 리스트는 객체를 공유함
    -> 따라서 이전에 지나갔던 경로가 여전히 0으로 처리되어 막다른 길이 생겨버리는 문제가 발생. 만약 제대로 복사하려면 deepcopy라는 메서드를 쓰던지
        아니면 [row[:] for row in list_]로 매 번 행을 통째로 복사한 리스트 컴프리헨션을 만들던지 해야함

"""

# import os, sys

# base = os.path.dirname(os.path.abspath(__file__))
# sys.stdin = open(os.path.join(base, "input.txt"), "r")

import sys

sys.stdin = open("./input.txt", "r")

def main(a_: list) -> int:
    """
    Args:
        list_(list(list(int))): 사다라의 형태를 담고 있는 2차원 리스트
    
    Returns:
        answer(int) = 목표에 도달하는 x의 좌표(좌표는 0부터 시작해서 n-1까지 있음)
    """
    for i in range(len(a_[0])):
        list_ = [row[:] for row in a_]
        if list_[0][i] == 0: # 만약 시작점이 0이면?
            continue
        
        cur_xy = (1, i)

        깊이_cnt = 1
        # print(f"{i}번째 시작")
        # 내려가는 로직
        while True:

            x, y = cur_xy
            if x == 99:
                if list_[x][y] == 2:
                    return i

                else:
                    break

            if 0<=y+1<100 and list_[x][y+1] != 0: # 오른쪽
                list_[x][y] = 0
                cur_xy = (x, y+1)
                # print(f"1 cur_xy = {cur_xy} x = {x} y = {y}")

            elif 0<=y-1<100 and list_[x][y-1] != 0: # 왼쪽
                list_[x][y] = 0
                cur_xy = (x, y-1)
                # print(f"2 cur_xy = {cur_xy} x = {x} y = {y}")

            elif 0<=x+1<100 and list_[x+1][y] != 0: # 아래
                cur_xy = (x+1, y)
                깊이_cnt += 1
                # print(f"3 cur_xy = {cur_xy} x = {x} y = {y}")

            else:
                print(f"예외상황 발생: cur_xy = {cur_xy} x = {x} y = {y}")
                print(f"\n list_[x][y+1] = {list_[x][y+1]}")
                print(f"list_[x][y-1] = {list_[x][y-1]}")
                print(f"list_[x+1][y] = {list_[x+1][y]}")
                raise

    return -1



# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
while True:

    try:
        line = input()
    except EOFError:
        break

    test_case = int(line)
    b = [list(map(int, input().split())) for _ in range(100)]
    # print(test_case)
    print(f"#{test_case} {main(b)}")
    # print(f"#{test_case} {b[98][47]}")
    
