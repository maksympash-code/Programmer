from Military_object import GeneralStaff, MilitaryBase
from classSpy import Spy

class Secret_agent(Spy):
    def __init__(self, name):
        super(Secret_agent, self).__init__(name)

    def visit_general_staff(self, staff):
        print(f"Secret_agent {self.name} copyed documentation in the amount of {staff.secretPaper} and generals: {staff.generals}")

    def visitMilitaryBase(self, base):
        print(f"Secret_agent {self.name} collected information on the number of tanks: {base.tanks}, officers: {base.officers}, soldiers: {base.soldiers} and jeeps:{base.jeeps}")

class Saboteur(Spy):
    def __init__(self, name):
        super().__init__(name)

    def visit_general_staff(self, staff):
        print("Подумки говорить: Всіх уб'ю!!!")
        staff.generals = 0
        staff.secretPaper = 0

    def visitMilitaryBase(self, base):
        base.jeeps -= 2
        base.tanks -= 1
        base.officers -= 3
        base.soldiers -= 10


class JamesBond(Spy):
    def __init__(self, name):
        super().__init__(name)

    def visit_general_staff(self, staff : GeneralStaff):
        print(self.name, staff.name)

    def visitMilitaryBase(self, base: MilitaryBase):
        print(self.name, base.name)



if __name__ == '__main__':
    generalStaff = GeneralStaff(20, 100, "Kremlin")
    print(generalStaff)

    militaryBase = MilitaryBase(10, 1000, 300, 20, "BNR")
    print(militaryBase)

    james = JamesBond("James Bond")
    generalStaff.accept(james)
    militaryBase.accept(james)

    vasilii = Secret_agent("Vasilii")
    vasilii.visit_general_staff(generalStaff)
    vasilii.visitMilitaryBase(militaryBase)