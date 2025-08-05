# pynotescli/commands/delete.py

import os

def run(title):
    filename = f"{title}.txt"
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted: {filename}")
    else:
        print(f"Note not found: {filename}")
