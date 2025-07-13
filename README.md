
This project serves as a game for the users, and this combines python Flask REST API backend with a C++ SFML graphical frontend and a C++ REST client. It manages players and game modes through a RESTful service and provides a simple interactive GUI.
As components there are:
- the REST API (rest.py)
Flask-based server handling players and game modes stored in JSON files. Supports CRUD operations via HTTP endpoints (/game, /players, /modes).

- the C++ REST Client (functions.cpp)
Uses cpr library to send JSON player data to the REST API (POST /game).

- the SFML Graphics App (graphics.cpp)
Displays a window with a player rectangle and score text. Loads a font and handles window events.
Also, for local use, some files .json were added:
- players.json — stores player info (name, age, score, level)
- modes.json — stores game modes (name, description, complexity, max players)

for building and running, the following steps should be followed :

1. Start Flask server:
python rest.py

2. Build and run C++ REST client (requires cpr):
g++ functions.cpp -o functions.exe -lcpr -lssl -lcrypto -lcurl
./functions.exe

3. Build and run SFML app (link SFML and include paths accordingly):
g++ graphics.cpp -o graphics.exe -I<include_path> -L<lib_path> -lsfml-graphics -lsfml-window -lsfml-system -mwindows
./graphics.exe

As requirements:
- Python 3.x with Flask
- C++17 or newer
- SFML library
- cpr HTTP library for C++
- vcpkg for dependency management 



