# utils.py
def get_dog_age_input():
    while True:
        try:
            age = float(input("Enter your dog's age in years: "))
            if age < 0:
                print("Age can't be negative! Please enter a valid age.")
            else:
                return age
        except ValueError:
            print("That's not a valid number! Please try again.")