"""
Args:
    test_case_n(str): 테스트 케이스 개수
    n(str): 배열의 세로 크기
    m(str): 배열의 가로 크기
    list_(list(str)): 2차원 리스트(바코드)

Returns:
    answer(int): 잘못된 암호면 0, 아니면 해당 배열을 모두 합한 값
    print(str): f"#{test_case} {answer}"

제약사항:
    python만 30초
    1<= n <= 50, 56 <= m <= 100
    정확한 테스트 케이스 숫자는 주어지지 않았지만 우선 검증 단계에선 10개
    만약 50 * 56의 배열을 10개 탐색하면 ?
    각 숫자는 이미지에 인코딩 규칙이 명시되어 있음

가정:
    비밀코드의 범위를 체크하는 check 기능
     -> 이게 막히는 이유. 예제를 보면 0에서 부터 배열이 시작. 즉 56개의 원소가
     1을 기준으로 양 끝을 재단할 수 없으면, 만약 56개가 아닐 때
     어디를 추가해야 하는가? 이에 대한 조건이나 가정은 없음
     이제 보니 각 숫자별로 패턴이 있음. 그리고 공통 패턴으로 0으로 시작해서 1로 끝남
     즉 마지막 1을 찾고 그 끝에서 56칸을 뒤로 스캔하는 방식이 필요함
     dict로 각 패턴별로 만들면 될 듯
    올바른 값인지 검증하는 check 기능(10의 배수 체크)

의사코드:
    dict_7bit = {
        "0001101" : 0,
        "0011001" : 1,
        "0010011" : 2,
        "0111101" : 3,
        "0100011" : 4,
        "0110001" : 5,
        "0101111" : 6,
        "0111011" : 7,
        "0110111" : 8,
        "0001011" : 9
    }
    list_str = []
    stack_ = ""
    for i in list_:
        if "1" in i:
            i_idx = i.rfind("1")
            a = i[i_idx - 55:i_idx + 1]
            for j in a:
                stack_ += j
                if len(stack_) == 7:
                    list_str.append(dict_7bit["".join(stack_)])
    
    # check 로직
    list_int = int(list_str)
    list_int_jjack = 0
    list_int_hol = 0
    for x in range(0, len(list_int), 2):
        list_int_hol += list_int[x]

    for y in range(1, len(list_int), 2):
        list_int_jjack += list_int[y]

    if (list_int_jjack * 3 + list_int_hol)%10 == 0:
        return sum(list_int)
    
    else:
        return 0
"""
import sys
sys.stdin = open("./input.txt", "r")


def main(list_origin: list, m: int) -> int:
    dict_7bit = {
        "0001101" : 0,
        "0011001" : 1,
        "0010011" : 2,
        "0111101" : 3,
        "0100011" : 4,
        "0110001" : 5,
        "0101111" : 6,
        "0111011" : 7,
        "0110111" : 8,
        "0001011" : 9
    }
    
    # check 로직
    print(f"list_str: {list_str}")
    list_int = list(map(int, list_str))
    print(list_int)
    list_int_jjack = 0
    list_int_hol = 0

    for x in range(0, 8, 2):
        list_int_hol += list_int[x]

    for y in range(1, 8, 2):
        list_int_jjack += list_int[y]

    if (list_int_jjack * 3 + list_int_hol) % 10 == 0:
        return sum(list_int)
    
    else:
        return 0
    

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a, b = input().split()
    a = int(a) # 세로 길이
    b = int(b) # 가로 길이
    list_ = [list(input()) for i in range(a)]
    print(f"{test_case} {a} {b} {main(list_, b)}")
