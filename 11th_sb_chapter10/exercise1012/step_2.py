from manim import *

config.frame_height = 6
config.frame_width = 10
config.pixel_width = 2500
config.pixel_height = 2500

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[-3.5, 5, 1],
            y_range=[-2.5, 4, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_numbers": True,"font_size":28,"color":BLACK,"tip_length":0.35,"tip_width":0.25},
            tips=True)
        axes.add_coordinates().set_color(BLACK)
        axes.y_axis.get_tick_marks()[2].shift(DOWN*0.17)
        axes.y_axis.get_tick_marks()[3].shift(DOWN*0.1)
        axes.x_axis.get_tick_marks()[2].set_opacity(0)
        axes.x_axis.get_tick_marks()[3].set_opacity(0)
        axes.x_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        axes.y_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        axes.y_axis.shift(RIGHT*0.2)
        axes.x_axis.shift(UP*0.2)
        origin_label = Tex("0",color=BLACK,font_size=30).scale(0.8).next_to(axes.c2p(0, 0), LEFT, buff=0.15).shift(RIGHT*0.1+DOWN*0.15)

        x_label = MathTex("x", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT, buff=0.2)
        y_label = MathTex("y", color=BLACK).next_to(axes.y_axis.get_end(), UP, buff=0.2)
        y_label1 = axes.get_x_axis_label(MathTex("y'", color=BLACK)).next_to(axes.y_axis.get_start(), UP, buff=0.2).shift(DOWN*0.8)
        x_label1 = axes.get_y_axis_label(MathTex("x'", color=BLACK)).next_to(axes.x_axis.get_start(), RIGHT, buff=0.2).shift(LEFT*0.8)
        graph = axes.plot(
            lambda x: np.sqrt(1 - x**2),
            x_range=[-0.975, 0.975,0.01],
            color="#464196",stroke_width=3)
        left_dot = Dot(axes.c2p(-0.975, 0.22), color="#990F4B").scale(0.6)
        right_dot = Dot(axes.c2p(0.975, 0.22), color="#990F4B").scale(0.6)
        top_dot = Dot(axes.c2p(0, 1), color="#990F4B").scale(0.6)
        label = MathTex(r"f(x)=\sqrt{1-x^2}", color=BLACK).scale(0.7).shift(UP*0.7+RIGHT*1)

        arrow_left = Arrow(
             start=axes.c2p(-1.65, -0.4),
             end=axes.c2p(0.7, -0.4),color="#A87900",stroke_width=3,max_tip_length_to_length_ratio=0.15).shift(RIGHT*0.4)
        arrow_right = Arrow(
            start=axes.c2p(3.5, -0.4),
            end=axes.c2p(1.3, -0.4),color="#A87900",stroke_width=3,max_tip_length_to_length_ratio=0.15).shift(LEFT*0.4)
        label1 = MathTex("1^-",color=BLACK,font_size=28).move_to(axes.c2p(-1.1, -0.7)).shift(RIGHT*1.4+DOWN*0.04)
        label2 = MathTex("1^+", color=BLACK,font_size=28).move_to(axes.c2p(1.1, -0.7)).shift(RIGHT*0.5)

        self.add(axes, x_label,y_label,  y_label1, x_label1,arrow_left,arrow_right,origin_label,label,
                 label1,label2,graph, left_dot, right_dot, top_dot)
        
        #curve diagram
        line = NumberLine(
            x_range=[-2, 2, 1],
            length=4,
            color="#76424E",
            include_ticks=True,
            include_numbers=False,include_tip=True,stroke_width=2,tip_length=0.35,tip_width=0.25)
        line.get_tick_marks()[0].set_opacity(0)
        line.get_tick_marks()[1].shift(LEFT*0.3)
        line.get_tick_marks()[2].shift(LEFT*0.18)
        line.get_tick_marks()[3].shift(LEFT*0.1)
        line.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)

        minus1 = MathTex("-1", color=BLACK).scale(0.7).next_to(line.n2p(-1), DOWN)
        zero = MathTex("0", color=BLACK).scale(0.7).next_to(line.n2p(0), DOWN)
        plus1 = MathTex("1", color=BLACK).scale(0.7).next_to(line.n2p(1), DOWN)

        curve = ParametricFunction(
            lambda t: np.array([line.n2p(t)[0],np.cos(np.pi/2 * t),0]), t_range=[-2, 2], color="#A00498", stroke_width=2)
        
        text1 = Text("+ve", color=BLACK).scale(0.6).move_to([line.n2p(0)[0], 1.3, 0])
        text2 = Text("-ve", color=BLACK).scale(0.6).move_to([line.n2p(-1.9)[0], -0.6, 0])
        text3 = Text("-ve", color=BLACK).scale(0.6).move_to([line.n2p(1.9)[0], -0.6, 0])

        curve_diagram=VGroup(line,curve,minus1, zero, plus1,text1,text2,text3).scale(0.5).shift(DR*3)
        self.add(curve_diagram)