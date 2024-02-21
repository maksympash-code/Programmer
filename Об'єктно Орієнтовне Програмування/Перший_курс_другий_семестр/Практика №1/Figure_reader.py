from Triangle import *
class Figure_reader:
    def __init__(self, file_name):
        self.file_name = file_name


    def read_file(self):
        figures = []
        with open(self.file_name) as f:
            for line in f:
                #print(line)
                line.split()
                data = line.split()
                print(data)
                figure_type = data[0]
                try:
                    if figure_type == 'Triangele':
                        a,b,c = [float(el) for el in data[1:]]
                        triangle = Triangle(a,b,c)
                        figures.append(triangle)
                    elif figure_type == 'Rectangle':
                        pass
                    elif figure_type == 'Parallelogram':
                        pass
                    elif figure_type == 'Circle':
                        pass
                except AssertionError:
                    pass
        return figures