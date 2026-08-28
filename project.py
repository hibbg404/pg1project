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

# Start 
# the program

register_patient()
