"""
Args:
113
(9+(5*2+1)+(3*3*7*6*9*1*7+1+8*6+6*1*1*5*2)*4*7+4*3*8*2*6+(7*8*4*5)+3+7+(2+6+5+1+7+6+7*3*(6+2)+6+6)*2+4+2*2+4*9*3)
85
(4+8+4*(8*5*(7*(6*8)+3+(6+(3+7+1*7*5*4)*3)*2*3+5)+6+7*7)*4+2+9*4+7+2*3*(7*6*1*8)+9+9)
...
    test_case_len: 테스트케이스의 길이
    test_case_list: 테스크 케이스 리스트

Returns:
    answer: 답 계산하기

제약사항:
    python 30초
    테스트 케이스 10개
    피연산자의 숫자는 0~9만 주어짐(두자리 숫자 구분x)

규칙:
    중위 표현식을 문자열로 줄테니
    이걸 계산하는 후위 표현식 만들기 문제

가정:
    수식을 담아두는 리스트와 숫자를 담아두는 리스트로 나눠야 함
    “3+(3+4+5)*6+7”
    334567
    +(++)*+
    7 + 6 * 5(+ 4 + 3 ) 3 +
    숫자 리스트를 먼저 그냥 pop하고, 수식의 경우에는 pop하다가 (가 나오면 따로 while문 돌게 하기
    근데 이러면 괄호문 안에 있는 괄호는 어쩌지?
    괄호 여부 큐를 따로 두고, (나오면 append하고 )나오면 pop해서 체크?

회고:
    AI로 품
    요새 문제 풀이 능력이 많이 떨어짐. 근데 대부분 이유를 보면 단순한게,
    무엇을 구현해야 할지 모른다는 점이 큰 듯
    이전 문제들은 문제를 이해하고, 어떤 흐름으로 구현해야 하는지
    무엇이 필요한지를 직관적으로 정의했는데,
    지금은 문제 이해도 어렵고, 어떻게 해야 풀 수 있는지 감도 안오는 경우가 대부분
    가장 중요한 역량은 문제를 이해하는 것
    제약 사항을 보고 어느 방식으로 해야하는지 방향성을 잡고
    문제 자체를 내가 스스로 어떻게 해결하는지 직접 구조화하고
    구현에 들어갈 것
    구현 자체는 내가 못하진 않음. 하지만 문제 접근 및 풀이 방법에서 많이 해매는 듯

"""


import sys
sys.stdin = open("./input.txt", "r")


def main(list_str: str) -> int:
    dict_cal = {
        '(': 0,
        '+': 1,
        '*': 2
    }
    stack = [] # 연산자 전용
    out = [] # 출력 리스트
    stack_cal = [] # 계산용 리스트

    for i in list_str:
        if i.isdigit():
            out.append(i)

        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                out.append(stack.pop())
            stack.pop()

        else:
            while stack and dict_cal[stack[-1]] >= dict_cal[i]:
                out.append(stack.pop())
            stack.append(i)

    while stack: # stack 털기. 남은 연산기호 털어야 함
        out.append(stack.pop())

    for j in out:
        if j in '+*':
            b = stack_cal.pop()
            a = stack_cal.pop()
            if j == '+':
                stack_cal.append(a + b)
            elif j == '*':
                stack_cal.append(a * b)

        else:
            stack_cal.append(int(j))

    return stack_cal[0]


test_case = 1

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
while True:
    try:
        line = input()

    except EOFError:
        break

    n = int(line)
    list_str = input()

    print(f"#{test_case} {main(list_str)}")
    test_case += 1
