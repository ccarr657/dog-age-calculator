# dog-age-calculator
Dog Age to Human Age Calculator

This is a full-stack web application that converts dog years to human years. It is build using Flask(Python) for backend processing and JavaScript/HTML/CSS for the frontend.

**Features:
  *Two input options:
    -Option A: Manually type a number into the textbox and click Calculate
    -Option B: Click the Say Age button and speak the number - speech to text input
  *After submitting the age, a Clear button appears to reset the results
  *Responsive interface for interactive accessible input

This project includes a CI pipeline using GitHub Actions that:
- In python-ci.yml, update ' run: python test_script.py '
- Installs dependencies from 'requirments.txt'
- Runs test_script.py to verify core logic
- Prevents Flask from hanging in a headless environment
