from questionResult import QuestionResult

class User:
    """User class, describing users information and the results of a poll.
    
    Attributes:
        name        Name of the user.

        __answers   List of answers of the user.
                    Each answer must have type QuestionResult.
    """
    
    name = None
    __answers = []

    def __init__(self,
                 name):
        """Constructor of the class.
        """
        self.name = name
        self.__answers = []

    def addAnswer(self,
                  answer: QuestionResult):
        """Function, responsible for adding an answer to the user's answers.
        """
        self.__answers.append(answer)

    def getAnswers(self):
        """Functions returns the list of all answers made by the user.
        """
        return self.__answers