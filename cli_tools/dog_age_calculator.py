# dog_age_calculator.py
from converter import dog_to_human_years
from utils import get_dog_age_input

# Get dog's age from user input
age = get_dog_age_input()

# Calculate human equivalent age
human_age = dog_to_human_years(age)

# Output the result
print(f"Your dog is about {human_age} human years old.")