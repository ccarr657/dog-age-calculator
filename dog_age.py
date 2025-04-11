# dog-age-calculator
# Calculate dog age
def dog_to_human_years(dog_age):
    if dog_age <= 2:
        return dog_age * 10.5
    else:
        return 21 + (dog_age - 2) * 4

age = float(input("Enter your dog's age in years: "))
human_age = dog_to_human_years(age)
print(f"Your dog is about {human_age} human years old.")    