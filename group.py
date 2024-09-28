import random

class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.examinees = []
        self.current_room_available_seats = []

def get_number_of_groups():
    # TODO Input Validation
    num_groups = int(input("How many Question Sets are there? "))
    return num_groups

def get_group_name(group_sn):
    return chr(65+group_sn)

def create_groups():
    num_groups = get_number_of_groups()
    group_list = []
    for i in range(num_groups):
        group_list.append(Group(get_group_name(i)))
    return group_list

def get_number_of_examinees():
    # TODO Input Validation
    num_examinees = int(input("How many examinees are there? "))
    return num_examinees

def get_symbol_start():
    # TODO Input Validation
    symbol_start = int(input("First Symbol No. "))
    return symbol_start

def get_symbol_end(start_symbol, num_examinees):
    # TODO Make Symbol Number of Equal Length
    return start_symbol + num_examinees

def assign_groups(group_list):
    start_symbol = get_symbol_start()
    num_examinees = get_number_of_examinees()
    end_symbol = get_symbol_end(start_symbol, num_examinees)
    for sn in range(start_symbol, end_symbol+1):
        curr_group = random.randint(0, len(group_list)-1)
        group_list[curr_group].examinees.append(sn)
    return group_list


if __name__ == "__main__":
    group_list = create_groups()
    """print("Created groups successfully")
    for g in group_list:
        print(g.group_name)
    """
    group_list = assign_groups(group_list)
    for g in group_list:
        print(g.group_name)
        for e in g.examinees:
            print(e, end = " ")
        print()

