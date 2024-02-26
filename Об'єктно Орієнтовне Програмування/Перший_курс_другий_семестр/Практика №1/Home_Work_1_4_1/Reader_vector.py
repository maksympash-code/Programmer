from Vectors import Vectors


class Vectors_reader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name) as f:
            all_vect = []
            for line in f:
                lines = line.strip().split()
                args = list(map(int, lines[0:]))
                vector = Vectors(*args)
                vect = [vector.dimension(), vector.length(), vector.middle(), vector.max(), vector.min()]

                all_vect.append(vect)
        return all_vect

    def worker(self):
        all_vect = self.read()
        res_1 = all_vect[0]
        res_2 = all_vect[0]
        mid = 0
        for i in all_vect:
            if i[0] > res_1[0]:
                res_1 = i
            elif i[0] == res_1[0]:
                if i[1] > res_1[1]:
                    res_1 = i
            if i[1] > res_2[1]:
                res_2 = i
            elif i[1] == res_2[1]:
                if i[0] < res_2[0]:
                    res_2 = i
            mid += i[1]
        print(f"The biggest dimension: {res_1}")
        print(f"The biggest length: {res_2}")
        print(f"The middle: {mid / len(all_vect)}")


if __name__ == '__main__':
    reader = Vectors_reader('input01.txt')
    print(*reader.read())
    reader.worker()