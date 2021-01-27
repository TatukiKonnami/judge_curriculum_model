from learning_unit import LearningUnit
from learning_content import LearningContent
from typing import List

class Curriculum():
    def __init__(self, units: List[LearningUnit], name: str):
        self.units = units
        self.name = name

    def addUnit(self, name: str):
        self.units.append(LearningUnit([], name, []))

    def searchUnit(self, unit_name: str) -> LearningUnit:
        return [i for i in self.units if i.name == unit_name][0]

    def addContent(self, unit_name: str, name: str):
        unit:LearningUnit = self.searchUnit(unit_name)
        unit.addContents(LearningContent(name))

    def addTransit(self, origin_name: str, dest_name: str):
        origin: LearningUnit = self.searchUnit(origin_name)
        dest: LearningUnit = self.searchUnit(dest_name)
        origin.addTransition(dest)

    def print(self):
        print(self.name)
        for unit in self.units:
            unit.print()
