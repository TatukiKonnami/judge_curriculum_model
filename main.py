from curriculum_model import Curriculum

def createCurriculum(name: str) -> Curriculum:
    curriculum: Curriculum = Curriculum([], name)
    return curriculum

if __name__ == '__main__':
    curriculum = createCurriculum('C1')
    curriculum.addUnit('U1')
    curriculum.addUnit('U2')
    curriculum.addUnit('U3')
    curriculum.addContent('U1', 'C1')
    curriculum.addContent('U1', 'C2')
    curriculum.addContent('U2', 'C3')
    curriculum.addContent('U2', 'C4')
    curriculum.addContent('U3', 'C5')

    curriculum.addTransit('U1', 'U2')
    curriculum.addTransit('U1', 'U3')
    curriculum.addTransit('U2', 'U3')

    curriculum.print()

