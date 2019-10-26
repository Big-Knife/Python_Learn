class AnonymousSurvey():
    """收集匿名调查问卷的答案"""

    def __init__(self,question):
        """储存一个问题，并为储存答案做准备"""
        self.question = question
        self.responses = []

    def