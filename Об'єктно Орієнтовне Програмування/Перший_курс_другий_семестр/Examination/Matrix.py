import numpy as np


class Matrix:
    def __init__(self, data):
        if not self.is_square(data):
            raise ValueError("Matrix must be square.")
        self.data = np.array(data)
        self.n = self.data.shape[0]

    @staticmethod
    def is_square(data):
        return all(len(row) == len(data) for row in data)

    @classmethod
    def from_keyboard(cls):
        n = int(input("Enter the size of the matrix (N): "))
        data = []
        for i in range(n):
            row = list(map(int, input(f"Enter row {i + 1} (space-separated numbers): ").split()))
            data.append(row)
        return cls(data)

    @classmethod
    def from_file(cls, filename):
        try:
            with open(filename, 'r') as file:
                data = [list(map(int, line.split())) for line in file]
            return cls(data)
        except FileNotFoundError:
            print(f"File {filename} not found. Please make sure the file exists.")
            return None

    def to_screen(self):
        for row in self.data:
            print(' '.join(map(str, row)))

    def to_file(self, filename):
        with open(filename, 'w') as file:
            for row in self.data:
                file.write(' '.join(map(str, row)) + '\n')


# Пример использования
if __name__ == "__main__":
    # Створення матриці з клавіатури
    matrix1 = Matrix.from_keyboard()
    matrix1.to_screen()
    matrix1.to_file("matrix1.txt")

    # Створення матриці з файлу
    matrix2 = Matrix.from_file("matrix2.txt")
    if matrix2:
        matrix2.to_screen()
