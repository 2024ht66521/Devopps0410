# ACEest_Fitness - DevOps Assignment (End-to-end)

This repository contains a small Flask application (ACEest Fitness & Gym) and all DevOps-related files required by the assignment:
- Flask web app (`app.py`)
- Unit tests with `pytest` (`test_app.py`)
- `Dockerfile` to containerize the app
- GitHub Actions workflow to build the Docker image and run tests on push
- `requirements.txt`

## Run locally (virtualenv recommended)
1. Create virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
   The app will be available at http://127.0.0.1:5000

## Run tests locally
   ```bash
   pytest -q
   ```

## Build and run with Docker
   ```bash
   docker build -t aceest_fitness:latest .
   docker run --rm -p 5000:5000 aceest_fitness:latest
   ```
   Then open http://localhost:5000

## GitHub Actions / CI
The workflow located at `.github/workflows/ci.yml` will:
- Build the Docker image on each push to `main` or `master`
- Run `pytest` inside the built image

## Notes & Tips
- The Flask app uses an in-memory list for simplicity; this is suitable for the assignment but not for production.
- If you want to run tests inside CI without Docker, update the workflow to set up Python and run `pytest` directly.
