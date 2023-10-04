from questionResult import QuestionResult

class QuestionBase:
    """Basic class of a question in a poll.
    Idealy, to be inherited before usage.
    
    Attributes:
        __questionExplanation   The explanation of the question.

        __questionAnswers       Answers for the questions.

        __isAutoCheck           Does the question has particular right answer.

        __rightAnswer           In case of existing right answer, this variable
                                contains the information about the right answer.
    """

    __questionExplanation = None
    __questionAnswers = None
    __isAutoCheck = False
    __rightAnswer = None

    def __init__(self,
                 questionExplanation,
                 questionAnswers,
                 isAutoCheck = False,
                 rightAnswer = None):
        """Constructor of the class.
        """
        self.__questionExplanation = questionExplanation
        self.__questionAnswers = questionAnswers
        self.__isAutoCheck = isAutoCheck
        self.__rightAnswer = rightAnswer

    def getExplanation(self):
        """Function, which returns the generated explanation of the answer.
        In case of terminal interface, it must return str.
        """
        return str(self.__questionExplanation)
    
    def getAnswers(self):
        """Function, which returns the generated answers' part of the UI.
        In case of terminal interface, it must return str.
        """
        return str(self.__questionAnswers)
    
    def getRightAnswer(self):
        """Function, returning the right answer.
        If __isAutoCheck is False, then returns None.
        """
        if not self.__isAutoCheck:
            return None
        else:
            return self.__rightAnswer
        
    def isAnswerRight(self,
                      answer):
        """Function, responsible for checking, wheather the answer is correct.
        """
        if not self.__isAutoCheck:
            return None
        else:
            return self.__rightAnswer == answer
        
    def answer(self,
               answer = None):
        """Function, returning QuestionResult object with the answer.
        """
        return QuestionResult(self, answer)
