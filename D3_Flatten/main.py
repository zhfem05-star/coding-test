"""
평탄화 작업

제약 조건:
    python만 30초 -> 생각보다 시간이 빠듯한 알고리즘일 수 있음
    가로 길이 = 100
    모든 상자의 높이는 1 <= x <= 100

규칙:
    높은 곳에 있는 애를 낮은 곳으로 내림. 이 과정에서 같은 높이의 덤프가 있으면
    -> 아무거나 상관없음

    가장 낮은 높이에 있는 곳으로 높은 곳에 있는 상자를 옮겨야 함

    이런 작업을 loop 돌려서 모든 상자들의 높이(원소) 간의 차이가 1 이내여야 함
    만약 횟수 안에 다 못한다? -> 그냥 종료하고 최소 높이와 최대 높이 차 구하기
가정:
    상자의 높이(원소) = 1에서 100까지이고
    덤프횟수는 = 1000
    모든 상자를 스캔, max하고 min 찾은 다음 이것의 최솟값과 최댓값의 격차를 줄일 로직
    (가로길이)100 * (덤프횟수)1000 
    루프는 덤프횟수(n)가 없을 때 까지 -> 1000번의 연산
    테스트케이스 10개
    가로길이(x)를 매번 탐색 -> 100(min하고 max까지 구해야 하니 루프 별 2번 연산해서 100 * 2 * 1000 * 10 = 2000000)
    우선 10만 번의 연산까지는 괜찮음 최솟값 인덱스에서 최저값 인덱스로 값을 1만큼 옮기는 작업
    그리고 루프 마지막에 max와 min의 diff 구하기
"""
import sys
sys.stdin = open("./input.txt", "r")


def main(a: int, b: list) -> int:
    """
    Args:
        a(int): 덤프횟수
        b(list(int)): 상자 높이 리스트

    Returns:
        answer(int): 최종 b의 최대 높이 - 최소 높이

    """
    dump_ = a
    if max(b) - min(b) <= 1:
        return max(b) - min(b)
    
    while dump_ != 0:
        max_idx = b.index(max(b))
        min_idx = b.index(min(b))

        b[max_idx] -= 1
        b[min_idx] += 1
        # print(b)
        dump_ -= 1
        
    return max(b) - min(b)

test_case = 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
while True:
    try:
        line = input()
    except EOFError:
        break

    a = int(line)
    b = input()
    b = list(map(int, b.split()))

    answer = main(a, b)
    print(f"#{test_case} {answer}")

    test_case +=1