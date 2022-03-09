from typing import Protocol


class Proto(Protocol):
    def draw(self):
        ...


class Lottery:
    def draw(self):
        ...


class Painter:
    def draw(self):
        ...


def f(x: Proto):
    x.draw()


f(Lottery())
f(Painter())
