# Demo

This repository demonstrates integration with Codecov.

## Setup Instructions

1. **Add a Codecov Token:**
   - In your GitHub repository, navigate to **Settings** > **Secrets and variables** > **Actions**.
   - Click **New repository secret** and add your Codecov token with the name `CODECOV_TOKEN`.

2. **Clone the Repository:**
   - Clone this repository to your local machine.

3. **Install Dependencies:**
   - Run `pip install -r requirements.txt` to install the necessary Python packages.

4. **Run Tests:**
   - Execute `pytest --cov=src --cov-report=xml` to run tests and generate a coverage report.

5. **Continuous Integration:**
   - The repository is set up with GitHub Actions to run tests and upload coverage reports to Codecov on each push and pull request.
