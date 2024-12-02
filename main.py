### Restaurant Reservation System



### Create classes

# Table class
class Table:
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        #self.capacity = capacity
        self.is_available = True


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



### Run main program
def main():
    while True:
        print("\n\n ---- Restaurant Reservation System ----\n")
        print("1: View available tables")
        print("2: View reservations")
        print("3: Make a reservation")
        print("4: Cancel a reservation")
        print("5: Exit")


main()