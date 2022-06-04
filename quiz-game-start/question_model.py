from mimetypes import guess_all_extensions


class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer 

