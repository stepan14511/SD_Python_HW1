class QuestionResult:
    """Class, responsible for storing the results of a particular question.

    Attributes:
        __question          The question itself.

        __answer            Chosen answer by user.

        __isRightAnswer     Possible values:
                                True -> right answer;
                                False -> wrong answer;
                                None -> question is not AutoChecked.
    """
    __question = None
    __answer = None
    __isRightAnswer = False

    def __init__(self,
                 question,
                 answer):
        """Constructor of the class.
        
        Question class must contain function isAnswerRight(self, answer), which
        returns:
            True -> right answer
            False -> wrong answer
            None -> question does not support auto check.
        """
        self.__question = question
        self.__answer = answer
        self.__isRightAnswer = question.isAnswerRight(answer)

    def isRight(self) -> bool:
        """Function, returning whether the answer is correct.
        Return Null if the question is not AutoChecked.
        """
        return self.__isRightAnswer

    def getQuestion(self):
        """Function, returning the object, containing the particular question.
        """
        return self.__question
    
    def getAnswer(self):
        """Function, returning the answer itself.
        """
        return self.__answer
