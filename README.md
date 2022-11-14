# treblemusicapp

Treble

Summary: All-in-one independent songwriting, collaboration, production social network for musicians.

Domain (for now): www.treblemusicapp.com

Site Structure:

1. Homepage
    * News, site updates, songwriting news, top ranking uploads etc.
2. Jam Room (iffy on this one)
    * Upload jam tracks, sorted by genre, tempo, key etc.
    * ‘Walkie-talkie’ style jamming for back-and-forth engagement between users
3. Collaborate
    * Upload ‘building blocks’
        * Jam tracks to build on
        * Song project files
        * Upload individual instrument audio files
        * Upload lyrics
        * Etc.
    * Request ‘instrument fills’ (e.g. missing drums)
        * Document vision for song, what you are open to and what genre you are hoping for
    * Users can set their instrument and genre preference on profile page
        * Paired up with potential building blocks to contribute to
    * Voting on contributions
    * Reward and ranking system for contributors (giveaways etc.)
4. Sharing
    * Upload final or near final songs you have written
        * Either independently or
        * Through collaboration functionality
    * Feedback gathering and ranking from reviewers to writers
5. Production and Mastering
    * Upload demos or near final demos you have written
        * Either independently or
        * Through collaboration functionality
    * Independent producers can potentially be paid to finalize demos and upload mastered versions
    * Producers get ranking based on history and voting system for listeners
    * Unless completing contract without pay, only one producer should be working on a demo at a time (if not charging, but building portfolio and ranking, multiple can work on contract)
6. Rehearse
    * Find local rehearsal spaces and include friends or bandmates on reservation
    * Compare prices, availability, locations, sizes etc
    * Direct booking software
7. Record
    * Find local recording studios, sound engineers, and include friends or bandmates on reservation
    * Compare prices, availability, locations, sizes etc
    * Direct booking software
8. Forums, Chatrooms and FAQs
    * Misc music forums and chat-rooms (reddit style)
    * Sharing platform for experienced musicians, songwriters, and producers, to engage with learning audience, or to advertise gigs, network etc.
9. Chat (Friends and Collaborators)
    * Friends list can message and video chat directly
    * Other users can request chat (like IG) or request to be added to friend list
    * Collaborators put into separate list by project
10. Notifications
11. My Profile
    * Manage listener profile
    * Manage songwriter profile
    * Manage musican profile
    * Manage producer profile
    * Fun avatars and statistics on engagement metrics and contributions
    * Friend list
    * Band info, gig info, performance history
    * Manage portfolio of content through profile by type
    * Upload content and media to share (performances etc.)

## Development

From the project directory, do:
1. `cd backend`
2. `mkdir venv` to create a directory for you virtual environment
3. `python3 -m venv venv` to create the virtual environment in backend/venv
4. `source venv/bin/activate` to activate the virtual environment
5. `python3 -m pip install --upgrade pip` to update pip
5. `pip3 install -r requirements.txt` to install python dependencies
6. `export FLASK_DEBUG=true` to configure flask to use development mode with hot reloading
6. `flask run --host 0.0.0.0 --port 8080` to start the server

* Manage portfolio of content through profile by type

