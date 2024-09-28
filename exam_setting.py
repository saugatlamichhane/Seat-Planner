class ExamSetting:
    def __init__(self, org_name, org_address, exam_name, exam_year):
        self.org_name = org_name
        self.org_address = org_address
        self.exam_name = exam_name
        self.exam_year = exam_year
        self.room_list = []

def get_exam_setting():
    org_name = input("Enter the name of organization: ")
    org_address = input("Enter the address of organization: ")
    exam_name = input("Enter the title of examination: ")
    exam_year = input("Enter the examination year: ")
    exam_setting = ExamSetting(org_name, org_address, exam_name, exam_year)
    return exam_setting

if __name__ == "__main__":
    exam_setting = get_exam_setting()
    print(exam_setting.org_name, exam_setting.org_address)
    print(exam_setting.exam_name, exam_setting.exam_year)
