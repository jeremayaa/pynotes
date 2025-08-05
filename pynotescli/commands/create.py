# pynotescli/commands/create.py

import subprocess

def run(title):
    filename = f"{title}.txt"
    with open(filename, "w") as f:
        f.write("")
    subprocess.run(["open", filename])
    print(f"Note created and opened: {filename}")
