import sys
sys.stdin = open("./input.txt", "r")



T = int(input())
#args_ = input()
#list_ = list(map(int, args_.split()))
pre = 0
answer = 0
test_num: int

# main 함수. answer에 할당할 int 출력
def main(n: int, list_: list) -> int:
	"""
	Args:
		n(int) = 총 날짜 길이
		list_(list) = list_. 날짜 별 가격 리스트
	Returns:
		answer(int): 총 이익
	"""
	if list_[0] <= list_[1]:
		누적합 = list_[0]
		누적정보 = 1
	else:
		누적합 = 0
		누적정보 = 0
	answer = 0
	pre = list_[0]
    # 상승이면 True, 하강이면 False
	상승_하강_상태 = 0
#   for i in range(1, n):

	return answer
# args는 줄바꿈으로 구분하는구나
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	test_num = test_case
	n = int(input())
	args_ = input()
	list_ = list(map(int, args_.split()))
	answer = main(n, list_)
	print(f"#{test_num} {answer}")
	print(n, list_)