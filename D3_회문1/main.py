"""
Args:
    int_(str): 회문 문자열 길수
    list_(str): 2차원 문자배열

Returns:
    answer(int): 문자열 길이만큼의 회문들 cnt
    print(str): f"#{test_case} {answer}"

제약사항:
    python: 30초
    2차원 배열 크기: 8*8
    회문 길이: 1 <= n <= 8

규칙:
    aba와 같이 거꾸로 해도 같은 문자를 회문
    이를 조건으로 int_값의 길이를 갖는 회문 문자를
    가로 세로로 찾기

가정:
    for문으로 가로 한 번 탐색(행 내려가기 1번, 리스트 탐색 1번)
    2중 for문으로 세로문자열 탐색(열 탐색 1번 행 내려가기1 번)
    회문 체크는 deque에 넣고 슬라이딩 윈도우로 매번 체크하는 방식

의사코드:
Args:
    len_hm(int): 회문 길이
    list_(list(list(str)): 공백 구분자 없는 2차원 글자배열이었으나,
    그냥 str 원소로 갖는 1차원 배열로 쓰자고 생각했으나
    그냥 편집하기 편하게 리스로 다시 바꿈
Returns:
    answer(int): 회문 cnt


deque_ = deque() # 슬라이딩 윈도우 하려 했는데 그냥 매번 배열 갱신하기로함
answer = 0
# 귀찮음 이슈 + 넉넉한 제약사항
    for i in range(8):
        for j in range(8 - len_hm): # 가로 탐색
            if list_[i][j:j+len_hm] == list_[i][j:j+len_hm:-1]:
                answer += 1

회고:
    deque 자체가 슬라이스를 지원 안 하는줄 모름.. 애초에 itertools에서 isslice 쓰면 되긴 하지만
    deque는 양끝 탐색을 빠르게 한다는 구조 설계로 인해 구현은 가능하지만 최대한 양끝에만 쓰게 설계된 셈
    그래서 슬라이드를 따로 지원하지 않으니 isslice를 사용 or 그냥 리스트로 구현 방향으로 감
    그리고 map이나 reversed는 razy evaluation이라고, __next__ 메서드가 실행되지 않으면 그냥 map 객체의 주소만 보여줌.
    그냥 해당 함수의 위치만 참조함
"""

import sys
sys.stdin = open("./input.txt", "r")

from collections import deque

def main(len_hm: int, list_: list) -> int:
    """_summary_

    Args:
        len_hm (int): 회문의 길이
        list_ (list(list(int))): 2차원 리스트

    Returns:
        int: _description_
    """
    deque_ = [] # 슬라이딩 윈도우 하려 했는데 그냥 매번 배열 갱신하기로함
    # 귀찮음 이슈 + 넉넉한 제약사항
    answer = 0

    for i in range(8): # 가로 탐색 행 탐색
        for j in range(8 - (len_hm - 1)): # 열 탐색
            # print(list_[i][j:j+len_hm])
            # print(list(reversed(list_[i][j:j+len_hm])))
            if list_[i][j:j+(len_hm)] == list(reversed(list_[i][j:j+(len_hm)])):
                # print(list_[i][j:j+len_hm])
                answer += 1
    # 테스트1 결과 가로 탐색: 7개
    
    for i in range(8): # 세로 탐색. 열 탐색
        deque_ = []
        for j in range(8): # 행 탐색
            deque_.append(list_[j][i])
            # print(deque_)
            if len(deque_) == len_hm:
                if deque_ == list(reversed(deque_)):
                    # print(list(deque_))
                    answer += 1
                    deque_.pop(0)
                else:
                    deque_.pop(0)
    
    return answer

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
test_case = 1

while True:
    try:
        line = input()
    
    except EOFError:
        break
    
    a = int(line)
    b = [list(input()) for row in range(8)]
    
    print(f"#{test_case} {main(a, b)}")
    test_case += 1