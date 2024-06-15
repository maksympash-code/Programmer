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

    def __add__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            return NotImplemented
        return Matrix(np.dot(self.data, other.data))

    def __getitem__(self, index):
        i, j = index
        return self.data[i, j]

    def __setitem__(self, index, value):
        i, j = index
        self.data[i, j] = value

    def __iter__(self):
        self._iter_idx = 0
        return self

    def __next__(self):
        if self._iter_idx >= self.n * self.n:
            raise StopIteration
        result = self.data[self._iter_idx // self.n, self._iter_idx % self.n]
        self._iter_idx += 1
        return result

    def sum_elements(self):
        return sum(self)

# Пример использования
if __name__ == "__main__":
    # Створення матриці з файлу
    matrix1 = Matrix.from_file("matrix1.txt")
    print("matrix1 = ")
    matrix1.to_screen()
    matrix2 = Matrix.from_file("matrix2.txt")
    print("matrix2 = ")
    matrix2.to_screen()

    # Додавання матриць
    result_add = matrix1 + matrix2
    print("result_add = ")
    result_add.to_screen()
    result_add.to_file("result_add.txt")

    # Множення матриць
    result_mul = matrix1 * matrix2
    print("result_mul = ")
    result_mul.to_screen()
    result_mul.to_file("result_mul.txt")

    # Звернення до елемента матриці
    print("Елемент [1,1] в matrix1:", matrix1[1, 1])
    matrix1[1, 1] = 10
    print("matrix1 після зміни елемента [1,1]:")
    matrix1.to_screen()

    # Використання ітератора та обчислення суми елементів
    total_sum = matrix2.sum_elements()
    print("Сума елементів matrix1:", total_sum)
