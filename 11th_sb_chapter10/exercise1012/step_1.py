from manim import *

config.frame_height = 6
config.frame_width = 10
config.pixel_width = 2500
config.pixel_height = 2500

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[-3, 4, 1],
            y_range=[-2, 3, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_numbers": True,"font_size":28,"color":BLACK,"tip_length":0.35,"tip_width":0.25},
            tips=True)
        axes.add_coordinates().set_color(BLACK)

        x_label = MathTex("x").next_to(axes.x_axis.get_end(), RIGHT).set_color(BLACK)
        y_label = MathTex("f(x)").next_to(axes.y_axis.get_end(), UP).set_color(BLACK)

        left_line = axes.plot(lambda x: -x + 1,x_range=[-2, 1],color="#7E4071",stroke_width=3)
        right_line = axes.plot( lambda x: x - 1, x_range=[1, 3],color="#7E4071",stroke_width=3)

        self.add(axes, x_label,y_label, left_line, right_line)