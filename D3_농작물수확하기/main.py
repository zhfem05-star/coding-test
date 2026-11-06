"""
Args:
    test_case_(str): 총 테스트 케이스 갯수
    n(str): 한 변의 길이
    list_(str): 죄다 붙어있는 n*n의 배열

Returns:
    answer(int): 마름모 안에 있는 가중치의 총 합

제약사항:
    python 4초
    테스트 케이스 50개
    1 <= N <= 49
    최대 49*49 칸을 순회 -> 이걸 매번 순회하면 절대 안 됨


규칙:
    n * n의 정사각형에서 안에 마름모를 그려 그 안에 있는 값들을 모두 더하는 문제
    즉 마름모 위치를 구하고 그 안의 값들만 더하면 됨
    농장크기는 항상 홀수

가정:
    가운데 행을 기준으로 n + n-2 + n-5 ... 이런 식으로 귀결됨
    우선 이걸로 마름모가 칠해지는 법칙을 먼저 알아야 함
    마름모 구역의 위치를 구하면(O(n)) 나머지는 idx를 통해 조회만 하면 됨으로(O(1))
    사실상 시간복잡도 n의 작업임
    첫 행 i를 기준으로
    처음에는 int(n/2) + 1 열에서 칠해지기만 하고
    이후 양 옆으로 1씩 늘어나는 구조
    이전 양 옆으로 늘어간 구조에서 1씩 더 늘어나므로
    이 위치를 저장할 변수가 필요
    그리고 이 변수를 통해 계속 갱신하면서 위치 idx 리스트에 넣다가 i == int(n/2) + 1가 되면
    반복문 종료. 여기까지가 마름모 인덱스 구하기
    그 다음 반복문으로 리스트에 있는 애들 값 조회하면서 ++ 하고 총 가중치 구하기

의사 코드:
list_idx = [] # 지금까지 찾은 마름모 범위. 나중에 따로 반복문 돌려서 값 조회용
    for i in range(1, n//2 + 2):
        if n//2 + 1 == 1: # 이건 반복문 밖으로 빼도 되기는 함
            return 1
        
        if i == n//2 + 1: # 만약 중간까지 왔다면? -> 중간 행 모두 list_idx에 추가
            for j in range(n)
                list_idx.append(list_[n//2 + 1][j])
                break
        # 만약 n이 7이고 첫행이면 [1][(7//2 + 1)#가운데 - (1//2)#최소슬라이싱:(7//2 +1)#가운데 + (1//2)#최대슬라이싱 + 1#리스트 끝값 고려 
        list_idx.append(list_[i][(n//2 + 1) - (i//2):(n//2 + 1) + (i//2) + 1])
        # 반대편 위치의 값도 더하기
        list_idx.append(list[n-i][(n//2 + 1) - (i//2):(n//2 + 1) + (i//2) + 1])
    
    answer = sum(list_idx)

회고:
    swea에선 구분자 없는 2차원 배열 문제가 나오면 strip()쓰는 것을 상시 습관화
    그리고 테스트 케이스를 확인할 때는 swea에서 제공만 하는 테스트 케이스 답만 확인하지 말고
    다른 모든 테스트 케이스의 자료형이라도 확인하자
    테스트 케이스 별로 답은 몰라도
    적어도 자료 구조라도 똑바로 되어있는지 보면 내 코드의 구멍이 있다는 사실은 알 수 있음
        
        
"""

import sys
sys.stdin = open("./input.txt", "r")


def main(n: int, list_: list) -> int:
    """_summary_

    Args:
        n (int): 한 변의 길이
        list_ (list): 2차원 배열. 도화지

    Returns:
        int: 마름모 내의 값들 총합
    """
    if n//2 + 1 == 1: # 반복문 밖으로 뺌
        return list_[0][0]
    list_sum = [] # 임시 더하기용 리스트
    list_idx = [] # 지금까지 찾은 마름모 범위. 나중에 따로 반복문 돌려서 값 조회용
    for i in range(n//2 + 2):
        
        if i == n//2: # 만약 중간까지 왔다면? -> 중간 행 모두 list_idx에 추가
            for j in range(n):
                list_idx.append(list_[i][j])
            
            break
            
        # 만약 n이 7이고 첫행이면 [1][(7//2 + 1)#가운데 - (1//2)#최소슬라이싱:(7//2 +1)#가운데 + (1//2)#최대슬라이싱 + 1#리스트 끝값 고려 
        list_idx.append(list_[i][(n//2) - i:(n//2) + i + 1])
        # 반대편 위치의 값도 더하기
        list_idx.append(list_[(n-1)-i][(n//2) - i:(n//2) + i + 1])
    
    for q in list_idx:
        if type(q) == list:
            for w in q:
                list_sum.append(w)
        else:
            list_sum.append(q)
    
    return sum(list_sum)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    list_ = [list(map(int, input().strip())) for row in range(n)]
    # if test_case == 23 or test_case == 30:
    print(f"#{test_case} {main(n, list_)}")