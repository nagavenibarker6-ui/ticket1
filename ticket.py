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
