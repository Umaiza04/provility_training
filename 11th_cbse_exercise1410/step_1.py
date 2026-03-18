from manim import *
import numpy as np

config.frame_height = 10
config.frame_width = 40
config.pixel_width = 3000
config.pixel_height = 3000


class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        r = 2.4
        spacing = 0.5
        angle = PI/4.2

        direction = np.array([np.cos(angle), np.sin(angle), 0])
        normal = np.array([-direction[1], direction[0], 0])

        def venn_diagram(center_shift, mode):
            rectangle = Rectangle(
                width=10, height=7,
                stroke_color="#990F4B",
                fill_color="#ACE6EB",
                fill_opacity=0.5,
                stroke_width=4).move_to(center_shift)
            u_label = Text("U", color=BLACK, font_size=28).next_to(rectangle, UR, buff=0.1).shift(DL*0.8).scale(2)

            c1 = np.array([-1.3, 0, 0]) + center_shift
            c2 = np.array([1.3, 0, 0]) + center_shift
            circle_1 = Circle(radius=r, stroke_color="#770D75", stroke_width=4).move_to(c1)
            circle_2 = Circle(radius=r, stroke_color="#770D75", stroke_width=4).move_to(c2)

            hatch = VGroup()
            for t in np.arange(-6, 6, spacing):
                base = t * normal
                eps = 0.01

                diff1 = base + center_shift - c1
                a = np.dot(direction, direction)
                b1 = 2 * np.dot(diff1, direction)
                c_1 = np.dot(diff1, diff1) - r**2
                disc1 = b1*b1 - 4*a*c_1

                diff2 = base + center_shift - c2
                b2 = 2 * np.dot(diff2, direction)
                c_2 = np.dot(diff2, diff2) - r**2
                disc2 = b2*b2 - 4*a*c_2

                if mode == "left":
                    if disc1 >= 0:
                        s1 = (-b1 - np.sqrt(disc1)) / (2*a)
                        s2 = (-b1 + np.sqrt(disc1)) / (2*a)
                        parts = [(s1, s2)]
                        if disc2 >= 0:
                            t1 = (-b2 - np.sqrt(disc2)) / (2*a)
                            t2 = (-b2 + np.sqrt(disc2)) / (2*a)
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
                                base + (x1 + eps)*direction + center_shift,
                                base + (x2 - eps)*direction + center_shift,
                                stroke_color="#EC1170",
                                stroke_width=3.2))

                elif mode == "right":
                    if disc2 >= 0:
                        t1 = (-b2 - np.sqrt(disc2)) / (2*a)
                        t2 = (-b2 + np.sqrt(disc2)) / (2*a)
                        parts = [(t1, t2)]
                        if disc1 >= 0:
                            s1 = (-b1 - np.sqrt(disc1)) / (2*a)
                            s2 = (-b1 + np.sqrt(disc1)) / (2*a)
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
                                base + (x1 + eps)*direction + center_shift,
                                base + (x2 - eps)*direction + center_shift,
                                stroke_color="#EC1874",
                                stroke_width=3.2 ))

                elif mode == "intersection":
                    if disc1 >= 0 and disc2 >= 0:
                        s1 = (-b1 - np.sqrt(disc1)) / (2*a)
                        s2 = (-b1 + np.sqrt(disc1)) / (2*a)
                        t1 = (-b2 - np.sqrt(disc2)) / (2*a)
                        t2 = (-b2 + np.sqrt(disc2)) / (2*a)
                        left = max(s1, t1)
                        right = min(s2, t2)
                        if left < right:
                            hatch.add(Line(
                                base + (left + eps)*direction + center_shift,
                                base + (right - eps)*direction + center_shift,
                                stroke_color="#EC1874",
                                stroke_width=2.2 ))

            label1 = Text("X", color=BLACK, font_size=24).move_to(c1).shift(UP*2.9).scale(2)
            label2 = Text("Y", color=BLACK, font_size=24).move_to(c2).shift(UP*2.9).scale(2)
            a = MathTex("a", color=BLACK).scale(2).move_to(c1 + LEFT*0.8 + UP*0.7)
            c = MathTex("c", color=BLACK).scale(2).move_to(c1 + LEFT*0.8 + DOWN*0.7)
            b = MathTex("b", color=BLACK).scale(2).move_to(center_shift + UP*0.7)
            d = MathTex("d", color=BLACK).scale(2).move_to(center_shift + DOWN*0.7)
            f = MathTex("f", color=BLACK).scale(2).move_to(c2 + RIGHT*0.8 + UP*0.7)
            g = MathTex("g", color=BLACK).scale(2).move_to(c2 + RIGHT*0.8 + DOWN*0.7)

            return VGroup(rectangle, u_label, hatch, circle_1, circle_2, label1, label2,a, b, c, d, f, g)

        left_venn = venn_diagram(LEFT * 12, "left")
        mid_venn = venn_diagram(ORIGIN, "intersection")
        right_venn = venn_diagram(RIGHT * 12, "right")

        t1 = Text("X - Y", color=BLACK).scale(1.2).next_to(left_venn, DOWN)
        t2 = Text("X ∩ Y", color=BLACK).scale(1.2).next_to(mid_venn, DOWN)
        t3 = Text("Y - X", color=BLACK).scale(1.2).next_to(right_venn, DOWN)

        self.add(left_venn, mid_venn, right_venn, t1, t2, t3)