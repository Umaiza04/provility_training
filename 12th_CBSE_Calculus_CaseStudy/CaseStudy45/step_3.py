from manim import *
import numpy as np
config.frame_height=15
config.frame_width=13
config.pixel_width=2800
config.pixel_height=2800

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
    
        axis = Line(LEFT*5, RIGHT*5, color=BLACK)
        axis.add_tip()
        axis.add_tip(at_start=True)

        tick = Line(UP*0.25, DOWN*0.25, color=BLACK).move_to(ORIGIN)
        label1 = MathTex(r"\frac{a}{\sqrt{2}}", color=BLACK).next_to(tick, DOWN)
        label2 = MathTex("A'(x)", color=BLACK).next_to(axis.get_end(), RIGHT)
        label3 = MathTex("+", color=BLACK).move_to(LEFT*2 + UP*0.6)
        label4 = MathTex("-", color=BLACK).move_to(RIGHT*2 + DOWN*0.6)

        left_curve = CubicBezier(
            LEFT*4 + UP*1.2,
            LEFT*2.5 + UP*2.1,
            LEFT*1 + UP*1.1,
            ORIGIN)

        right_curve = CubicBezier(
            ORIGIN,
            RIGHT*1 + DOWN*1.2,
            RIGHT*2.5 + DOWN*2.1,
            RIGHT*4.3 + DOWN*1.1).shift(UL*0.01)

        curve = VGroup(left_curve, right_curve).set_color("#F7022A").set_stroke(width=5)

        label5 = MathTex(r"+\ to\ - \Rightarrow \text{local max}", color=BLACK)
        box = SurroundingRectangle(label5, color="#05696B",corner_radius=0.2,buff=0.2)
        text_group = VGroup(label5, box).move_to(DOWN*3+LEFT*1)
        arrow = Arrow(start=text_group.get_top() + DOWN*0.1,end=label1.get_bottom(),buff=0,
                      stroke_width=3,max_tip_length_to_length_ratio=0.08,color="#CA6B02").shift(UP*0.1+LEFT*0.35).set_z_index(-1)
        self.add(axis,tick,label1,label2,label3,label4,curve,text_group,arrow)