### Restaurant Reservation System

import time


### Create classes

# Table class
class Table:
    def __init__(self, table_number, capacity):
        self.__table_number = table_number
        self.__capacity = capacity
        self.__is_available = True

    @property
    def table_number(self):
        return self.__table_number
    
    @property
    def capacity(self):
        return self.__capacity

    def is_available(self):
        return self.__is_available
    
    def reserve_table(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False
    
    def __str__(self):
        status = "Available" if self.__is_available else "Reserved"
        return f"Table {self.__table_number} (Capacity: {self.__capacity}) - {status}"


tables = [Table(i, 4) for i in range(1, 6)]


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

reservations = []



### Create functions

# View available tables
def avail_tables(tables):
    print("\nAvailable tables:")
    for table in tables:
        if table.is_available:
            print(f"Table {table.table_number}")


# View reservations
def view_reservations():
    if not reservations:
        print("\nNo reservations found.")
        return


# Make reservation
def make_reservation(tables, reservations):
    print("\n\nCreating reservation...\n")

    # Get customer details
    name = input("Enter customer name: ")
    phone_number = input("Enter customer phone number: ")
    email = input("Enter customer email address: ")
    customer = Customer(name, phone_number, email)

    # Get reservation details
    reservation_type = input("Enter reservation type: (walk in or advance)").lower()
    reservation_date = input("Enter reservation date (YYYY-MM-DD): ")
    reservation_time = input("Enter reservation time (HH:MM): ")

    avail_tables(tables)
    table_number = int(input("\nEnter table number: "))
    table = next((table for table in tables if table.table_number == table_number and table.is_available), None)

    if table and table.is_available:
        table.reserve_table()
        reservation = Reservation(customer, reservation_type, reservation_date, reservation_time, table)
        reservations.append(reservation)
        print("\nReservation created.")

    else:
        print("\nTable not available.")



### Run main program
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
            view_reservations()
            time.sleep(1.5)

        elif choice == "3":
            make_reservation(tables, [])
            time.sleep(1.5)



main()