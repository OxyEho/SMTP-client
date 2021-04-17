from client.answer import Answer
from client.smtp_exception import SMTPException


class AnswerAnalyzer:

    @staticmethod
    def analyze_answer(answer: Answer):
        if answer.last_code > 499:
            raise SMTPException(answer.all_msg)
