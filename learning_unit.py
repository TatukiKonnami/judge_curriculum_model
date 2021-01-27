from learning_content import LearningContent
from typing import List

class LearningUnit():
    def __init__(self, contents:List[LearningContent], name: str, transitions ):
        self.contents = contents
        self.name = name
        self.transitions = transitions

    def addContents(self, content: LearningContent):
        self.contents.append(content)

    def addTransition(self, unit):
        self.transitions.append(unit)

    def print(self):
        print('\t{}'.format(self.name))
        for content in self.contents:
            content.print()
        print('\t-----> ' + str([i.name for i in self.transitions ]))
