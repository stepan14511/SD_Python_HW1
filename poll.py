from user import User

class Poll:
    """UI/UX of the poll.
    This is only an empty class, describing the interface of the Poll.

    Attributes:
        __questions     List of questions.

        __user          Variable, containing information about user and their answers.
    """

    __questions = None
    __user = None

    def __init__(self,
                 questions: list,
                 user: User):
        """Constructor of the class.
        """
        self.__questions = questions
        self.__user = user

    def startPoll(self):
        """Function, responsible for running the poll.
        This function is responsible of UI/UX itself.
        """
        pass

    def getUser(self) -> User:
        """Function, returning the user variable.
        """
        return self.__user