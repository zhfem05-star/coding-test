"""
Args:
    첫 째줄:
        {test_case} {길_총개수}
    그 다음 줄:
        list_(str): 띄어진 문자열로 주어짐. 순서쌍을 나타나는데 내가 알아서 나누라 함

Returns:
    answer(int): 가능여부를 나타내는 값, A에서 B로 갈 수 있으면 1, 아니면 0
    print(str): #{test_case} {answer}
    
제약사항:
    테스트케이스 10개
    노드는 총 100개
    노드 별 길은 총 2개(fan out만) -> 약 길만 200개
    
규칙:
    0에서 99로 갈 수 있는 길이 있는지 판별하는 문제
    노드별 경로는 (1, 2) -> 1에서 2로 갈 수 있음
    이런 식으로 표현되며 역주행 안됨. 단방향
    길은 최대 2갈래

가정:
    만약 푼다면 list_에서 받은 애들 먼저 () 씌우고, 그 다음 이걸 dict에 모두 등록
        등록은 for 문으로 i가 홀수 짝수인지 확인하고 짝수면 이전 원소 dict[이전원소].append(지금원소)
        이런식으로 진행
    {1: [2, 3]} 이런 식으로 등록하고 for 문으로 해당 노드 찾아가고, 찾아가면 pop하고
    찾아간 노드에 길이 있으면 이걸 재귀적으로 반복
    하다가 길이 없다면? 조건문으로 return None을 하던지 끝에 None을 넣어서 돌아가기
    이런 식으로 하다가 만약 키가 99? return 1
    
의사코드:
    list_ = 1차원 숫자 리스트. 이걸 기반으로 전부 dict 등록
    dict_ = defaultdict 쓸까 하다가 그냥 진행
    
회고:
    내가 dfs에 약하다는 것을 체감한 문제
    dfs로 재귀를 돌릴 때는 꼭 목적지로 갔을 때 값을 돌려받을 수 있는 변수가 필요함
    그리고 상태를 계속 갱신하기 위한 자료가 필요함
    dict 자료 구조는 if not으로 있고 없고를 판단 불가
    ex) if not dict_[list_[i-1]]: 이러면 안 됨
    ex) if list_[i-1] not in dict_ 이런 식으로 해야 해당 키가 있는지 없는지 체크 가능
"""

import sys
sys.stdin = open("./input.txt", "r")

from collections import deque

def dfs(dict_: dict, key_: int) -> int:
    """
    queue 안에 있는 값을 받고 그걸 dict에서 찾고 찾은 걸 queue에 넣고
    그걸 다시 dict에서 찾고...
    이 과정을 반복하기 위한 함수 
    """
    deque_ = deque()
    deque_.append(dict_[key_])
    dict_[key_] = []
    a = 0
    # print(f"{deque_}")
    for i in deque_:
        for j in i:
            # print(j)
            if j not in dict_:
                if j == 99:
                    # print("99에 닿음!")
                    return 1
                else:
                    continue
            else:
                a += dfs(dict_, j)
    
    if a >= 1:
        return 1
    
    return a

def main(list_: list) -> int:
    dict_ = {}
    
    
    for i in range(len(list_)):
        if i % 2 != 0:
            if list_[i-1] not in dict_: # key는 not이 아니라 in
                dict_[list_[i-1]] = []
                dict_[list_[i-1]].append(list_[i])
            else:
                dict_[list_[i-1]].append(list_[i])
    # print(dict_)
    answer = dfs(dict_, 0)
    

    return answer
    
while True:
    try:
        line = input()
    except EOFError:
        break
    
    test_case, edge_cnt = line.split()
    
    list_ = list(map(int, input().split()))
    
    # print(f"test_case: {test_case}, edge_cnt: {edge_cnt}\n{list_}")
    # print(main(list_))
    print(f"#{test_case} {main(list_)}")
    
