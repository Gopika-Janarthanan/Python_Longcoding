
class User:
    def __init__(self, user_id, name, email, password, contact_no, address):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.contact_no = contact_no
        self.address = address

    def display_user_details(self):
        print(f"User Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Contact Number: {self.contact_no}")
        print(f"Address: {self.address}")


class Chef:
    def __init__(self, chef_id, name, email, password, cuisines, price_per_hour, available):
        self.chef_id = chef_id
        self.name = name
        self.email = email
        self.password = password
        self.cuisines = cuisines
        self.price_per_hour = price_per_hour
        self.available = available

    def display_chef_details(self):
        print(f"Chef ID: {self.chef_id}")
        print(f"Chef Name: {self.name}")
        print(f"Cuisines: {', '.join(self.cuisines)}")
        print(f"Price per hour: {self.price_per_hour}")
        print(f"Available: {'Yes' if self.available else 'No'}")


class Booking:
    def __init__(self, booking_id, user, chef, booking_date, hours_booked, total_price, booking_status, payment_status):
        self.booking_id = booking_id
        self.user = user
        self.chef = chef
        self.booking_date = booking_date
        self.hours_booked = hours_booked
        self.total_price = total_price
        self.booking_status = booking_status
        self.payment_status = payment_status

    def display_booking_details(self):
        print(f"Booking ID: {self.booking_id}")
        print(f"User: {self.user.name}")
        print(f"Chef: {self.chef.name}")
        print(f"Booking Date: {self.booking_date}")
        print(f"Hours Booked: {self.hours_booked}")
        print(f"Total Price: {self.total_price}")
        print(f"Booking Status: {self.booking_status}")
        print(f"Payment Status: {self.payment_status}")


class ChefBookingApp:
    def __init__(self):
        self.users = []
        self.chefs = []
        self.bookings = []

    def register_user(self):
        user_id = len(self.users) + 1
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        contact_no = input("Enter your contact number: ")
        address = input("Enter your address: ")

        new_user = User(user_id, name, email, password, contact_no, address)
        self.users.append(new_user)
        print("User registered successfully!")

    def register_chef(self):
        chef_id = len(self.chefs) + 1
        name = input("Enter chef name: ")
        email = input("Enter chef email: ")
        password = input("Enter chef password: ")
        cuisines = input("Enter cuisines (comma-separated): ").split(',')
        price_per_hour = float(input("Enter price per hour: "))
        available = input("Is chef available? (yes/no): ").lower() == 'yes'

        new_chef = Chef(chef_id, name, email, password, cuisines, price_per_hour, available)
        self.chefs.append(new_chef)
        print("Chef registered successfully!")

    def list_available_chefs(self):
        available_chefs = [chef for chef in self.chefs if chef.available]
        if not available_chefs:
            print("No chefs available at the moment.")
        else:
            for chef in available_chefs:
                chef.display_chef_details()

    def book_chef(self):
        user_email = input("Enter your email to book a chef: ")
        user = next((u for u in self.users if u.email == user_email), None)
        if not user:
            print("User not found.")
            return

        self.list_available_chefs()
        chef_id = int(input("Enter the chef ID to book: "))
        chef = next((c for c in self.chefs if c.chef_id == chef_id and c.available), None)
        if not chef:
            print("Chef not found or unavailable.")
            return

        booking_date = input("Enter booking date (YYYY-MM-DD): ")
        hours_booked = int(input("Enter number of hours: "))
        total_price = hours_booked * chef.price_per_hour

        booking_id = len(self.bookings) + 1
        new_booking = Booking(
            booking_id, user, chef, booking_date,
            hours_booked, total_price, "Pending", "Unpaid"
        )
        self.bookings.append(new_booking)
        print("Chef booked successfully!")

    def view_bookings(self):
        if not self.bookings:
            print("No bookings available.")
        else:
            for booking in self.bookings:
                booking.display_booking_details()

    def chef_manage_booking(self):
        chef_email = input("Enter chef email: ")
        chef = next((c for c in self.chefs if c.email == chef_email), None)
        if not chef:
            print("Chef not found.")
            return

        chef_bookings = [b for b in self.bookings if b.chef == chef]
        if not chef_bookings:
            print("No bookings for this chef.")
        else:
            for booking in chef_bookings:
                booking.display_booking_details()
                action = input("Accept or Reject booking? (accept/reject): ").lower()
                if action == 'accept':
                    booking.booking_status = "Accepted"
                    booking.payment_status = "Paid"
                    print(f"Booking {booking.booking_id} accepted.")
                elif action == 'reject':
                    booking.booking_status = "Rejected"
                    print(f"Booking {booking.booking_id} rejected.")
                else:
                    print("Invalid action.")

app = ChefBookingApp()

while True:
    print("\n1. Register User\n2. Register Chef\n3. List Available Chefs\n4. Book a Chef\n5. View Bookings\n6. Chef Manage Bookings\n7. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        app.register_user()
    elif choice == 2:
        app.register_chef()
    elif choice == 3:
        app.list_available_chefs()
    elif choice == 4:
        app.book_chef()
    elif choice == 5:
        app.view_bookings()
    elif choice == 6:
        app.chef_manage_booking()
    elif choice == 7:
        print("Exiting application.")
        break
    else:
        print("Invalid choice. Try again.")

