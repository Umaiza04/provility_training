from manim import *

config.frame_height = 10
config.frame_width = 20
config.pixel_width = 2500
config.pixel_height = 2500

class Step_3(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[-3.5, 5, 1],
            y_range=[-4.5, 18, 1],
            x_length=10,
            y_length=15,
            axis_config={"include_numbers": True,"font_size":28,"color":BLACK,"tip_length":0.35,"tip_width":0.25},
            y_axis_config={"numbers_to_include": [-3,-2, -1, 1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16],
                           "decimal_number_config": {
                           "num_decimal_places": 0,
                           "color": BLACK, }, },
            x_axis_config={"numbers_to_include": [-3,-2, -1, 1, 2, 3,4],
                           "decimal_number_config": {
                           "num_decimal_places": 0,
                           "color": BLACK, }, },
            tips=True)
        axes.y_axis.get_tick_marks()[2].shift(DOWN*0.17)
        axes.y_axis.get_tick_marks()[3].shift(DOWN*0.1)
        axes.y_axis.get_tick_marks()[0].set_opacity(0)
        axes.y_axis.get_tick_marks()[20].set_opacity(0)
        axes.x_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        axes.y_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        axes.y_axis.shift(RIGHT*0.2)
        axes.x_axis.shift(UP*0.2)

        x_label = MathTex("x", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT, buff=0.2)
        y_label = MathTex("y", color=BLACK).next_to(axes.y_axis.get_end(), UP, buff=0.2)
        y_label1 = axes.get_x_axis_label(MathTex("y'", color=BLACK)).next_to(axes.y_axis.get_start(), UP, buff=0.2).shift(DOWN*0.8)
        x_label1 = axes.get_y_axis_label(MathTex("x'", color=BLACK)).next_to(axes.x_axis.get_start(), RIGHT, buff=0.2).shift(LEFT*0.8)
        points_coords = [(-2,-2), (-1,-1), (0.1,0.1), (1.02,1), (2.07,4), (3.08,9),(4.07,15.8)]
        dots = VGroup()
        for coord in points_coords:
            dot = Dot(axes.c2p(*coord), color="#CF0234", radius=0.08).shift(UL*0.13)
            circle = Circle(radius=0.15, color=BLACK, stroke_width=3).move_to(dot.get_center())
            dots.add(dot, circle)
        labels = VGroup(
            MathTex("(-2,-2)", color=BLACK).scale(0.6).next_to(axes.c2p(-2.05,-2.1), UL),
            MathTex("(-1,-1)", color=BLACK).scale(0.6).next_to(axes.c2p(-1.1,-1.3), UL),
            MathTex("(0,0)", color=BLACK).scale(0.6).next_to(axes.c2p(0,0), UP*1.5),
            MathTex("(1,1)", color=BLACK).scale(0.6).next_to(axes.c2p(1,0.8),UR),
            MathTex("(2,4)", color=BLACK).scale(0.6).next_to(axes.c2p(2,4.1), RIGHT),
            MathTex("(3,9)", color=BLACK).scale(0.6).next_to(axes.c2p(3,8.5), UR),
            MathTex("(4,16)", color=BLACK).scale(0.6).next_to(axes.c2p(4,15.5), UR),
           )
        line = axes.plot(
            lambda x: x,
            x_range=[-3, 0],
            color="#030AA7"
        ).shift(UP*0.2).set_z_index(-1)
        end_point = line.get_start()
        micro_tip = ArrowTriangleFilledTip(length=0.25, width=0.25, color="#030AA7")
        micro_tip.move_to(end_point).rotate(PI/5.25)
        line.add(micro_tip)

        parabola = axes.plot(
            lambda x: x**2,
            x_range=[0, 4.1],
            color="#176A25"
        ).shift(UP*0.22).set_z_index(-1)
        end_point = parabola.get_end()
        micro_tip = ArrowTriangleFilledTip(length=0.25, width=0.25, color="#176A25")
        micro_tip.move_to(end_point).rotate(-PI/1.75)
        parabola.add(micro_tip)
        label_left = MathTex(r"x \le 1", color=BLACK).scale(0.8).next_to(axes.c2p(-0.5, 1), LEFT)
        label_right = MathTex(r"x > 1", color=BLACK).scale(0.8).next_to(axes.c2p(2.5, 6), RIGHT)
        arrow_left = Arrow(
             start=axes.c2p(-0.5, -0.5),
             end=axes.c2p(0.85, -0.5),color="#A87900",stroke_width=3,max_tip_length_to_length_ratio=0.15).shift(RIGHT*0.4)
        arrow_right = Arrow(
            start=axes.c2p(2.5, -0.5),
            end=axes.c2p(1.14, -0.5),color="#A87900",stroke_width=3,max_tip_length_to_length_ratio=0.15).shift(LEFT*0.4)
        label1 = MathTex("1^-",color=BLACK,font_size=30).move_to(axes.c2p(-0.6, -0.8)).shift(RIGHT*1.3+DOWN*0.03)
        label2 = MathTex("1^+", color=BLACK,font_size=30).move_to(axes.c2p(0.75, -0.8)).shift(RIGHT*1)

        self.add(axes, x_label,y_label,dots,  y_label1, x_label1,labels,line,parabola,label_left,label_right,
                 arrow_left,arrow_right,label1,label2)