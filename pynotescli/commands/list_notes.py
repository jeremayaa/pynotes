# pynotescli/commands/list_notes.py

import os

def run():
    for file in os.listdir():
        if file.endswith(".txt"):
            print(f"- {file}")
