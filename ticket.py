class MovieBooking:
    def __init__(self, booking_id, movie_name, ticket_price, ticket_count):
        self.booking_id = booking_id
        self.movie_name = movie_name
        self.ticket_price = ticket_price
        self.ticket_count = ticket_count
    def total_bill(self):
        return self.ticket_price * self.ticket_count
    def booking_status(self):
        if self.ticket_count <= 0:
            return "Invalid Booking"
        return "Booking Confirmed"
def main():
    booking = MovieBooking(1, "Toxic", 250, 4)
    print("===== MOVIE BOOKING DETAILS =====")
    print(f"Booking ID   : {booking.booking_id}")
    print(f"Movie Name   : {booking.movie_name}")
    print(f"Ticket Price : {booking.ticket_price}")
    print(f"Ticket Count : {booking.ticket_count}")
    print(f"Total Bill   : {booking.total_bill()}")
    print(f"Status       : {booking.booking_status()}")
    print("================================")
if __name__ == "__main__":
    main()
