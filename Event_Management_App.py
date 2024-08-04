class User:
  
    def __init__(self, user_id, user_name, password, email, contact_no, address):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.email = email
        self.contact_no = contact_no
        self.address = address

    def list_user_details(self):
        print(f"User ID: {self.user_id}")
        print(f"User Name: {self.user_name}")
        print(f"Email: {self.email}")
        print(f"Contact Number: {self.contact_no}")
        print(f"Address: {self.address}")

class Admin:
  
    def __init__(self, admin_id, admin_name, a_password):
        self.admin_id = admin_id
        self.admin_name = admin_name
        self.a_password = a_password

class EventOrganizer:
  
    def __init__(self, event_organizer_id, event_organizer_name, contact_no, email, eo_password):
      
        self.event_organizer_id = event_organizer_id
        self.event_organizer_name = event_organizer_name
        self.contact_no = contact_no
        self.email = email
        self.eo_password = eo_password

    def list_event_organizer_details(self):
      
        print(f"Event Organizer ID: {self.event_organizer_id}")
        print(f"Event Organizer Name: {self.event_organizer_name}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.contact_no}")

    def add_event(self, app):
      
        event_name = input("Enter event name: ")
        date = input("Enter event date (YYYY-MM-DD): ")
        time = input("Enter event time (HH:MM): ")
        location = input("Enter event location: ")
        description = input("Enter event description: ")
        category_name = input("Enter event category name: ")

        category = next((c for c in app.categories if c.category_name == category_name), None)
        if not category:
            print("Category not found.")
            return
        category_id = category.category_id

        event_id = len(app.events) + 1
        event = Event(event_id, event_name, date, time, location, description, category_id, category_name)
        app.events.append(event)
        print("Event added successfully!")

class Category:
  
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name

    def list_category_details(self):
        print(f"Category ID: {self.category_id}")
        print(f"Category Name: {self.category_name}")

