import copy


class QuestionSix:
    def __init__(self):
        self.ignore_this = None


obj1 = QuestionSix()
obj1.x = 20
obj2 = copy.copy(obj1)
obj3 = copy.copy(obj2)
obj4 = copy.copy(obj1)
obj2.y = 5
obj4.x = 10
obj3.z = 30


a = 1
