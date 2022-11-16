## Development

From the project directory, do:
1. `cd backend`
2. `mkdir venv` to create a directory for you virtual environment
3. `python3 -m venv venv` to create the virtual environment in backend/venv
4. `source venv/bin/activate` to activate the virtual environment
5. `python3 -m pip install --upgrade pip` to update pip
5. `pip3 install -r requirements.txt` to install python dependencies
6. `python3 app.py` to start the server

* If a new package is installed with pip, remember to `pip3 freeze > requirements.txt`

Open To Dos:

- Fix password validation (new user submit getting hung)
- Find out why users aren't submitting (maybe related to validations)
- Configure flask_mail to send emails for new user registration and password reset
- Add favicon so logo shows in brower URL window
- Add db to store user preferences and info (including profile pic etc.)
- Create social media accounts and update links
- Set up file uploads to server
- Link file uploads to upload buttons
- Design page layouts and css (near final)
- Set up initial voting and like system
- Configure way to show:
    - User uploaded files (in profile, and selector for sharing)
    - Top 10 files by <attribute> which can be metadata associated with files
- Set up comments on shared files
- Set up friend requests and lists
- Set up direct messages and sharing (attachements)
- Profit