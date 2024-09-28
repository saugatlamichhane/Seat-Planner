import group

def get_number_of_groups():
    num_groups = int(input("How many Question Sets are there? "))
    return num_groups

def create_groups(num_groups):
    group_list = []
    for i in range(num_groups):
        group_list.append(group.group(chr(65+i)))
    return group_list

if __name__ == "__main__":
    num_groups = get_number_of_groups()
    group_list = create_groups(num_groups)
    print("Assigned groups successfully")
    for g in group_list:
        print(g.group_name)
