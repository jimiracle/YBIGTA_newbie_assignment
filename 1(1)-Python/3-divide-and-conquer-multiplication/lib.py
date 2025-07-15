from __future__ import annotations
import copy


"""
TODO:
- __setitem__ 구현하기
- __pow__ 구현하기 (__matmul__을 활용해봅시다)
- __repr__ 구현하기
"""


class Matrix:
    MOD = 1000

    def __init__(self, matrix: list[list[int]]) -> None:
        self.matrix = matrix

    @staticmethod
    def full(n: int, shape: tuple[int, int]) -> Matrix:
        return Matrix([[n] * shape[1] for _ in range(shape[0])])

    @staticmethod
    def zeros(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(0, shape)

    @staticmethod
    def ones(shape: tuple[int, int]) -> Matrix:
        return Matrix.full(1, shape)

    @staticmethod
    def eye(n: int) -> Matrix:
        matrix = Matrix.zeros((n, n))
        for i in range(n):
            matrix[i, i] = 1
        return matrix

    @property
    def shape(self) -> tuple[int, int]:
        return (len(self.matrix), len(self.matrix[0]))

    def clone(self) -> Matrix:
        return Matrix(copy.deepcopy(self.matrix))

    def __getitem__(self, key: tuple[int, int]) -> int:
        return self.matrix[key[0]][key[1]]

    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        """
        value 값을 matrix의 key[0], key[1]에 설정하함
        """
        self.matrix[key[0]][key[1]] = value % self.MOD


    def __matmul__(self, matrix: Matrix) -> Matrix:
        x, m = self.shape
        m1, y = matrix.shape
        assert m == m1

        result = self.zeros((x, y))

        for i in range(x):
            for j in range(y):
                for k in range(m):
                    result[i, j] += self[i, k] * matrix[k, j]

        return result

    def __pow__(self, n: int) -> Matrix:
        """
        result : 결과 저장되는 곳
        base : divide and conquer 방식 사용해서 반씩 진행, 마지막 case 되면 result @ base
        """

        result = Matrix.eye(self.shape[0])
        base = self.clone()

        while n > 0:
            if n % 2 == 1:
                result = result @ base
            base = base @ base
            n //= 2

        return result



    def __repr__(self) -> str:
        """
        matrix 형태대로 출력
        """
        string = ""
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if j == len(self.matrix[i]) - 1:
                    string += (str(self.matrix[i][j]))
                else:
                    string += (str(self.matrix[i][j]))
                    string += " "
            string += "\n"
        return string