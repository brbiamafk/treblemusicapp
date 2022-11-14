## Development

From the project directory, do:
1. `cd backend`
2. `mkdir venv` to create a directory for you virtual environment
3. `python3 -m venv venv` to create the virtual environment in backend/venv
4. `source venv/bin/activate` to activate the virtual environment
5. `python3 -m pip install --upgrade pip` to update pip
5. `pip3 install -r requirements.txt` to install python dependencies
6. `export FLASK_ENV=development` to configure flask to use development mode with hot reloading
6. `python3 app.py` to start the server

* If a new package is installed with pip, remember to `pip freeze > requirements.txt`
