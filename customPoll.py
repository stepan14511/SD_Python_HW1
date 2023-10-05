from poll import Poll
from user import User

def saveResultsToJSON(filename):
    def decorator(func):
        def _wrapper(*args, **kwargs):
            user = func(*args, **kwargs)
            saveToJSON(user)
            return user
        
        def saveToJSON(user):
            f = open(filename, "w+")
            answers = user.getAnswers()

            f.write("{\n")
            f.write(f'\t"Name": "{user.name}",\n')

            f.write('\t"Answers": [\n')
            for a_index, answer in enumerate(answers):
                f.write("\t{\n")
                f.write(f'\t\t"Question": "{answer.getQuestion().getExplanation()}",\n')
                f.write(f'\t\t"Answer": "{answer.getAnswer()}",\n')
                f.write(f'\t\t"Result": {(str(answer.isRight()) if answer.isRight() is not None else "Null").lower()}\n')
                f.write("\t}"+ ("," if a_index + 1 != len(answers) else "") +"\n")
            
            f.write("\t]\n}")
        return _wrapper
    return decorator


class CustomPoll(Poll):
    """Poll with console interactions only. (For our set of questions only).
    """

    def __init__(self,
                 questions: list,
                 user: User):
        """Constructor of the class.
        """
        super().__init__(questions, user)

    @saveResultsToJSON("Results.json")
    def startPoll(self):
        """Runs the UI/UX.
        
        Returns the users' object."""

        isValidNumericAnswer = lambda n, n_max: n.isdigit() and int(n) < n_max

        print(f"Welcome to our poll, {self._Poll__user.name}!")
        print(f"During this poll you will be asked {len(self._Poll__questions)} questions.")
        print("Here they are:")
        for q_index, question in enumerate(self._Poll__questions):
            print("-----------------------------------------")
            print(f"Question #{q_index+1}:")
            print(question.getExplanation())

            possible_answers = question.getAnswers()
            if possible_answers is not None:
                print("Possible answers:")
                print(possible_answers)

            print(f"Enter your answer{' (number of the right answer only)' if possible_answers is not None else ''}:")

            answer = input()
            if possible_answers is not None:
                while not isValidNumericAnswer(answer, question.getAmountOfAnswers()):
                    print("Wrong answer format. Try again:")
                    answer = input()
                self._Poll__user.addAnswer(question.answer(question.getAnswerByIndex(int(answer))))
            else:
                self._Poll__user.addAnswer(question.answer(answer))

            print("Nice! Your answer is saved.")
            print("Proceeding to the next question...\n\n" if q_index + 1 != len(self._Poll__questions) else "", sep="")

        print("Your results:")
        for r_index, result in enumerate(self._Poll__user.getAnswers()):
            generateStrEval = lambda ans: str("Right" if ans.isRight() else "Wrong") if ans.isRight() is not None else "Will be evaluated later."
            print(f"{r_index}) {generateStrEval(result)}.")
        print("Thanks for the participation!")
        print("Your results are saved to the file Results.txt.")

        return self._Poll__user
