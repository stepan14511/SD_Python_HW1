from questionBase import QuestionBase

class SingleChoiseQuestion(QuestionBase):
    """Single choise question
    """
    
    def __init__(self,
                 questionExplanation: str,
                 questionAnswers: list,
                 isAutoCheck: bool = False,
                 rightAnswer: str = None):
        """Constructor of the class.
        Parameters:
            questionExplanation     The explanation of the question.

            questionAnswers         Answers for the questions.

            isAutoCheck             Does the question has particular right answer.

            rightAnswer             In case of existing right answer, this variable
                                    contains the information about the right answer.
        """
        super().__init__(questionExplanation, questionAnswers, isAutoCheck, rightAnswer)

    def getAnswers(self) -> str:
        """Function, which returns the generated answers' part of the UI.
        """
        output = ""
        for ans_id, ans in enumerate(self._QuestionBase__questionAnswers):
            output += f"{ans_id}) {ans}\n"
        return output
    
    def getAmountOfAnswers(self):
        """Return the number of possible answers.
        """
        return len(self._QuestionBase__questionAnswers)
    
    def getAnswerByIndex(self,
                         index):
        """Returns the answer by it's index.
        """
        return self._QuestionBase__questionAnswers[index]