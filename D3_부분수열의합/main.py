"""
Args:
    1
    4 3
    1 2 1 2

    test_case(str): 테스트 케이스의 총 갯수
    str_1(str): 인자로 쓸 두 자연수. 순서대로 N, K 공백으로 나뉘어 있음
    str_2(str): 수열. 이 수열을 써서 K를 만들어야 함
    
Returns:
    #1 4
    answer(int): 수열의 합이 K가 되는 경우의 수를 cnt
제약사항:
    python 8초
    1 ≤ N ≤ 20, 1 ≤ K ≤ 1000
    테스트 케이스 수는 20개
규칙:
    N과 K, 수열 list_가 주어짐
    N은 len(list_), K는 도달해야하는 목표 값
    출력으로 k가 될 수 있는 부분 수열
    핵심은 수열 list_에서 숫자 1개 이상을 뽑아서 K가 될 경우의 수
    
가정:
    N은 1~20의 범위.
    수열의 수는 1~100
    최대 20개를 매번 모두 탐색한다고 하면 시간이 너무 오래 걸리긴 함
    하나 고르고 19개의 경우의 수를 모두 탐색, 또 하나 고르고 18개의 경우의 수를 모두 탐색..
    아마 이걸 완전탐색하려면 순서는 의미가 없을 것임
    우선 순서 상관 없으면 그냥 for문으로 수열 돌리고, 계속해서 재귀로 남은 수열 돌리는 식으로 완전탐색
    그럼 dfs에 list_up, val 을 인자로 넣어서 갱신하고 원하는 값이 되면 return 1, 만약 넘으면 return None
    지금 코드의 문제는 이미 완성된 조합이 있는데도 계속해서 같은 계산 결과를 중복해서 한다는 점
    같은 결과를 어떻게 덜 계산할까?
    
회고:
    잘 모르겠어서 AI 씀
    최악의 테스트 케이스 보니까 뭔 값이 기하급수적으로 상승
    원인은 파라미터에서 answer를 초기화 안 하고 그대로 받아서 생기는 문제였음.
    각 스택마다 answer를 초기화 안 하면 마지막 스택에서 값이 풀리면서 answer의 값이
    다음 for문으로 갈 때 따따블로 상승. 즉 하나의 루트에서의 answer값이 다음 루트에서도 더해져서
    어마어마한 수로 상승하게 됨
    처음에 값이 이상하게 나와서 dp로 풀까하다가
    그냥 풀어보고 도저히 안 되겠어서 그냥 AI를 썼는데,
    내가 몰랐던 부분은 재귀 과정의 첫 부분에서 첫 원소를 선택하거나 선택 안 하는 과정에 대한 이해도가 낮았음
    1,2,3,4,5인데 이걸 dfs로만 돌리면 무조건 어떤 부분 수열이던 1은 포함하고 있는 경우의 수가 나옴
    왜냐하면 dfs의 첫 부분에서 이미 list_int[0]을 더했기 때문임. 그래서 순수 dfs 함수로만 풀려면 애초에 순서를 다르게 잡아야 함
    dfs나 완전탐색에 대한 사고력이 아직 부족함
    그리고 테스트 케이스가 부족한 경우 내가 최악의 경우를 가정하고 테스트 케이스 짜야 함
"""

import sys
sys.stdin = open("./input.txt", "r")



def dfs(list_up: list, val: int, goal: int) -> int:
    """_summary_

    Args:
        list_up (list): 매번 갱신되는 list, 재귀로 들어가는 부분은 현재 스택의 원소를 제외한 리스트
        val (int): 해당 스탭에서 받는 이전 값의 합
        goal(int): 목표하는 수. K
        answer(int): 재귀로 나온 값들 받는 변수
        set_up: list형태의 현재까지의 조합을 정리한 set
    Returns:
        return 1: 만약 원하는 목표 수에 도달
        return 0: 만약 원하는 목표 수를 넘음
        return answer: 재귀로 나온 값들 받는 변수
    """
    answer = 0
    list_tmp = list_up[:]
    
    if list_tmp:
        val += list_tmp[0]
    
    else:
        return 0
    
    
    if val == goal:
        return 1
    
    elif val > goal:
        return 0
    
    for i in range(len(list_tmp)):
        list_nxt = list_tmp[i+1:]
        
        answer += dfs(list_nxt, val, goal)
    
    return answer

def main(list_int: list, k: int) -> int:
    """_summary_

    Args:
        list_int (list): 인자 list
        k (int): 목표값

    Returns:
        answer(int): 값
    """
    answer = 0
    for i in range(len(list_int)):
        answer += dfs(list_int[i:], 0, k)   # i번 원소를 첫 원소로 시작
        
    return answer
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    list_int = list(map(int, input().split()))
    print(f"#{test_case} {main(list_int, k)}")
