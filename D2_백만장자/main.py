import sys
sys.stdin = open("./input.txt", "r")



T = int(input())
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
	answer = 0
	max_ = 0
	reverse_list = list_[::-1]
	for i in range(n):
		# 작을 경우 answer += max_ - reverse_list[i]
		if max_ >= reverse_list[i]:
			answer += max_ - reverse_list[i]
		# 클 경우 max_ 갱신
		elif max_ < reverse_list[i]:
			max_ = reverse_list[i]
   
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
	#print(n, list_)


# list_ = [1,2,3,4,5]
# reverse_list = list_[::-1]

# print(type(reverse_list[0]))