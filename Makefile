# Define variables
VENV_NAME=venv
PYTHON=python  # Use 'python' on Windows instead of 'python3'
PIP=$(VENV_NAME)/Scripts/pip  # On Windows, pip is located in the Scripts folder
DJANGO_PORT=8000
DJANGO_APP=FinalProject

# Create a virtual environment
venv:
	$(PYTHON) -m venv $(VENV_NAME)
	$(PIP) install --upgrade pip

# Install dependencies
install: venv
	$(PIP) install -r requirements.txt

# Run Django app
run:
	$(VENV_NAME)/Scripts/python manage.py runserver $(DJANGO_PORT)

# Migrate database
migrate:
	$(VENV_NAME)/Scripts/python manage.py migrate

# Create superuser
createsuperuser:
	$(VENV_NAME)/Scripts/python manage.py createsuperuser

# Run all necessary commands to set up and start the app
setup: install migrate run

# Stop the server (ctrl + c stops the server manually)
stop:
	@echo "Stop the Django server by pressing Ctrl+C"

# Clean virtual environment
clean:
	rm -rf $(VENV_NAME)
