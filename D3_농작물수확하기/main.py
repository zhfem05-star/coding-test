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
    우선 가운데에서 부터 시작
    반복문 시작
    deque()에 있는 값 popleft()
    반복문2 시작
    loop에서 pop한 변수의 위치를 directions에 맞게 조건문 작성
    조건문 시작
    (방향 연산 후 1이상 n 이하에 들어가는지)
    (루트 체크에 0인지)
    을 짜서 방향마다 순회(약 4회 연산)
    조건에 맞으면 해당 위치와 값을 deque에 넣고(여기서 가중치 ++)(rote_check도 체크)
    조건문 종료
    반복문2 종료
    반복문 끝


"""

import sys
sys.stdin = open("./input.txt", "r")


def main():
    pass

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    pass

a = 1

for i in range(1,49+1):
    a *= i

print(a)
    
