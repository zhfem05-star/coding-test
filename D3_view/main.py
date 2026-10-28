import sys
sys.stdin = open("./input.txt", "r")
#import tracemalloc

"""
대충 2 ~ n -2 까지 범위로 for문 하고
list_[i] 기준 -2 ~ +2 까지 애들 슬라이딩 윈도우로 움직이면 될 것 같은데
[0, 0, 1, 2, 3] 이면 i 기준 좌우 2만 확인하면 끝인데, 만약 시간 문제가 있다면 슬라이딩 윈도우로 움직이면 될 듯?
움직이기 -> max 체크(건물 높이가 죄다 같으면?) -> max로 가장 큰 건물(a), a 제외 가장 큰 건물(b)로 하여 a - b 를 answer ++ 
공간 메모리 문제가 터진 것 같음. 스택 메모리가 1mb 의 제약을 갖고 있음. 슬라이딩 윈도우로 구현해야 함
입력 형식을 지키자. 이번에는 테스트 케이스 개수가 없는데 까먹고 안 넣음.
그리고 테스트 케이스도 로컬 말고 웹에서 한 번 더 돌려보자
"""


# main 함수. answer에 할당할 int 출력
def main(a: int, b: list) -> int:
    answer = 0
    for i in range(2, a - 2):
        if i == 2:
            list_tmp = b[i-2:i+3]
        else:
            list_tmp.pop(0)
            list_tmp.append(b[i + 2])
        #print(list_tmp)
        # 만약 가운데 건물이 가장 크면 answer에 ++ 해서 조광권 층수 구하기
        if b[i] == max(list_tmp):
            x = list_tmp[2]
            y = sorted(list_tmp)[-2]
            answer += x - y
            #print(answer)
            

        else:
            continue

    return answer #noqa

# 1. 메모리 추적 시작
#tracemalloc.start()

for test_case in range(1, 11):
    #print(f"{test_case}번째 루프")
    a = int(input())
    b = input()
    b = list(map(int, b.split()))
    answer = main(a, b)
    print(f"#{test_case} {answer}")
#current, peak = tracemalloc.get_traced_memory()
# 3. 추적 종료
#tracemalloc.stop()
#print(f"current = {current}, peak = {peak}")