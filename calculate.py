CONSULTATION_FEE = 100
LAB_TEST_RATE = 10


def calculate_total():
    # Get and validate patient type
    while True:
        PatientType = input("Enter Patient Type (Subsidised/Private): ").strip()

        if PatientType.lower() == "subsidised":
            PatientType = "Subsidised"
            Discount = 0.70
            break
        elif PatientType.lower() == "private":
            PatientType = "Private"
            Discount = 0
            break
        else:
            print("Invalid patient type. Please enter Subsidised or Private.")

    # Get and validate number of lab tests
    while True:
        try:
            NumberOfLabTest = int(input("Enter number of lab tests: "))

            if NumberOfLabTest >= 0:
                break
            else:
                print("Please enter a whole number of 0 or more.")

        except ValueError:
            print("Please enter a whole number.")

    # Calculate subtotal
    Subtotal = CONSULTATION_FEE + (NumberOfLabTest * LAB_TEST_RATE)

    # Calculate discount
    DiscountAmount = Subtotal * Discount

    # Calculate total
    Total = Subtotal - DiscountAmount

    print("\n--- Bill Summary ---")
    print("Patient Type:", PatientType)
    print("Subtotal: $", format(Subtotal, ".2f"))
    print("Discount: $", format(DiscountAmount, ".2f"))
    print("Total: $", format(Total, ".2f"))


def main_menu():
    while True:
        print("\n===== MAIN MENU =====")
        print("1. Calculate Consultation Bill")
        print("2. Exit")

        Choice = input("Enter your choice: ")

        if Choice == "1":
            calculate_total()

        elif Choice == "2":
            print("Thank you. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1 or 2.")


# Start the program
main_menu()