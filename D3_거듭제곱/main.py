"""
Args:
    1
    9 8
    2
    2 8
    ........
    test_case(str): 테스트 케이스 넘버
    str_(str): 두 수가 공백을 구분자로 주어짐
    
Returns:
    #1 43046721
    #2 256
    .......

제약사항:
    python 30초
    테스트케이스 10개
    
규칙:
    두 문자열 n m 이 주어지고 n ** m의 값을 매번 출력하는 코드를 만들어라

회고:
    아마 python은 쉽고 자바나 C의 경우에는 라이브러리를 못쓰니까 어려운 문제 같음
    python자체에는 자료형에 크기 제약을 신경 쓸 필요도, 사실 재귀 호출도 필요 없음
    재귀호출로 구현도 그리 어렵지는 않음. 다른 언어는 어려울 수도 있음
    사실 그냥 python이 코테에서 유리한 이유를 보여주는 문제
"""


import sys
sys.stdin = open("./input.txt", "r")


def main():
    pass

while True:
    try:
        line = input()
    
    except EOFError:
        break
    
    test_case = int(line)
    b = list(map(int, input().split()))
    m, n = b
    
    print(f"#{test_case} {m ** n}")
    
