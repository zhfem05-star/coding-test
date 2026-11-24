"""
Args:
3
123 1
2737 1
32888 2
    test_case_cnt: testcase의 수
    list_int: 숫자열
    n: 바꿀 수 있는 횟수

Returns:
    answer: 횟수만큼 교환했을 때 최대 상금

제약사항:
    python 30초
    테스트 케이스 15개
    최대자릿수는 6개, 교환횟수는 10개
    6 * 10의 경우의 수


"""

from itertools import combinations

print(combinations(range(6), 2))