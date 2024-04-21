
class ProtectedDictInt_iterator:
    def __init__(self,collection):
        # self.collection = collection
        self.keys = list(collection.keys())
        self.keys.sort()
        self.index = 0 # поточна позиція у колекції

    def __next__(self):
        try:
            current = self.keys[self.index]
            self.index += 1
            return current
        except IndexError:
            raise StopIteration


