# ==============================
# 1. REGISTER PATIENT
# ==============================

def register_patient():

    # Enter patient name
    while True:
        name = input("Enter patient name: ")

        if name.strip() == "":
            print("Error! Enter a valid name!")
        else:
            break

    # Enter patient age
    while True:
        age = input("Enter patient age: ")

        if not age.isdigit() or int(age) <= 0:
            print("Error! Enter a valid age!")
        else:
            age = int(age)
            break

    # Enter patient ID
    while True:
        patient_id = input("Enter patient ID: ")

        if patient_id.strip() == "":
            print("Error! Enter a valid ID!")
        else:
            break

    # Display patient information
    print("\nPatient Details:")
    print("Name:", name)
    print("Age:", age)
    print("ID:", patient_id)

    print("\nSuccessfully entered Patient Details!")


# ==============================
# 2. BOOK APPOINTMENT
# ==============================

def book_appointment():

    new_booking = "Y"

    while new_booking == "Y":

        # Enter department
        while True:
            department = input(
                "Enter department (GP/Specialist): "
            ).strip().lower()

            if department == "gp":
                department = "GP"
                break
            elif department == "specialist":
                department = "Specialist"
                break
            else:
                print("Invalid department. Please enter GP or Specialist.")

        # Enter appointment date
        while True:
            appointment_date = input(
                "Enter appointment date (DD/MM/YYYY): "
            )

            try:
                appointment_date = datetime.strptime(
                    appointment_date, "%d/%m/%Y"
                )

                today = datetime.today()

                if appointment_date.date() < (
                    today + timedelta(days=7)
                ).date():
                    print(
                        "Invalid date. Appointment must be at least 7 days ahead."
                    )
                else:
                    break

            except ValueError:
                print(
                    "Invalid date format. Please use DD/MM/YYYY."
                )

        print(
            "Appointment confirmed for",
            department,
            "on",
            appointment_date.strftime("%d/%m/%Y")
        )

        new_booking = input(
            "Would you like to book another appointment? (Y/N): "
        ).strip().upper()

        while new_booking not in ["Y", "N"]:
            print("Please enter Y or N.")
            new_booking = input(
                "Would you like to book another appointment? (Y/N): "
            ).strip().upper()

    print("\nReturning to Main Menu...")


# ==============================
# 3. CALCULATE CONSULTATION BILL
# ==============================

CONSULTATION_FEE = 100
LAB_TEST_RATE = 10


def calculate_total():

    # Get and validate patient type
    while True:
        patient_type = input(
            "Enter Patient Type (Subsidised/Private): "
        ).strip()

        if patient_type.lower() == "subsidised":
            patient_type = "Subsidised"
            discount = 0.70
            break

        elif patient_type.lower() == "private":
            patient_type = "Private"
            discount = 0
            break

        else:
            print(
                "Invalid patient type. "
                "Please enter Subsidised or Private."
            )

    # Get and validate number of lab tests
    while True:
        try:
            number_of_lab_tests = int(
                input("Enter number of lab tests: ")
            )

            if number_of_lab_tests >= 0:
                break
            else:
                print(
                    "Please enter a whole number of 0 or more."
                )

        except ValueError:
            print("Please enter a whole number.")

    # Calculate subtotal
    subtotal = (
        CONSULTATION_FEE
        + (number_of_lab_tests * LAB_TEST_RATE)
    )

    # Calculate discount
    discount_amount = subtotal * discount

    # Calculate total
    total = subtotal - discount_amount

    # Display bill
    print("\n--- Bill Summary ---")
    print("Patient Type:", patient_type)
    print("Subtotal: $", format(subtotal, ".2f"))
    print("Discount: $", format(discount_amount, ".2f"))
    print("Total: $", format(total, ".2f"))

    print("\nReturning to Main Menu...")


# ==============================
# 4. ASSIGN TRIAGE ROOM
# ==============================

def assign_triage_room():

    # Get and validate severity
    while True:
        try:
            severity = int(
                input("Enter severity level (1-10): ")
            )

            if severity < 1 or severity > 10:
                print(
                    "Invalid input. Please enter a whole number "
                    "from 1 to 10."
                )
            else:
                break

        except ValueError:
            print(
                "Invalid input. Please enter a whole number "
                "from 1 to 10."
            )

    # Assign room
    if severity >= 1 and severity <= 4:
        room = "Waiting Room"

    elif severity >= 5 and severity <= 7:
        room = "Room 1"

    else:
        room = "Room 2"

    # Display triage summary
    print("\n--- Triage Summary ---")
    print("Severity Level:", severity)
    print("Assigned Room:", room)

    print("\nReturning to Main Menu...")


# ==============================
# MAIN MENU
# ==============================

def main_menu():

    while True:

        print("\n==============================")
        print("       PATIENT MANAGEMENT")
        print("==============================")
        print("1. Register Patient")
        print("2. Book Appointment")
        print("3. Calculate Consultation Bill")
        print("4. Assign Triage Room")
        print("5. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_patient()

        elif choice == "2":
            book_appointment()

        elif choice == "3":
            calculate_total()

        elif choice == "4":
            assign_triage_room()

        elif choice == "5":
            print("\nThank you. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1-5.")


# ==============================
# START THE PROGRAM
# ==============================

main_menu()




