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
    for문으로 가로 한 번 탐색
    2중 for문으로 세로문자열 탐색
    이러면 괜찮을 듯
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
            if list_[i][j:j+len_hm] == list_[i][j:j+len_hm, -1]:
                answer += 1

"""

import sys
sys.stdin = open("./input.txt", "r")


def main():
    pass

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    pass
    
