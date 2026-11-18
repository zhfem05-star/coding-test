"""
Args:
1
ti
Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasics ...
2
ing
Thedoublehelixformsthestructuralbasisofsemi-conservativeDNAreplication.1,2Less ...
...
    test_case: 테스트 케이스 idx
    grep_str: 포착해야 하는 단어
    str_: 뒤져야 하는 문자열

Returns:
    answer(int): grep_str이 str_ 안에 얼마나 들어있는지 cnt

제약사항:
    python 30초
    테스트케이스 10개
    문장의 길이 1000개
    grep_str의 길이 10자 이내

규칙:
    grep_str 찾아서 cnt

가정:
    우선 aaaa에서 aa찾기 같은 경우는 그냥 겹치는 것 고려해서 찾는다고 생각함
    슬라이딩 윈도우 기법으로 찾고 조건 맞을 때마다 cnt ++ 하는 방향으로 구현

회고:
    join은 str 클래스 메서드로 파라미터로 들어가는 리스트 안의 값을 이어 붙이는데
    이 때 join에 쓰인 인스턴스 문자열을 받아 해당 문자열을 구분자로 하여 str으로 변환해줌
    "".join([1,2,3])이면 "123"이런 식으로 붙이고, "-".join([1,2,3])이면 "1-2-3"으로 변환
    즉 str 메서드지만 파라미터로 리스트를 받고 사실상 인스턴스 자체도 파라미터로 받는 느낌으로 활용 가능
    그리고 운영체제마다 띄어쓰기 다르니 뭔가 output 안 맞는다? strip()써서 공백 지우셈
"""

import sys
sys.stdin = open("./input.txt", "r", encoding="utf-8")

from collections import deque

def main(str_: str, grep_str: str) -> int:
    count = 0
    grep_que = deque() # 슬라이딩 윈도우
    str_que = [i for i in str_] # 뒤져야 할 문자열
    grep_ = [i for i in grep_str] # grep 문자열

    for i in str_que:
        grep_que.append(i)
        if len(grep_que) == len(grep_):
            if "".join(grep_que) == "".join(grep_):
                count += 1
                grep_que.popleft()
            else:
                grep_que.popleft()
        else:
            pass

    return count



# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
while True:
    try:
        line = input()

    except EOFError:
        break

    test_case = line

    grep_str = input()

    str_ = input()

    print(f"#{test_case} {main(str_, grep_str)}")
