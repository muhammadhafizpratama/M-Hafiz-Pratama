import json
from pathlib import Path

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path(r'C:\Users\LENOVO\nexen\exercise 10\user_info.json')
    username = get_stored_username(path)
    
    if username:
        correct = input(f"Are you {username}? (y/n): ")
        if correct.lower() == 'y':
            print(f"Welcome back, {username}!")
            return


    username = get_new_username(path)
    print(f"We'll remember you when you come back, {username}!")

greet_user()