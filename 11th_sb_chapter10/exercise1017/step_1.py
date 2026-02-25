from manim import *
import numpy as np

config.frame_height = 10
config.frame_width = 14
config.pixel_width = 2500
config.pixel_height = 2500

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        x_min = -2*np.pi
        x_max =  2*np.pi
        axis_left  = -2.4*np.pi
        axis_right =  2.4*np.pi

        tick_positions = [ -2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
        tick_labels = [r"-2\pi", r"-\frac{3\pi}{2}", r"-\pi", r"-\frac{\pi}{2}",r"\frac{\pi}{2}", r"\pi", r"\frac{3\pi}{2}", r"2\pi"]

        def make_x_ticks(axes):
            ticks = VGroup()
            numbers = VGroup()
            for pos, label in zip(tick_positions, tick_labels):
                point = axes.c2p(pos, 0)
                tick = Line( point + 0.12*DOWN,point + 0.12*UP,stroke_width=2,color=BLACK)
                number = MathTex(label, color=BLACK).scale(0.7)
                number.next_to(point, DOWN, buff=0.15)
                ticks.add(tick)
                numbers.add(number)
            return VGroup(ticks, numbers)

        #sin x graph
        axes1 = Axes(
            x_range=[axis_left, axis_right, np.pi/2],
            y_range=[-2.5, 3, 1],
            x_length=11,
            y_length=5,
            axis_config={"color":BLACK,"tip_length":0.35,"tip_width":0.25},
            tips=True,
            y_axis_config={"include_ticks": True,"include_numbers":True}, ).set_color(BLACK).shift(UP*2.5)
        
        sin_curve = axes1.plot(
            lambda x: np.sin(x),
            x_range=[x_min, x_max],
            color="#DE0C62",
            stroke_width=4)

        x_label1 = MathTex("x", color=BLACK).next_to(axes1.x_axis.get_end(), RIGHT)
        y_label1 = MathTex("y", color=BLACK).next_to(axes1.y_axis.get_end(), UP)
        label1 = MathTex(r"y=\sin x", color=BLACK).scale(0.9).next_to(axes1, UP, buff=0.3).shift(LEFT*4)
        sin_ticks = make_x_ticks(axes1)

        #|sin x| graph
        axes2 = Axes(
            x_range=[-7,7, np.pi/2],
            y_range=[-2.0, 2.2, 1],
            x_length=11,
            y_length=4,
            axis_config={"color":BLACK,"tip_length":0.35,"tip_width":0.25},
            tips=True,
            y_axis_config={"include_ticks": False},).set_color(BLACK).shift(DOWN*3)

        sin2_curve = axes2.plot(
            lambda x: np.abs(np.sin(x)),
            x_range=[x_min, x_max],
            color="#DE0C62",
            stroke_width=4,use_smoothing=False )

        x_label2 = MathTex("x", color=BLACK).next_to(axes2.x_axis.get_end(), RIGHT)
        y_label2 = MathTex("y", color=BLACK).next_to(axes2.y_axis.get_end(), UP)
        label2 = MathTex(r"y=|\sin x|", color=BLACK).scale(0.9).next_to(axes2, UP, buff=0.3).shift(LEFT*4)
        sin2_ticks = make_x_ticks(axes2)

        self.add(axes1, sin_curve, sin_ticks, x_label1, y_label1, label1,axes2, sin2_curve, sin2_ticks, x_label2, y_label2, label2)