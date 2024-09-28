import group
import exam_setting
import room
import string_format
import random

# Alternative approach: assign seats randomly to all of them and then assign them group


# Updates available seats
def update_available_seats(current_group, current_room, alloted_seat):
    # Prepare a list of seats to remove
    seats_to_remove = []
    # Add the surrounding seats to seats_to_remove list
    current_row = int(alloted_seat[:2])
    current_col = int(alloted_seat[2:])
    for row in range(current_row-1, current_row+2):
        if row > 0 and row <= current_room.rows:
            for col in range(current_col-1, current_col+2):
                if col > 0 and col <= current_room.cols:
                    row_str = string_format.get_two_digit_string(row)
                    col_str = string_format.get_two_digit_string(col)
                    seat_str = row_str+col_str
                    seats_to_remove.append(seat_str)
    # Remove each them if the availble_seats_list contains it
    for seat in seats_to_remove:
        if seat in current_group.current_room_available_seats:
            current_group.current_room_available_seats.remove(seat)

# Allots seat for each student of the group
def allot_seat(current_exam_setting, group_list, group_sn):
    current_group = group_list[group_sn-1]
    # Set current_room to the first room
    current_room = current_exam_setting.room_list[0]
    current_room_counter = 1
    current_group.current_room_available_seats = list(current_room.empty_seats)
   
    for examinee in current_group.examinees:
        # If current_room doesn't have any available seats for the examinees in current group, move onto the next room.
        while len(current_group.current_room_available_seats) == 0:
            current_room_counter += 1
            # If room_list doesn't have another room, add new_room and move onto the new room.
            if len(current_exam_setting.room_list) < current_room_counter:
                current_exam_setting.add_room()
            current_room = current_exam_setting.room_list[current_room_counter - 1]
            current_group.current_room_available_seats = list(current_room.empty_seats)
        # Place the student in a random available seat
        # Remove that seat from empty_seats and update current_room_available_seats
        current_seat = random.choice(current_group.current_room_available_seats)
        examinee += current_group.group_name
        current_room.room_seat_final.update({current_seat: examinee})
        current_room.empty_seats.remove(current_seat)
        update_available_seats(current_group, current_room, current_seat)

def main():

    # Create exam setting
    current_exam_setting = exam_setting.get_exam_setting()

    # Starting from first group, allot seats for each examinee in each group
    group_list = group.create_groups()
    group_list = group.assign_groups(group_list)
    group_sn_counter = 1

    while group_sn_counter <= len(group_list):
        allot_seat(current_exam_setting, group_list, group_sn_counter)
        group_sn_counter += 1

    # Print exam setting
    print(current_exam_setting.org_name, current_exam_setting.org_address)
    print(current_exam_setting.exam_name, current_exam_setting.exam_year)
    print()

    # Print Seat Plan
    for current_room in current_exam_setting.room_list:
        print(f"Room {current_room.room_sn}")
        for row in range(1, current_room.rows+1):
            for col in range(1, current_room.cols+1):
                row_str = string_format.get_two_digit_string(row)
                col_str = string_format.get_two_digit_string(col)
                seat_str = row_str + col_str
                print(current_room.room_seat_final.get(seat_str, "|EMPTY|").rjust(7), end = " ")
            print()

        print()

main()
# TODO Create PDF file.
