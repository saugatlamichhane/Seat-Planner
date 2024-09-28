import room

class ExamSetting:
    def __init__(self, org_name, org_address, exam_name, exam_year):
        self.org_name = org_name
        self.org_address = org_address
        self.exam_name = exam_name
        self.exam_year = exam_year
        self.room_list = []
        self.add_room()

    def add_room(self):
        room_sn = len(self.room_list)+1
        rows = int(input(f"How many rows in Room {room_sn}? "))
        cols = int(input(f"How many cols in Room {room_sn}? "))
        self.room_list.append(room.Room(room_sn, rows, cols))

def get_exam_setting():
    org_name = input("Enter the name of organization: ")
    org_address = input("Enter the address of organization: ")
    exam_name = input("Enter the title of examination: ")
    exam_year = input("Enter the examination year: ")
    current_exam_setting = ExamSetting(org_name, org_address, exam_name, exam_year)
    return current_exam_setting

if __name__ == "__main__":
    current_exam_setting = get_exam_setting()
    print(current_exam_setting.org_name, current_exam_setting.org_address)
    print(current_exam_setting.exam_name, current_exam_setting.exam_year)
