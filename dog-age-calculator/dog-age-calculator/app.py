from flask import Flask, render_template, request
from datetime import date
from converter import dog_to_human_years  # Import dog age calculation function
from athena_age import get_athena_age_string  # Import Athena age function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    human_age = None
    dog_age = None
    athena_birthdate = date(2024, 9, 7)  # Athena's birthday
    athena_age_str = get_athena_age_string(athena_birthdate)

    if request.method == "POST":
        try:
            dog_age = int(request.form["dog_age"])
            human_age = dog_to_human_years(dog_age)
            human_age = round(human_age, 2)
        except ValueError:
            human_age = "Please enter a valid number."

    return render_template("index.html", human_age=human_age, athena_age=athena_age_str)

if __name__ == "__main__":
    app.run(debug=True)