class Motel:
    def __init__(self, capacity):
        self.capacity = capacity
        self.reservations = []

    def make_reservation(self, guest_name, room_number):
        if len(self.reservations) < self.capacity:
            reservation = {"guest_name": guest_name, "room_number": room_number}
            self.reservations.append(reservation)
            return True
        else:
            return False

    def cancel_reservation(self, guest_name):
        for reservation in self.reservations:
            if reservation["guest_name"] == guest_name:
                self.reservations.remove(reservation)
                return True
        return False

    def update_reservation(self, old_guest_name, new_guest_name):
        for reservation in self.reservations:
            if reservation["guest_name"] == old_guest_name:
                reservation["guest_name"] = new_guest_name
                return True
        return False

    def get_reservation(self, room_number):
        for reservation in self.reservations:
            if reservation["room_number"] == room_number:
                return reservation
        return None

    def check_room_availability(self, room_number):
        for reservation in self.reservations:
            if reservation["room_number"] == room_number:
                return False
        return True

    def check_guest_reservation(self, guest_name):
        for reservation in self.reservations:
            if reservation["guest_name"] == guest_name:
                return True
        return False

    def list_reservations(self):
        return self.reservations

    def clear_reservations(self):
        self.reservations = []
