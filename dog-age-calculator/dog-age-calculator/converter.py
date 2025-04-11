# converter.py
def dog_to_human_years(dog_age):
    if dog_age <= 2:
        return dog_age * 10.5
    else:
        return 21 + (dog_age - 2) * 4