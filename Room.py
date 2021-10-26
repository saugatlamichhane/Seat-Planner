# The object "room" must have attributes roomSN, emptySeats roomSeatFinal.
class Room:
    def __init__(self, roomsn):
        self.roomSN = roomsn
        self.emptySeats = []
        self.roomSeatFinal = {}