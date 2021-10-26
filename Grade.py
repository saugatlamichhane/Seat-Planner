# The object "grade" must have attributes gradeSN, sectionsList, noOfStds and nonAllotedStds.
class Grade:
    def __init__(self, gradesn, noofstds):
        self.gradeSN = gradesn
        self.noOfStds = noofstds
        self.sectionsList = []
        self.nonAllotedStds = []