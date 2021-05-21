import copy


class QuestionThree:
    def __init__(self):
        self.ignore_this = None


obj1 = QuestionThree()
obj1.x = "Hello"
obj2 = copy.copy(obj1)
obj3 = copy.copy(obj2)
obj4 = copy.copy(obj1)
obj2.x = 6
obj2.y = "World"
obj4.x = 22


a = 1
