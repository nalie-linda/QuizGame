
# OOP class is defined without parentheses. Attributes are initialized in the init definition
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
