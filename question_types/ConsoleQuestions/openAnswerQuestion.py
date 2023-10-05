from questionBase import QuestionBase

class OpenAnswerQuestion(QuestionBase):
    """Question with open answer.
    """
    
    def __init__(self,
                 questionExplanation: str):
        """Constructor of the class.
        Parameters:
            questionExplanation     The explanation of the question.
        """
        super().__init__(questionExplanation)