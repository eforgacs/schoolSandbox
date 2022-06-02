class ParentClass(object):
    string_var = "a"


class ChildClass(ParentClass):
    another_string_var = "b"


child = ChildClass()

