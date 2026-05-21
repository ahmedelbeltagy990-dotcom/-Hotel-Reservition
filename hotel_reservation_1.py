 # ===========================================================
#   Hotel Reservation System
#   Written in Python for Beginners
# ============================================================

from datetime import datetime

# ─────────────────────────────────────────
# Main Data - Available Rooms Dictionary
# ─────────────────────────────────────────
rooms = {
    "101": {"type": "Single Room", "price": 300,  "available": True},
    "102": {"type": "Double Room", "price": 500,  "available": True},
    "103": {"type": "Luxury Suite", "price": 1200, "available": True},
    "104": {"type": "Single Room", "price": 300,  "available": False},  # Reserved
    "105": {"type": "Double Room", "price": 500,  "available": True},
}

# Empty list to store bookings
bookings = []

# Booking ID counter
booking_counter = 1000


# ─────────────────────────────────────────
# Functions
# ─────────────────────────────────────────

def show_available_rooms():
    """Display available rooms"""
    
    print("\n" + "="*50)
    print("        Available Rooms")
    print("="*50)

    found = False

    for room_num, info in rooms.items():

        status = "Available" if info["available"] else "Reserved"

        if info["available"]:
            print(f"Room {room_num} | {info['type']} | "
                  f"{info['price']} EGP per night | {status}")
            found = True

    if not found:
        print("No rooms available right now.")

    print("="*50)


def calculate_nights(checkin_str, checkout_str):
    """Calculate number of nights"""

    fmt = "%Y-%m-%d"

    checkin  = datetime.strptime(checkin_str, fmt)
    checkout = datetime.strptime(checkout_str, fmt)

    delta = checkout - checkin

    return delta.days


def make_booking(guest_name, room_num, checkin, checkout, guests):
    """Create a new booking"""

    global booking_counter

    # Check if room exists
    if room_num not in rooms:
        print(f"\nError: Room {room_num} does not exist.")
        return None

    # Check room availability
    if not rooms[room_num]["available"]:
        print(f"\nError: Room {room_num} is already reserved.")
        return None

    # Calculate nights and total cost
    nights = calculate_nights(checkin, checkout)

    if nights <= 0:
        print("\nError: Checkout date must be after checkin date.")
        return None

    price_per_night = rooms[room_num]["price"]
    total_price = nights * price_per_night

    # Create booking
    booking_counter += 1

    booking = {
        "id": f"BK{booking_counter}",
        "guest": guest_name,
        "room": room_num,
        "type": rooms[room_num]["type"],
        "checkin": checkin,
        "checkout": checkout,
        "nights": nights,
        "guests": guests,
        "price_per_night": price_per_night,
        "total": total_price,
        "status": "Confirmed"
    }

    # Save booking
    bookings.append(booking)

    # Update room availability
    rooms[room_num]["available"] = False

    # Print booking confirmation
    print("\n" + "="*50)
    print("     Booking Successful!")
    print("="*50)

    print(f"Booking ID     : {booking['id']}")
    print(f"Guest Name     : {booking['guest']}")
    print(f"Room Number    : {room_num}")
    print(f"Room Type      : {booking['type']}")
    print(f"Check-in Date  : {booking['checkin']}")
    print(f"Check-out Date : {booking['checkout']}")
    print(f"Nights         : {booking['nights']}")
    print(f"Guests         : {booking['guests']}")
    print(f"Price/Night    : {booking['price_per_night']} EGP")
    print(f"Total Price    : {booking['total']} EGP")

    print("="*50)

    return booking


def show_all_bookings():
    """Display all bookings"""

    print("\n" + "="*50)
    print("         All Bookings")
    print("="*50)

    if not bookings:
        print("No bookings yet.")

    else:
        for b in bookings:
            print(f"{b['id']} | {b['guest']} | "
                  f"Room {b['room']} | "
                  f"{b['checkin']} -> {b['checkout']} | "
                  f"{b['total']} EGP")

    print("="*50)


def cancel_booking(booking_id):
    """Cancel a booking"""

    for b in bookings:

        if b["id"] == booking_id:

            b["status"] = "Cancelled"

            # Make room available again
            rooms[b["room"]]["available"] = True

            print(f"\nBooking {booking_id} cancelled successfully.")
            return

    print(f"\nBooking ID {booking_id} not found.")


# ─────────────────────────────────────────
# Program Execution
# ─────────────────────────────────────────

print("========================================")
print("      Grand Azure Hotel System")
print("========================================")

# 1. Show available rooms
show_available_rooms()

# 2. Make bookings
print("\n--- Creating Bookings ---")

make_booking(
    guest_name = "Ahmed Mohamed",
    room_num   = "101",
    checkin    = "2026-06-01",
    checkout   = "2026-06-05",
    guests     = 2
)

make_booking(
    guest_name = "Sara Khaled",
    room_num   = "103",
    checkin    = "2026-06-10",
    checkout   = "2026-06-13",
    guests     = 1
)

# 3. Try booking reserved room
print("\n--- Trying Reserved Room ---")

make_booking(
    guest_name = "Mahmoud Ali",
    room_num   = "101",
    checkin    = "2026-06-07",
    checkout   = "2026-06-09",
    guests     = 1
)

# 4. Show all bookings
show_all_bookings()

# 5. Cancel booking
print("\n--- Cancel Booking ---")

cancel_booking("BK1001")

# 6. Show rooms after cancellation
show_available_rooms()