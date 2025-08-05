# pynotescli/main.py

import argparse
from pynotescli.commands import create, list_notes, delete

def main():
    parser = argparse.ArgumentParser(prog="pynotes", description="Note-taking CLI")
    subparsers = parser.add_subparsers(dest="command")

    # create
    create_parser = subparsers.add_parser("create", help="Create a new note")
    create_parser.add_argument("title", help="Note title")

    # list
    subparsers.add_parser("list", help="List existing notes")

    # delete
    delete_parser = subparsers.add_parser("delete", help="Delete a note")
    delete_parser.add_argument("title", help="Title of note to delete")

    args = parser.parse_args()

    if args.command == "create":
        create.run(args.title)
    elif args.command == "list":
        list_notes.run()
    elif args.command == "delete":
        delete.run(args.title)
    else:
        parser.print_help()
