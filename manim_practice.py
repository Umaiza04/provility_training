from manim import *
from numpy import right_shift

class manim_practice(Scene):
    def construct(self):
        triangle=Triangle().scale(1.5)
        square=Square().scale(1)
        circle=Circle()
        circle.shift(LEFT*3)
        square.shift(RIGHT*3)
        self.add(triangle)
        self.add(square)
        self.add(circle)
       