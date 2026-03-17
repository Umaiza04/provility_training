from manim import *

config.frame_height = 6
config.frame_width = 10
config.pixel_width = 2500
config.pixel_height = 2500

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[-2.5, 6, 1],
            y_range=[-2.5, 3, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_numbers": True,"font_size":28,"color":BLACK,"tip_length":0.35,"tip_width":0.25},
            x_axis_config={"numbers_to_include": [-2, -1, 1, 2, 3, 4, 5],
                           "decimal_number_config": {
                           "num_decimal_places": 0,
                           "color": BLACK, }, },
            tips=True)
        axes.x_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        axes.y_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        axes.y_axis.get_tick_marks()[0].set_opacity(0)
        axes.y_axis.get_tick_marks()[1].set_opacity(0)
        axes.y_axis.get_tick_marks()[2].set_opacity(0)
        axes.y_axis.get_tick_marks()[3].set_opacity(0)
        axes.y_axis.shift(RIGHT*0.2)
        origin_label = Tex("0",color=BLACK,font_size=30).scale(0.8).next_to(axes.c2p(0, 0), LEFT, buff=0.15).shift(RIGHT*0.1+DOWN*0.15)

        x_label = MathTex("x", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT, buff=0.2)
        y_label = MathTex("y", color=BLACK).next_to(axes.y_axis.get_end(), UP, buff=0.2)
        y_label1 = axes.get_x_axis_label(MathTex("y'", color=BLACK)).next_to(axes.y_axis.get_start(), UP, buff=0.2).shift(DOWN*0.8)
        x_label1 = axes.get_y_axis_label(MathTex("x'", color=BLACK)).next_to(axes.x_axis.get_start(), RIGHT, buff=0.2).shift(LEFT*0.8)

        left_line = axes.plot(lambda x: -x + 1,x_range=[-1.7, 1],color="#9D0216",stroke_width=3).set_z_index(-1)
        end_point = left_line.get_start()
        micro_tip = ArrowTriangleFilledTip(length=0.25, width=0.25, color="#1F2A7C")
        micro_tip.move_to(end_point).rotate(-PI/3.5)
        left_line.add(micro_tip)
        right_line = axes.plot( lambda x: x - 1, x_range=[1, 4],color="#9D0216",stroke_width=3).set_z_index(-1)
        end_point = right_line.get_end()
        micro_tip = ArrowTriangleFilledTip(length=0.25, width=0.25, color="#1F2A7C")
        micro_tip.move_to(end_point).rotate(-PI/1.4)
        right_line.add(micro_tip)
        label = MathTex(r"f(x)=|x-1|",font_size=30, color=BLACK).rotate(PI/3.7).shift(UP*4+DOWN*3+RIGHT*1)
        arrow_left = Arrow(
             start=axes.c2p(-1.65, -0.5),
             end=axes.c2p(0.7, -0.5),color="#A87900",stroke_width=3,max_tip_length_to_length_ratio=0.15).shift(RIGHT*0.4)
        arrow_right = Arrow(
            start=axes.c2p(3.5, -0.5),
            end=axes.c2p(1.3, -0.5),color="#A87900",stroke_width=3,max_tip_length_to_length_ratio=0.15).shift(LEFT*0.4)
        label1 = MathTex("1^-",color=BLACK,font_size=30).move_to(axes.c2p(-1.1, -0.7)).shift(RIGHT*1.3+DOWN*0.03)
        label2 = MathTex("1^+", color=BLACK,font_size=30).move_to(axes.c2p(1.1, -0.7)).shift(RIGHT*1)

        self.add(axes, x_label,y_label, left_line, right_line, y_label1, x_label1,label,arrow_left,arrow_right,origin_label,
                 label1,label2)