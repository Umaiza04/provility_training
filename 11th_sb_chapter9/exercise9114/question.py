from manim import *
import numpy as np
config.frame_height=15
config.frame_width=13
config.pixel_width=2800
config.pixel_height=2800

class SecGraph(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
    x_range=[-np.pi - 0.6, np.pi + 0.6, np.pi/2],  
    y_range=[-2, 6, 1],
    x_length=10,
    y_length=8,
    axis_config={
        "color": "#0B7A2F",
        "include_tip": True,
         "tip_length": 0.35,
         "tip_width": 0.25,
        "stroke_width": 8,},)

        x_labels = axes.get_x_axis().add_labels({
            -np.pi: MathTex("-\\pi", color=BLACK),
            -np.pi/2: MathTex("-\\frac{\\pi}{2}", color=BLACK),
            np.pi/2: MathTex("\\frac{\\pi}{2}", color=BLACK),
            np.pi: MathTex("\\pi", color=BLACK), })

        y_labels = axes.get_y_axis().add_labels({
            -1: MathTex("-1", color=BLACK),
            1: MathTex("1", color=BLACK),
            2: MathTex("2", color=BLACK),
            3: MathTex("3", color=BLACK),
            4: MathTex("4", color=BLACK),
            5: MathTex("5", color=BLACK) })
        x_label = Text("x", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT, buff=0.2)
        y_label = Text("y", color=BLACK).next_to(axes.y_axis.get_end(), UP, buff=0.2)

        sec_middle= axes.plot(lambda x: 1 / np.cos(x),x_range=[-PI/2 + 0.168, PI/2 - 0.168],color="#040273",stroke_width=6)
        sec_left= axes.plot(lambda x: 1 / np.cos(x),x_range=[-PI + 0.00009, -PI/2 - 0.53],color="#040273",stroke_width=6)
        sec_right= axes.plot(lambda x: 1 / np.cos(x),x_range=[PI/2 + 0.53, PI - 0.009],color="#040273",stroke_width=6)

        dashline1 = DashedLine(
            axes.c2p(-np.pi/2, -2),
            axes.c2p(-np.pi/2, 6),
            color="#8B2E2E",dash_length=0.1, stroke_width=5 )

        dashline2 = DashedLine(
            axes.c2p(np.pi/2, -2),
            axes.c2p(np.pi/2, 6),
            color="#8B2E2E",
            dash_length=0.1, stroke_width=5, )

        self.add( axes, x_labels, y_labels,x_label,y_label, dashline1, dashline2, sec_left, sec_middle, sec_right   )
