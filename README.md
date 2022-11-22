## Development

From the project directory, do:
1. `cd backend`
2. `mkdir venv` to create a directory for you virtual environment
3. `python3 -m venv venv` to create the virtual environment in backend/venv
4. `source venv/bin/activate` to activate the virtual environment
5. `python3 -m pip install --upgrade pip` to update pip
6. `pip3 install -r requirements.txt` to install python dependencies
7. `python3` to start python
8. `from app import db, User` to set import db into app
9. `db.create_all()` to start up db schema
10. `python3 app.py` to start the server

* If a new package is installed with pip, remember to `pip3 freeze > requirements.txt`

Open To Dos:

- Convert togglemenu to separate script
- Only show #profilepicheader if logged in
- Only show Login if not logged in
- Create tables and drop-downs for user preferences:
 - Songwriter:
  - Genre preferences
  - Years of experience
  - Portfolio/links
 - Musician:
  - Instruments played
  - Years of experience
  - Porfolio/links
- Lyricist:
  - Genre preferences
  - Portfolio/links
 - Producer:
  - Genre preferences
  - Years of experience
  - Portfilio/links
 - Listener:
  - Genre preferences
- Add db to store user preferences and info (including profile pic etc.)
- Update profile pic header to reference user settings once logged in
- Update profile page to show user settings when logged in
- Remove stuck cliker icon from My Profile page
- Accept TOS checkbox on register page not display text
- Validate email (low priority)
- Figure out way to show validation errors on register and login
    - Form submission causes a page redirect which makes flash('message') not work as intended I believe
- Configure flask_mail to send emails for new user registration and password reset
- Add favicon so logo shows in brower URL window
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
- Set up direct messages and sharing (attachement)
- Profit