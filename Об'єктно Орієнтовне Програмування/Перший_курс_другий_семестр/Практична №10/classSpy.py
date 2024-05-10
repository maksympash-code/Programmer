from abc import ABCMeta, abstractmethod


class Spy(metaclass=ABCMeta):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def visitMilitaryBase(self, base):
        pass

    @abstractmethod
    def visit_general_staff(self, staff):
        pass