Assignment3 readme

# NAME Bozhang Zhou
# EMAIL bozhangz@uci.edu
# STUDENT ID 93213406

This assignment includes the following starter files:

a3.py: Use this file as the main module for your program.
ds_protocol.py: This file creates and parses DSP JSON protocol messages. It creates join, post, and bio messages, and parses server responses.
ds_client.py: This file handles socket communication with the DSP server.
Profile.py: This file contains the Profile and Post classes used to store username, password, bio, DSP server address, and journal posts.
server.py: This is the provided local DSP server used for testing.
ui.py: This file handles user commands, local profile editing, post management, and online publishing commands.
README.txt: Instructions
templates/: This folder contains the Flask HTML templates used by server.py to display posts and user profiles in the browser.


Please visit the course Canvas for a detailed overview of the assignment.

Operation:

First, start the DSP server in one terminal:

python3 server.py

The DSP socket server runs on port 3001 by default.
The Flask web page runs on port 3002 by default.

Then, open another terminal and run the journal program:

python3 a3.py


Supported Commands:

C: Creating a new dsu journal file in the specified directory. If the file already exists, the program loads the existing profile.

O: Opening an existing dsu file and loads the profile.

E -usr: Updating the username. The username cannot be empty or contain spaces.

E -pwd: Updating the password. The password cannot be empty or contain spaces.

E -bio: Updating the profile bio.

E -addpost: Adding a new post to the profile.

E -delpost: Deleteing a post by index.

P -usr: Printing the username.

P -pwd: Printing the password.

P -bio: Printing the bio.

R [file_path]
Reads and prints the raw contents of a .dsu file. If the file is empty, it prints EMPTY.

Q
Quits the program.

P -posts:
Prints all posts.

P -post [index]:
Prints one specific post by index.

P -all:
Prints the username, password, bio, and all posts.

R <file_path>
Read and print the raw contents of a .dsu file. If the file is empty, the program prints EMPTY.

Example:

C . -n test_a3

When prompted, enter:

username: ethan_test
password: password123
bio: this is my bio
server: 127.0.0.1

Then add a post:

E -addpost "hello from UI"

Publish the post:

E -publishpost 0

Publish the bio:

E -publishbio yes

To view published posts, open this page in a browser:

http://127.0.0.1:3002/posts