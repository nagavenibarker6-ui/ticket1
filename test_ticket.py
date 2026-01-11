from ticket import MovieBooking

def test_total_bill():
    booking = MovieBooking(1, "Toxic", 250, 4)
    assert booking.total_bill() == 1000

def test_booking_status_valid():
    booking = MovieBooking(2, "Avatar", 300, 3)
    assert booking.booking_status() == "Booking Confirmed"

def test_booking_status_invalid():
    booking = MovieBooking(3, "Inception", 200, 0)
    assert booking.booking_status() == "Invalid Booking"
