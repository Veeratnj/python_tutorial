"""
Match-Case Statement

Example and comments for Match-Case Statement.
"""

# Match-Case Statement
command = "start"
match command:
    case "start":
        print("Starting")
    case "stop":
        print("Stopping")
    case _:
        print("Unknown command")
