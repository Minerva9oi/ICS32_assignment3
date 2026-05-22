# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# NAME Bozhang Zhou
# EMAIL bozhangz@uci.edu
# STUDENT ID 93213406

import shlex
from Profile import Profile, Post, DsuProfileError, DsuFileError
from pathlib import Path

def run():
    current_file= None
    current_profile=None
    while True:
        text=input()
        try:
            order_parts=shlex.split(text)
        except ValueError:
            print("ERROR")
            continue

        if len(order_parts)==0:
            print("ERROR")
            continue
        
        elif order_parts[0]=="Q":
            break
        elif order_parts[0]=="C":
            current_profile, current_file=create_file(order_parts, current_profile, current_file)
        elif order_parts[0]=="O":
            current_profile, current_file=open_file(order_parts, current_profile, current_file)
        elif order_parts[0]=="E":
            edit_profile(order_parts, current_profile, current_file)
        elif order_parts[0]=="P":
            print_profile(order_parts, current_profile, current_file)
        elif order_parts[0] == "R":
            read_file(order_parts)

        else:
            print("ERROR")
            continue

def create_file(order_parts, current_profile, current_file):
    if len(order_parts)!=4 or order_parts[2] != "-n":
        print("ERROR")
        return current_profile, current_file
    
    folder_path=Path(order_parts[1])
    if not folder_path.exists() or not folder_path.is_dir():
        print("ERROR")
        return current_profile, current_file
    journal_name=order_parts[3]
    if journal_name.strip()=='':
        print("ERROR")
        return current_profile, current_file
    
    file_path=folder_path/(journal_name+'.dsu')

    profile=Profile()
    if file_path.exists():
        try:
            profile.load_profile(file_path)
            print("profile loaded")
            return profile, file_path
        except (DsuFileError, DsuProfileError):
            print("ERROR")
            return current_profile, current_file
    user_name=input("username:")
    pass_word=input("password:")
    bio=input("bio:")

    if user_name.strip()=='' or pass_word.strip()=='' or bio.strip()=='':
        print("ERROR")
        return current_profile, current_file
    if " " in user_name or " " in pass_word:
        print("ERROR")
        return current_profile, current_file
    
    profile.username=user_name
    profile.password=pass_word
    profile.bio=bio
    try:
        file_path.touch()
        profile.save_profile(file_path)
        print(file_path)
        return profile, file_path
    except DsuFileError:
        print("ERROR")
        return current_profile, current_file


def open_file(order_parts, current_profile, current_file):
    if len(order_parts)!=2:
        print("ERROR")
        return current_profile, current_file
    file_path=Path(order_parts[1])
    if not file_path.exists() or not file_path.is_file() or file_path.suffix != ".dsu":
        print("ERROR")
        return current_profile, current_file
    profile=Profile()

    try:
        profile.load_profile(file_path)
        print("profile loaded")
        return profile, file_path
    except (DsuFileError, DsuProfileError):
        print("ERROR")
        return current_profile, current_file
    
def edit_profile(order_parts, current_profile, current_file):
    if current_profile is None or current_file is None:
        print("ERROR")
        return
    if len(order_parts)<3:
        print("ERROR")
        return
    index=1
    while index<len(order_parts):
        option=order_parts[index]

        if index+1 >= len(order_parts):
            print("ERROR")
            return
        
        value=order_parts[index+1]
        index +=2
        

        if option=="-usr":
            if value.strip()==''or' ' in value:
                print("ERROR")
                return
            current_profile.username=value

        elif option=="-pwd":
            if value.strip()==''or ' 'in value:
                print("ERROR")
                return
            current_profile.password=value

        elif option=='-bio':
            if value.strip()=='':
                print("ERROR")
                return
            current_profile.bio=value
        
        elif option=='-addpost':
            if value.strip()=='':
                print("ERROR")
                return
            post=Post(value)
            current_profile.add_post(post)
        
        elif option=='-delpost':
            try:
                delete_index=int(value)
            except ValueError:
                print("ERROR")
                return
            delete_resultbool=current_profile.del_post(delete_index)
            if delete_resultbool == False:
                print("ERROR")
                return

        else:
            print("ERROR")
            return
        

        try:
            current_profile.save_profile(str(current_file))
        except DsuFileError:
            print("ERROR")
            return
        
def print_profile(order_parts, current_profile, current_file):
    if current_profile is None or current_file is None:
        print("ERROR")
        return

    if len(order_parts) < 2:
        print("ERROR")
        return

    if order_parts[1] == "-usr":
        if len(order_parts) != 2:
            print("ERROR")
            return
        print(current_profile.username)

    elif order_parts[1] == "-pwd":
        if len(order_parts) != 2:
            print("ERROR")
            return
        print(current_profile.password)

    elif order_parts[1] == "-bio":
        if len(order_parts) != 2:
            print("ERROR")
            return
        print(current_profile.bio)

    elif order_parts[1] == "-posts":
        if len(order_parts) != 2:
            print("ERROR")
            return

        posts = current_profile.get_posts()

        for index in range(len(posts)):
            print(str(index) + ": " + posts[index].get_entry())

    elif order_parts[1] == "-post":
        if len(order_parts) != 3:
            print("ERROR")
            return

        try:
            post_id = int(order_parts[2])
        except ValueError:
            print("ERROR")
            return

        posts = current_profile.get_posts()

        if post_id < 0 or post_id >= len(posts):
            print("ERROR")
            return

        print(posts[post_id].get_entry())

    elif order_parts[1] == "-all":
        if len(order_parts) != 2:
            print("ERROR")
            return

        print("Username: " + str(current_profile.username))
        print("Password: " + str(current_profile.password))
        print("Bio: " + str(current_profile.bio))

        posts = current_profile.get_posts()

        for index in range(len(posts)):
            print(str(index) + ": " + posts[index].get_entry())

    else:
        print("ERROR")
        return

def read_file(text):
    if len(text)!=2:
        print("ERROR")
        return
    
    file_path=Path(text[1])

    if not file_path.exists() or not file_path.is_file() or file_path.suffix != ".dsu":
        print("ERROR")
        return
    else:
        content=file_path.read_text()
        
        if len(content)==0:
            print("EMPTY")
            return
        else:
            print(content, end='')