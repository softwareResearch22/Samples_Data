from abc import ABC, abstractmethod



class RawMaterials:

    def get_materials(self):
        return "Materials arrived."


class Mixing:

    def mix_materials(self):
        return "Mixing done."


class Calenders:

    def cut_cords(self):
        return "Cord materials are cut."


class Building:

    def assembly_tires(self):
        return "Green tire is obtained."


class Curing:

    def cure_tires(self):
        return "Tires are cured."


class FinalFinish:

    def test_tires(self):
        return "Tires are tested."


class Logistics:

    def send_tires(self):
        return "Tires are sold. You can buy a new Maserati"


class FacadeTire:

    def __init__(self):
        self.raw = RawMaterials()
        self.mixer = Mixing()
        self.calender = Calenders()
        self.builder = Building()
        self.cure = Curing()
        self.tester = FinalFinish()
        self.trucks = Logistics()

    def sell_tires(self):
        result = self.raw.get_materials()
        result += " " + self.mixer.mix_materials()
        result += " " + self.calender.cut_cords()
        result += " " + self.builder.assembly_tires()
        result += " " + self.cure.cure_tires()
        result += " " + self.tester.test_tires()
        result += " " + self.trucks.send_tires()
        return result


if __name__ == '__main__':
        FACADE = FacadeTire()
        result = FACADE.sell_tires()
        # OUT:
        'Materials arrived. Mixing done. Cord materials are cut. Green tire is obtained. Tires are cured. Tires are tested. Tires are sold. You can buy a new Maserati'
