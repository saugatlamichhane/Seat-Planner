# The object "school" must have attributes schoolName, schoolAddress, leastGrade, highestGrade and roomList.
class School:
    def __init__(self, name, address, leatgrade, highestgrade):
        self.schoolName = name
        self.schoolAddress = address
        self.leastGrade = leatgrade
        self.highestGrade = highestgrade
        self.roomList = []