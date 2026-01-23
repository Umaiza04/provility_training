from turtle import fillcolor
from manim import *
from numpy import right_shift

class manim_practice(Scene):
    def construct(self):
       text=Text("ROBOGEBRA",color=BLUE,font_size=70).shift(UP*3)
       triangle=Triangle(fill_color=PINK,fill_opacity=0.5).scale(1.5).set_stroke(width=15)
       square=Square(fill_color=BLUE, fill_opacity=0.5).scale(1).set_stroke(width=15)
       circle=Circle(fill_color=GREEN, fill_opacity=0.5).set_stroke(width=15)
       circle.shift(LEFT*3)
       square.shift(RIGHT*3)
       self.add(triangle)
       self.add(square)
       self.add(circle)
       self.add(text)