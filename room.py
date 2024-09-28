import string_format

class Room:
    def __init__(self, room_sn, rows, cols):
        self.room_sn = room_sn
        self.rows = rows
        self.cols = cols
        self.empty_seats = []
        self.room_seat_final = {}
        self.create_seats()

    def create_seats(self):
        for row in range(1, self.rows+1):
            for col in range(1, self.cols+1):
                seat_sn = get_seat_name(row, col)
                self.empty_seats.append(seat_sn)
        
def get_seat_name(row, col):
    row_sn = string_format.get_two_digit_string(row)
    col_sn = string_format.get_two_digit_string(col)
    return row_sn + col_sn
    
