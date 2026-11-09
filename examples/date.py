import os
import sys
from pprint import pprint


sys.path.append(os.path.realpath("."))
import inquirer  # noqa


questions = [
    inquirer.Date(
        "day",
        message="When an error accured?"
    ),
]

answers = inquirer.prompt(questions)

pprint(answers)
