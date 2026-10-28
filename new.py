import sys
from pathlib import Path

ROOT = Path(__file__).parent

MAIN_TEMPLATE = '''import sys
input = sys.stdin.readline


def main():
    pass

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    pass
    
'''


def create(name: str):
    folder = ROOT / name
    if folder.exists():
        print(f"이미 존재합니다: {folder}")
        return

    folder.mkdir()
    (folder / "input.txt").write_text("", encoding="utf-8")
    (folder / "문제설명.txt").write_text("", encoding="utf-8")
    (folder / "main.py").write_text(MAIN_TEMPLATE, encoding="utf-8")
    print(f"생성 완료: {folder}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("사용법: python new.py D3_view")
        sys.exit(1)
    create(sys.argv[1])

# print(ROOT)