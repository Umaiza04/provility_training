from manim import *
import numpy as np
config.frame_height=15
config.frame_width=13
config.pixel_width=2800
config.pixel_height=2800

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
    x_range=[-np.pi - 0.6, np.pi + 0.9, np.pi/2],  
    y_range=[-3.5, 6, 1],
    x_length=10,
    y_length=10,
    axis_config={
        "color": BLACK,
        "include_tip": True,
         "tip_length": 0.35,
         "tip_width": 0.25,
        "stroke_width": 4,},)

        x_labels = axes.get_x_axis().add_labels({
            -np.pi: MathTex("-\\pi", color=BLACK),
            -np.pi/2: MathTex("-\\frac{\\pi}{2}", color=BLACK),
            np.pi/2: MathTex("\\frac{\\pi}{2}", color=BLACK),
            np.pi: MathTex("\\pi", color=BLACK), })

        y_labels = axes.get_y_axis().add_labels({
            -1: MathTex("-1", color=BLACK),
            -2: MathTex("-2", color=BLACK),
            1: MathTex("1", color=BLACK),
            2: MathTex("2", color=BLACK),
            3: MathTex("3", color=BLACK),
            4: MathTex("4", color=BLACK),
            5: MathTex("5", color=BLACK) })
        x_label = MathTex("x", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT, buff=0.2)
        y_label = MathTex("y", color=BLACK).next_to(axes.y_axis.get_end(), UP, buff=0.2)
        y_label1 = axes.get_x_axis_label(MathTex("y'", color=BLACK)).shift(DOWN*4.4+LEFT*5.2)
        x_label1 = axes.get_y_axis_label(MathTex("x'", color=BLACK)).shift(DOWN*6.5+LEFT*5.6)
        origin_label = Tex("0",color=BLACK).scale(0.8).next_to(axes.c2p(0, 0), LEFT, buff=0.15).shift(RIGHT*0.14+DOWN*0.1)
        origin_circle = Circle(radius=0.2, color="#AC4F06").move_to(axes.c2p(0, 0)).shift(DOWN*0.1+LEFT*0.1)
        axes.y_axis.get_tick_marks()[0].set_opacity(0)
        axes.x_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        axes.y_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        axes.y_axis.shift(RIGHT*0.15)
        axes.x_axis.shift(UP*0.18)


        sec_middle= axes.plot(lambda x: 1 / np.cos(x),x_range=[-PI/2 + 0.173, PI/2 - 0.173],color="#040273",stroke_width=6).shift(UP*0.17)
        end_point = sec_middle.get_end()
        micro_tip = ArrowTriangleFilledTip(length=0.2, width=0.15, color="#1F2A7C")
        micro_tip.move_to(end_point).rotate(-PI/2)
        sec_middle.add(micro_tip)
        end_point = sec_middle.get_start()
        micro_tip = ArrowTriangleFilledTip(length=0.2, width=0.15, color="#1F2A7C")
        micro_tip.move_to(end_point).rotate(-PI/2.1)
        sec_middle.add(micro_tip)
        sec_left= axes.plot(lambda x: 1 / np.cos(x),x_range=[-PI - 0.45, -PI/2 - 0.4],color="#040273",stroke_width=6)
        sec_right= axes.plot(lambda x: 1 / np.cos(x),x_range=[PI/2 + 0.4, PI + 0.45],color="#040273",stroke_width=6)

        dashline1 = DashedLine(
            axes.c2p(-np.pi/2, -2.6),
            axes.c2p(-np.pi/2, 6),
            color="#9D0216",dash_length=0.1, stroke_width=4 ).shift(RIGHT*0.1)

        dashline2 = DashedLine(
            axes.c2p(np.pi/2, -2.6),
            axes.c2p(np.pi/2, 6),
            color="#9D0216",
            dash_length=0.1, stroke_width=4, ).shift(LEFT*0.05)
        dot = Dot(point=axes.c2p(0, 1), color="#CF0234", radius=0.08).shift(UP*0.16)
        func_label = MathTex(r"f(x) = sec",color=BLACK).next_to(axes.c2p(PI/2, 5.5), UP, buff=0).shift(RIGHT*1.5)
        zero_minus_tex = MathTex("0^-",color=BLACK).move_to(axes.c2p(-1.1, 0.7)).shift(RIGHT*0.5)
        zero_plus_tex = MathTex("0^+", color=BLACK).move_to(axes.c2p(1.1, 0.7)).shift(LEFT*0.5)
        arrow_left = Arrow(
             start=axes.c2p(-1.5, 0.4),
             end=axes.c2p(-0.2, 0.4),color="#A87900",stroke_width=3,).shift(RIGHT*0.4)
        arrow_right = Arrow(
            start=axes.c2p(1.5, 0.4),
            end=axes.c2p(0.2, 0.4),color="#A87900",stroke_width=3,).shift(LEFT*0.4)

        self.add( axes, x_labels, y_labels,x_label,y_label,x_label1,y_label1, dashline1, dashline2, sec_left, sec_middle, sec_right ,func_label 
                 ,zero_minus_tex,zero_plus_tex,arrow_left, arrow_right ,dot,origin_label,origin_circle)
