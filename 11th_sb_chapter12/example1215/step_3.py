from turtle import fillcolor

from manim import *
import numpy as np

config.frame_height = 10
config.frame_width = 15
config.pixel_width = 2800
config.pixel_height = 2800


class Step_3(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        rectangle = Rectangle(
            width=10, height=6.5,
            stroke_color="#990F4B",
            fill_color="#FFF9E5",
            fill_opacity=0.8,
            stroke_width=4)
        s_label = Text("U", color=BLACK, font_size=45).next_to(rectangle, UR, buff=0.2).shift(LEFT*1)

        r = 2.4
        c1 = np.array([-1.3, 0, 0])
        c2 = np.array([1.3, 0, 0])
        circle_1 = Circle(radius=r, stroke_color="#990F4B",stroke_width=4,fill_color="#FCE4EC").move_to(c1).set_z_index(1)
        circle_2 = Circle(radius=r, stroke_color="#990F4B",stroke_width=4).move_to(c2)

        intersection = Intersection(circle_1, circle_2,stroke_width=0,fill_color=WHITE,fill_opacity=1)

        hatch = VGroup()
        spacing = 0.5
        angle = PI/4.2

        direction = np.array([np.cos(angle), np.sin(angle), 0])
        normal = np.array([-direction[1], direction[0], 0])

        for t in np.arange(-12, 12, spacing):
            base = t * normal
            eps = 0.01

            diff1 = base - c1
            a = np.dot(direction, direction)
            b1 = 2 * np.dot(diff1, direction)
            c_1 = np.dot(diff1, diff1) - r**2
            disc1 = b1*b1 - 4*a*c_1

            segs1 = []
            if disc1 >= 0:
                s1 = (-b1 - np.sqrt(disc1)) / (2*a)
                s2 = (-b1 + np.sqrt(disc1)) / (2*a)
                segs1.append((s1, s2))

            diff2 = base - c2
            b2 = 2 * np.dot(diff2, direction)
            c_2 = np.dot(diff2, diff2) - r**2
            disc2 = b2*b2 - 4*a*c_2

            segs2 = []
            if disc2 >= 0:
                t1 = (-b2 - np.sqrt(disc2)) / (2*a)
                t2 = (-b2 + np.sqrt(disc2)) / (2*a)
                segs2.append((t1, t2))
            for s1, s2 in segs1:
                parts = [(s1, s2)]
                for t1, t2 in segs2:
                    new_parts = []
                    for x1, x2 in parts:
                        left = max(x1, t1)
                        right = min(x2, t2)
                        if left < right:
                            if x1 < left:
                                new_parts.append((x1, left))
                            if right < x2:
                                new_parts.append((right, x2))
                        else:
                            new_parts.append((x1, x2))
                    parts = new_parts
                for x1, x2 in parts:
                    hatch.add(Line(
                        base + (x1 + eps)*direction,
                        base + (x2 - eps)*direction,
                        stroke_color="#FF7FAA",
                        stroke_width=4
                    ))

            for t1, t2 in segs2:
                parts = [(t1, t2)]
                for s1, s2 in segs1:
                    new_parts = []
                    for x1, x2 in parts:
                        left = max(x1, s1)
                        right = min(x2, s2)
                        if left < right:
                            if x1 < left:
                                new_parts.append((x1, left))
                            if right < x2:
                                new_parts.append((right, x2))
                        else:
                            new_parts.append((x1, x2))
                    parts = new_parts
                for x1, x2 in parts:
                    hatch.add(Line(
                        base + (x1 + eps)*direction,
                        base + (x2 - eps)*direction,
                        stroke_color="#70BAE9",
                        stroke_width=4
                    ))

        label1 = Text("S", color=BLACK, font_size=40).move_to(circle_1).shift(UP*2.7)
        label2 = Text("C", color=BLACK, font_size=40).move_to(circle_2).shift(UP*2.7)
        label3 = MathTex(r"S \cap \overline{C}", color=BLACK).scale(1.4).move_to(circle_1.get_center() + LEFT * 0.9).set_z_index(3)
        label4 = MathTex(r"\overline{S} \cap C", color=BLACK).scale(1.4).move_to(circle_2.get_center() + RIGHT * 0.9).set_z_index(3)

        start_s = circle_1.get_top() + LEFT*0.2
        end_s = rectangle.get_top() + UP * 1 + LEFT * 2.5
        start_c = circle_2.get_top() + RIGHT*0.2
        end_c = rectangle.get_top() + UP * 1 + RIGHT * 2.5
        arrow_1 = CurvedArrow(start_s, end_s, color="#DF6625", angle=-TAU/12, tip_length=0.2)
        arrow_2 = CurvedArrow(start_c, end_c, color="#DF6625", angle=TAU/12, tip_length=0.2)

        label5 = Text("Only S", color=BLACK, font_size=38).next_to(arrow_1.get_end(), LEFT).shift(UP*0.3+RIGHT*0.6)
        label6 = Text("Only C", color=BLACK, font_size=38).next_to(arrow_2.get_end(), RIGHT).shift(UP*0.3+LEFT*0.6)
        label7 = Text("Only one of the two jobs", color=BLACK, font_size=30).next_to(rectangle, DOWN)

        outline1 = circle_1.copy().set_fill(opacity=0)
        outline2 = circle_2.copy().set_fill(opacity=0)

        self.add(rectangle,hatch,intersection,outline1, outline2,circle_1, circle_2,s_label,label1, label2,label3, label4,
                 arrow_1, arrow_2,label5, label6,label7)