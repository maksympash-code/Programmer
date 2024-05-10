from FileReader import FileReaderLineObserver, FileReader


class ShowLines(FileReaderLineObserver):
    def onReceive(self, line):
        print(line)
    def onReadFinish(self):
        print("file read finished!!!")

class LenWordsInLine(FileReaderLineObserver):
    def __init__(self):
        self.counter = 0

    def onReceive(self, line: str):
        line = line.split()
        self.counter += len(line)

    def onReadFinish(self):
        print(f"Кількість слів у {self.counter}")

class TargetWord(FileReaderLineObserver):
    def __init__(self,word):
        self.word = word
        self.yes = 0
        self.no = 0

    def onReceive(self, line: str):
        if self.word in line:
            self.yes += 1
        else:
            self.no += 1
    def onReadFinish(self):
        if self.yes != 0:
            print(f"Слово {self.word} є у текстовому файлі")
        else:
            print(f"Слова {self.word} немає у текстовому файлі")

class DifferentWords(FileReaderLineObserver):
    def __init__(self):
        self.similar_words = 0
        self.different_words = 0
        self.words = {}

    def onReceive(self, line: str):
        line = line.split()
        for line in line:
            if self.words is not line:
                self.words += line
        print(self.words)

    def onReadFinish(self):
        pass

if __name__ == '__main__':
    file_reader = FileReader("test")
    # showLines = ShowLines()
    # file_reader.subscribe(showLines)
    # lenWordsInLine = LenWordsInLine()
    # file_reader.subscribe(lenWordsInLine)
    TargetWord = TargetWord("Привіт")
    file_reader.subscribe(TargetWord)
    DifferentWords = DifferentWords()
    file_reader.subscribe(DifferentWords)

    file_reader.read()