class Event:
  
    def __init__(self, event_id, event_name, date, time, location, description, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name
        self.event_id = event_id
        self.event_name = event_name
        self.date = date
        self.time = time
        self.location = location
        self.description = description

    def list_event_details(self):
        print(f"Event ID: {self.event_id}")
        print(f"Event Name: {self.event_name}")
        print(f"Event Date: {self.date}")
        print(f"Event Time: {self.time}")
        print(f"Event Location: {self.location}")
        print(f"Event Description: {self.description}")

class Ticket:
  
    def __init__(self, ticket_id, event_id, ticket_type, price, ticket_availability):
        self.ticket_id = ticket_id
        self.event_id = event_id
        self.ticket_type = ticket_type
        self.price = price
        self.ticket_availability = ticket_availability

    def list_ticket_details(self):
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Ticket Type: {self.ticket_type}")
        print(f"Event Ticket Price: {self.price}")
        print(f"Ticket Availability: {self.ticket_availability}")

class Booking:
  
    def __init__(self, booking_id, user_name, event_organizer_name, category_name, event_name, ticket_id, payment_status, booking_status):
        self.booking_id = booking_id
        self.user_name = user_name
        self.event_organizer_name = event_organizer_name
        self.category_name = category_name
        self.event_name = event_name
        self.ticket_id = ticket_id
        self.payment_status = payment_status
        self.booking_status = booking_status

    def list_booking_details(self, users, event_organizers, categories, events, tickets):
        user = next((u for u in users if u.user_name == self.user_name), None)
        event_organizer = next((eo for eo in event_organizers if eo.event_organizer_name == self.event_organizer_name), None)
        category = next((c for c in categories if c.category_name == self.category_name), None)
        event = next((e for e in events if e.event_name == self.event_name), None)
        ticket = next((t for t in tickets if t.ticket_id == self.ticket_id), None)

        if user and event_organizer and category and event and ticket:
            print(f"Booking Details:-")
            print(f"Booking ID: {self.booking_id}")
            print("Category Details:")
            category.list_category_details()
            print("User Details:")
            user.list_user_details()
            print("Event Organizer Details:")
            event_organizer.list_event_organizer_details()
            print("Event Details:")
            event.list_event_details()
            print("Ticket Details:")
            ticket.list_ticket_details()
            print(f"Payment Status: {self.payment_status}")
            print(f"Booking Status: {self.booking_status}")
        else:
            print("Booking details not found.")

class EventManagementApp:
    def __init__(self):
        self.users = [
            User(1, 'Raj', 'password1', 'raj@gamil.com', '1234567890', 'Mumbai'),
            User(2, 'Aarti', 'password2', 'aarti@gmail.com', '0987654321', 'Delhi')
        ]
        self.event_organizers = [
            EventOrganizer(1, 'Vikram', '1987651125', 'vikram@gmail.com', 'password1'),
            EventOrganizer(2, 'Neha', '2223344556', 'neha@gmail.com', 'password2')
        ]
        self.categories = [
            Category(1, 'Music'),
            Category(2, 'Sports')
        ]
        self.events = [
            Event(1, 'Music Fest', '2024-09-01', '18:00', 'Mumbai Arena', 'A grand music festival.', 1, 'Music'),
            Event(2, 'Football Match', '2024-09-15', '16:00', 'Delhi Stadium', 'Exciting football match.', 2, 'Sports')
        ]
        self.tickets = [
            Ticket(1, 1, 'General', 500, 100),
            Ticket(2, 2, 'VIP', 1500, 50)
        ]
        self.admins = [Admin('admin', 'Admin', 'admin')]

    def app(self):
        while True:
            print("1. Register")
            print("2. User Login")
            print("3. Admin Login")
            print("4. Event Organizer Login")
            print("5. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.register()
            elif choice == "2":
                self.user_login()
            elif choice == "3":
                self.admin_login()
            elif choice == "4":
                self.event_organizer_login()
            elif choice == "5":
                print("Thank You!!!")
                break
            else:
                print("Invalid input")

    def register(self):
        print("1. Register as User")
        print("2. Register as Event Organizer")

        choice = input("Enter your choice: ")
        if choice == "1":
            self.user_register()
        elif choice == "2":
            self.event_organizer_register()
        else:
            print("Invalid choice")

    def user_register(self):
        user_id = len(self.users) + 1
        user_name = input("Enter your name: ")
        password = input("Enter your password: ")
        email = input("Enter your email: ")
        contact_no = input("Enter your contact number: ")
        address = input("Enter your address: ")
        new_user = User(user_id, user_name, password, email, contact_no, address)
        self.users.append(new_user)
        print("User registered successfully!")
        self.user_homepage(new_user)

    def event_organizer_register(self):
        event_organizer_id = len(self.event_organizers) + 1
        event_organizer_name = input("Enter your name: ")
        contact_no = input("Enter your contact number: ")
        email = input("Enter your email: ")
        eo_password = input("Enter your password: ")
        new_event_organizer = EventOrganizer(event_organizer_id, event_organizer_name, contact_no, email, eo_password)
        self.event_organizers.append(new_event_organizer)
        print("Event Organizer registered successfully!")

    def user_login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user = next((u for u in self.users if u.email == email and u.password == password), None)
        if user:
            print("Login successful!")
            self.user_homepage(user)
        else:
            print("Invalid email or password.")

    def admin_login(self):
        admin_id = input("Enter your admin ID: ")
        a_password = input("Enter your password: ")
        admin = next((a for a in self.admins if a.admin_id == admin_id and a.a_password == a_password), None)
        if admin:
            print("Login successful!")
            self.admin_homepage(admin)
        else:
            print("Invalid admin ID or password.")

    def event_organizer_login(self):
        email = input("Enter your email: ")
        eo_password = input("Enter your password: ")
        event_organizer = next((eo for eo in self.event_organizers if eo.email == email and eo.eo_password == eo_password), None)
        if event_organizer:
            print("Login successful!")
            self.event_organizer_homepage(event_organizer)
        else:
            print("Invalid email or password.")

    def user_homepage(self, user):
        while True:
            print("User Homepage")
            print("1. Search for Events")
            print("2. Search for Category")
            print("3. View Categories")
            print("4. Logout")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.search_events(user)
            elif choice == "2":
                self.search_categories()
            elif choice == "3":
                self.view_categories(user)
            elif choice == "4":
                print("Logged out successfully!")
                break
            else:
                print("Invalid choice")

    def search_categories(self):
        search_term = input("Enter category name to search: ")
        results = [c for c in self.categories if search_term.lower() in c.category_name.lower()]
        if results:
            print("Categories found:")
            for category in results:
                category.list_category_details()
        else:
            print("No categories found.")

    def search_events(self, user):
        search_term = input("Enter event name to search: ")
        results = [e for e in self.events if search_term.lower() in e.event_name.lower()]
        if results:
            print("Events found:")
            for event in results:
                event.list_event_details()
                self.list_ticket_details(event.event_id)
                print("1. See Ticket")
                print("2. Book Event")
                choice = input("Enter your choice: ")
                if choice == "1":
                    self.list_ticket_details(event.event_id)
                elif choice == "2":
                    self.book_event(user, event)
                else:
                    print("Invalid choice")
        else:
            print("No events found.")

    def view_categories(self, user):
        print("All Categories:")
        for category in self.categories:
            category.list_category_details()
            self.list_events_by_category(category.category_id, user)

    def list_events_by_category(self, category_id, user):
        events_in_category = [event for event in self.events if event.category_id == category_id]
        if events_in_category:
            print(f"Events in Category {category_id}:")
            for event in events_in_category:
                event.list_event_details()
                self.list_ticket_details(event.event_id)
                print("1. See Ticket")
                print("2. Book Event")
                choice = input("Enter your choice: ")
                if choice == "1":
                    self.list_ticket_details(event.event_id)
                elif choice == "2":
                    self.book_event(user, event)
                else:
                    print("Invalid choice")
        else:
            print("No events in this category.")

    def list_ticket_details(self, event_id):
        tickets = [t for t in self.tickets if t.event_id == event_id]
        if tickets:
            for ticket in tickets:
                ticket.list_ticket_details()
        else:
            print("No tickets found for this event.")

    def book_event(self, user, event):
        ticket_id = input("Enter ticket ID to book: ")
        ticket = next((t for t in self.tickets if t.ticket_id == int(ticket_id)), None)
        if ticket and ticket.ticket_availability > 0:
            booking_id = len(self.bookings) + 1
            booking = Booking(booking_id, user.user_name, 'Event Organizer Name', event.category_name, event.event_name, ticket_id, "Paid", "Confirmed")
            self.bookings.append(booking)
            ticket.ticket_availability -= 1
            print("Event booked successfully!")
        else:
            print("Invalid ticket ID or no tickets available.")

    def admin_homepage(self, admin):
        while True:
            print("Admin Homepage")
            print("1. View all Users")
            print("2. View all Event Organizers")
            print("3. View all Bookings")
            print("4. Logout")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.view_all_users()
            elif choice == "2":
                self.view_all_event_organizers()
            elif choice == "3":
                self.view_all_bookings()
            elif choice == "4":
                print("Logged out successfully!")
                break
            else:
                print("Invalid choice")

    def view_all_users(self):
        print("All Users:")
        for user in self.users:
            user.list_user_details()

    def view_all_event_organizers(self):
        print("All Event Organizers:")
        for event_organizer in self.event_organizers:
            event_organizer.list_event_organizer_details()

    def view_all_bookings(self):
        print("All Bookings:")
        for booking in self.bookings:
            booking.list_booking_details(self.users, self.event_organizers, self.categories, self.events, self.tickets)

    def event_organizer_homepage(self, event_organizer):
      
        while True:
            print("Event Organizer Homepage")
            print("1. Add Event")
            print("2. Logout")

            choice = input("Enter your choice: ")
            if choice == "1":
                event_organizer.add_event(self)
            elif choice == "2":
                print("Logged out successfully!")
                break
            else:
                print("Invalid choice")

app = EventManagementApp()
app.app()
