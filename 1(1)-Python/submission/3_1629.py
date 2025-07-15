# lib.py의 Matrix 클래스를 참조하지 않음
import sys


"""
TODO:
- fast_power 구현하기 
"""


def fast_power(base: int, exp: int, mod: int) -> int:
    """
    빠른 거듭제곱 알고리즘 구현
    분할 정복을 이용, 시간복잡도 고민!
    """
    # 구현하세요!
    if exp == 1:
        return base % mod
    if exp == 0:
        return 1
    if exp % 2 == 1:
        return (fast_power(base, exp - 1, mod) * base) % mod
    else:
        tmp = fast_power(base, exp // 2, mod)
        return (tmp * tmp) % mod


def main() -> None:
    A: int
    B: int
    C: int
    A, B, C = map(int, input().split()) # 입력 고정
    
    result: int = fast_power(A, B, C) # 출력 형식
    print(result) 

if __name__ == "__main__":
    main()
