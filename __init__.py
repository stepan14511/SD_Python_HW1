import sys
sys.path.append('question_types')
sys.path.append('question_types/ConsoleQuestions')

from user import User
from customPoll import CustomPoll
from openAnswerQuestion import OpenAnswerQuestion
from singleChoiseQuestion import SingleChoiseQuestion

name = input("Type your name: ")
poll = [
    OpenAnswerQuestion("How old are you?"),
    OpenAnswerQuestion("How is your mood?"),
    SingleChoiseQuestion("How would you rate this poll?",
                         ["Excelent",
                          "Good",
                          "Ok",
                          "Bad",
                          "Awful"],
                          isAutoCheck = True,
                          rightAnswer = "Excelent"),
    SingleChoiseQuestion("Pick anything you want.",
                         ["1",
                          "2",
                          "3"]),
    SingleChoiseQuestion("Pick 1:",
                         ["0",
                          "1",
                          "2",
                          "3",
                          "4"],
                          isAutoCheck = True,
                          rightAnswer = "1"),
    SingleChoiseQuestion("Pick ANYTHING BUT 1 (to show result as Wrong):",
                         ["0",
                          "1",
                          "2",
                          "3",
                          "4"],
                          isAutoCheck = True,
                          rightAnswer = "1")
]

usersPoll = CustomPoll(poll, User(name))
usersPoll.startPoll()