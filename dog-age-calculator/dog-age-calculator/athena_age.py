from datetime import date

def get_athena_age_string(birthdate):
    today = date.today()
    age_in_days = (today - birthdate).days
    age_in_years = age_in_days / 365
    if age_in_years < 1:
        age_in_months = round(age_in_days / 30) # If under 1 year, divide by 30 - average days in months
        return f"{age_in_months} month{'s' if age_in_months != 1 else ''} old"
    else:
        age_in_years = round(age_in_years, 2)
        return f"{age_in_years} year{'s' if age_in_years != 1 else ''} old" # Age in years