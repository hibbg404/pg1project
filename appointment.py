from datetime import datetime, timedelta

def book_appointment():
    new_booking = "Y"

    while new_booking == "Y":
        department = input("Enter department (GP/Specialist): ")

        appointment_date = input("Enter appointment date (DD/MM/YYYY): ")
        appointment_date = datetime.strptime(appointment_date, "%d/%m/%Y")
        today = datetime.today()

        while appointment_date < today + timedelta(days=7):
            print("Invalid date. Appointment must be at least 7 days ahead.")
            appointment_date = input("Enter appointment date (DD/MM/YYYY): ")
            appointment_date = datetime.strptime(appointment_date, "%d/%m/%Y")

        print("Appointment confirmed for", department, "on", appointment_date.strftime("%d/%m/%Y"))

        new_booking = input("Would you like to book another appointment? (Y/N): ")

    print("Returning to Main Menu")

# Run the function
book_appointment()
