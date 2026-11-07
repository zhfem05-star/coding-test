"""
Args:
    test_case(str): 각 테스트 케이스 idx
    list_(str): 한 줄짜리 1차원 배열. 구분자는 공백. deque로 하면 시간 복잡도 낮아지니 deque로 진행

Returns:
    answer(list): 배열
    print(str): "#{test_case} {answer}"

제약사항:
    python만 30초
    주어지는 각 수는 int 범위를 넘지 않음
    마지막 암호배열은 모두 1자리 수로 구성됨
    10개의 테스트 케이스
    
규칙:
    5번씩 매번 반복
    첫 배열의 첫 원소를 -1, 그 다음 원소는 -2 ... 5번째 원소는 -5
    딱 5번만 하고 다음 루프 실행.. 반복
    그러다가 어떤 원소가 루프 중 0보다 작거나 같으면 0으로 만들고 뒤로 보낸 다음 루프 종료
    -> return 현재 배열
    
가정:
    우선 규칙이 상세해서 따로 로직이나 의사코드는 크게 생각할 필요가 없음
    형변환이 관건. main()함수에는 list(int)로 받아 값 변환이 자유롭게 하고
    출력할 때 결과 리스트를 for문으로 받아 str로 출력
    
의사코드:
    answer = ""
    a = 1
    while a:
        for i in range(1, 6):
            pop_list_ = list_.popleft()
            pop_list_ -= i
            if pop_list_ <= 0: # 종료 조건
                list_.append(0)
                a = 0
                break
            else:
                list_.append(pop_list_)
    for j in range(len(list_)):
        if j == len(list_) - 1:
            answer += str(list_[j])
        else:
            answer += str(list_[j]) + " "
            
"""

import sys
sys.stdin = open("./input.txt", "r")

from collections import deque

def main(list_: list) -> str:
    """

    Args:
        list_ (list(int)): 숫자형 배열. 형변환해서 넣으셈

    Returns:
        answer(str): list_를 공백으로 구분하는 배열로 반환. 형변환해서 출력하셈. 근데 사실 print하면 str로 형변환은 필요 없지 않나?
        그래도 명시적으로 하는 것이 좋을 듯
    """
    list_deque = deque(list_)
    answer = ""
    a = 1
    while a:
        for i in range(1, 6):
            pop_list_ = list_deque.popleft()
            pop_list_ -= i
            if pop_list_ <= 0: # 종료 조건
                list_deque.append(0)
                a = 0
                break
            else:
                list_deque.append(pop_list_)
    for j in range(len(list_deque)):
        if j == len(list_deque) - 1:
            answer += str(list_deque[j])
        else:
            answer += str(list_deque[j]) + " "
    
    return answer


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
while True:
    try:
        line = input()
    except EOFError:
        break
    
    a = line # 테스트 케이스
    b = list(map(int, input().split()))
    print(f"#{a} {main(b)}")
       
