### Virgil Padua - Restaurant Reservation System
### A reservation system for a restaurant that manages tables, reservations, and customers



import time



### Create classes

# Table class
class Table:
    def __init__(self, table_number):
        self.__table_number = table_number
        self.__is_available = True

    @property
    def table_number(self):
        return self.__table_number
    
    def is_available(self):
        return self.__is_available
    
    def reserve_table(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False
    
    def release_table(self):
        self.__is_available = True
    
    def __str__(self):
        status = "Available" if self.__is_available else "Reserved"
        return f"Table {self.__table_number} - {status}"

tables = [Table(i) for i in range(1, 6)]


# Customer class
class Customer:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email


# Reservation class
class Reservation:
    def __init__(self, customer, reservation_type,reservation_date,reservation_time, table):
        self.customer = customer
        self.reservation_type = reservation_type
        self.reservation_date = reservation_date
        self.reservation_time = reservation_time
        self.table = table

    def priority_seating(self):
        return "Normal Seating"

created_reservations = []

# Walk in reservation subclass
class WalkInReservation(Reservation):
    def __init__(self, customer, reservation_type, reservation_date, reservation_time, table):
        super().__init__(customer, reservation_type, reservation_date, reservation_time, table)


# Advance Reservation subclass
class AdvanceReservation(Reservation):
    def __init__(self, customer, reservation_type, reservation_date, reservation_time, table):
        super().__init__(customer, reservation_type, reservation_date, reservation_time, table)

    # Return High Priority for Advance Reservations
    def priority_seating(self):
        return "High Priority Seating"



### Create functions

# View available tables
def avail_tables(tables):
    print("\nAvailable tables:")
    
    # Print available tables
    for table in tables:
        if table.is_available():
            print(f"Table {table.table_number}")


# View reservations
def view_reservations(reservations):
    if not reservations:
        print("\nNo reservations found.")
        return
    
    # Print all reservation details 
    else:
        print("\n\nCurrent reservations:")
        for reservation in reservations:
            print(f"\nCustomer details: {reservation.customer.name} | {reservation.customer.phone_number} | {reservation.customer.email} \nReservation details: Table {reservation.table.table_number} | {reservation.reservation_type} | {reservation.reservation_date} | {reservation.reservation_time}\n\n")


# Determine priority of a reservation
def handle_seating(reservation):
    if reservation.priority_seating() == "High Priority Seating":
        print("\nAdvanced Reservation: High Priority Seating")
    else:
        print("\nWalk in Reservation: Normal Seating")


# Make a reservation
def make_reservation(tables, reservations):
    print("\n\nCreating reservation...\n")

    # Get customer details
    name = input("Enter customer name: ").upper()
    phone_number = input("Enter customer phone number: ")
    email = input("Enter customer email address: ").lower()
    customer = Customer(name, phone_number, email)

    # Get reservation details
    reservation_type = input("Enter reservation type: (walk in or advance) ").upper()
    reservation_date = input("Enter reservation date (YYYY-MM-DD): ")
    reservation_time = input("Enter reservation time (HH:MM): ")

    # List available tables
    avail_tables(tables)
    table_number = int(input("\nEnter table number: "))
    table = next((table for table in tables if table.table_number == table_number and table.is_available), None)

    # Reserve selected table
    if table and table.is_available:
        table.reserve_table()

        # Handle seating based on priority
        if reservation_type == "WALK IN":
            reservation = WalkInReservation(customer, reservation_type, reservation_date, reservation_time, table)

        else:
            reservation = AdvanceReservation(customer, reservation_type, reservation_date, reservation_time, table)
        
        created_reservations.append(reservation)
        print("\n\nReservation created.")
        handle_seating(reservation) 
        
    else:
        print("\nTable not available.")


# Cancel a reservation
def cancel_reservation(name, reservation_date):
    for reservation in created_reservations:
        
        # Find matches 
        if reservation.customer.name == name and reservation.reservation_date == reservation_date:
            reservation.table.release_table()
            created_reservations.remove(reservation)
            print("\n\nReservation canceled.")
            return



### Main loop
def main():
    while True:
        print("\n\n\n ---- Restaurant Reservation System ---- \n")
        print("1: View available tables")
        print("2: View reservations")
        print("3: Make a reservation")
        print("4: Cancel a reservation")
        print("5: Exit")

        choice = input("\nInput the number of what you would like to do: ")

        if choice == "1":
            avail_tables(tables)
            time.sleep(1.5)
        
        elif choice == "2":
            view_reservations(created_reservations)
            time.sleep(2.5)

        elif choice == "3":
            make_reservation(tables, [])
            time.sleep(2.5)

        elif choice == "4":
            name = input("Enter customer name: ").upper()
            reservation_date = input("Enter reservation date (YYYY-MM-DD): ")
            cancel_reservation(name, reservation_date)
            time.sleep(1.5)

        else:
            break



### Run program
main()
