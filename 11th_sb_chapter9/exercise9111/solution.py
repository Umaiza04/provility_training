from manim import*
config.frame_height=10
config.frame_width=12
config.pixel_width=2800
config.pixel_height=2800

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[-5.5, 7, 1],
            y_range=[-6, 6, 1],
            x_length=10,
            y_length=8,
            axis_config={"color": BLACK,
                         "include_tip": True,
                         "tip_length": 0.35,
                         "tip_width": 0.25,
                         "stroke_width": 3,},
            x_axis_config={"numbers_to_include": [-4,-3,-2, -1, 1, 2, 3, 4, 5],
                           "decimal_number_config": {
                           "num_decimal_places": 0,
                           "color": BLACK, }, },
            y_axis_config={"numbers_to_include": [-3, -2, -1, 1, 2, 3],
                           "decimal_number_config": {
                           "num_decimal_places": 0,
                           "color": BLACK, },  }, )
        axes.y_axis.shift(DOWN*0.2+RIGHT*0.2)
        
        axes.x_axis.get_tick_marks()[10].set_opacity(0)
        axes.x_axis.get_tick_marks()[0].set_opacity(0)
        axes.x_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        axes.y_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)

        axes.y_axis.get_tick_marks()[0].set_opacity(0)
        axes.y_axis.get_tick_marks()[1].set_opacity(0)
        axes.y_axis.get_tick_marks()[2].set_opacity(0)
        axes.y_axis.get_tick_marks()[9].set_opacity(0)
        axes.y_axis.get_tick_marks()[10].set_opacity(0)

        for num in axes.y_axis.numbers:
            if num.get_value() < 0:
                num.next_to( axes.y_axis.number_to_point(num.get_value()), RIGHT, buff=0.12  )

        x_label = axes.get_x_axis_label(MathTex("x", color=BLACK)).shift(DOWN*0.4)
        y_label = axes.get_y_axis_label(MathTex("y", color=BLACK)).shift(UP*0.25+LEFT*0.7)
        x_label1 = axes.get_x_axis_label(MathTex("x'", color=BLACK)).shift(DOWN*4.8+LEFT*5.6)
        y_label1 = axes.get_y_axis_label(MathTex("y'", color=BLACK)).shift(DOWN*4.0+LEFT*5.6)

        # Arrow for 3- (approaching from left)
        three_minus_arrow = Arrow(axes.c2p(-3, 0.5), axes.c2p(2.5, 0.5), color="#A87900", stroke_width=3, tip_length=0.15).shift(UP*0.2)
        three_minus_text = MathTex("3^-", color=BLACK, font_size=34).next_to(three_minus_arrow, UP, buff=0.1).shift(RIGHT*1.3)

        # Arrow for 3+ (approaching from right)
        three_plus_arrow = Arrow(axes.c2p(5.5, 0.5), axes.c2p(3.5, 0.5), color="#A87900", stroke_width=3, tip_length=0.15).shift(UP*0.7)
        three_plus_text = MathTex("3^+", color=BLACK, font_size=34).next_to(three_plus_arrow, UP, buff=0.1)

        # Circle around the '3' on the x-axis (as seen in the drawing)
        three_circle = Circle(radius=0.2, color=BLACK, stroke_width=3).move_to(axes.c2p(3, 0)).shift(DOWN*0.15+LEFT*0.08)

        f = lambda x: 1/(x-3)
        y_top = axes.y_range[1]
        y_bottom = axes.y_range[0]
        x_right_limit = 3 + 1/y_top
        x_left_limit = 3+ 1/y_bottom
        left_curve = axes.plot(f,x_range=[-4.5, x_left_limit],color="#1F2A7C",stroke_width=4,use_smoothing=False).shift(DOWN*0.02+LEFT*0.05)
        end_point = left_curve.get_start()
        micro_tip = ArrowTriangleFilledTip(length=0.15, width=0.15, color="#1F2A7C")
        micro_tip.move_to(end_point)
        left_curve.add(micro_tip)
        right_curve = axes.plot( f, x_range=[x_right_limit, 6], color="#1F2A7C", stroke_width=4, use_smoothing=False).shift(UP*0.06+LEFT*0.08)
        end_point = right_curve.get_end()
        micro_tip = ArrowTriangleFilledTip(length=0.15, width=0.13, color="#1F2A7C")
        micro_tip.move_to(end_point).rotate(PI/1)
        right_curve.add(micro_tip)
        top_dot = Dot(axes.c2p(x_right_limit, y_top), color="#1F2A7C", radius=0.06).shift(LEFT*0.08+UP*0.03)
        bottom_dot = Dot(axes.c2p(x_left_limit, y_bottom), color="#1F2A7C", radius=0.06).shift(DOWN*0.02+LEFT*0.05)
        func_label_1 = MathTex("f(x) = \\frac{1}{x-3}", color=BLACK, font_size=30).move_to(axes.c2p(4.5, 2.5)).shift(UP*1)
        func_label_2 = MathTex("f(x) = \\frac{1}{x-3}", color=BLACK, font_size=30).move_to(axes.c2p(-2, -1.5)).shift(LEFT*0.5)
        up_arrow = Arrow(axes.c2p(3.3, 4.5), axes.c2p(3.3, 5.5), color=BLACK, buff=0, tip_length=0.2).shift(RIGHT*0.2+UP*0.4)
        up_text = MathTex("100", color=BLACK, font_size=28).next_to(up_arrow, RIGHT, buff=0.1)
        
        down_arrow = Arrow(axes.c2p(2.7, -4.5), axes.c2p(2.7, -5.5), color=BLACK, buff=0, tip_length=0.2).shift(LEFT*0.2+DOWN*0.4)
        down_text = MathTex("-100", color=BLACK, font_size=28).next_to(down_arrow, LEFT, buff=0.1)


        line = Line(
            axes.c2p(3, -6),
            axes.c2p(3, 6),
            color="#BB3F3F",
            stroke_width=3,).set_z_index(-3).shift(LEFT*0.086)
        asymptote_text = Text("At x = 3", color=BLACK, font_size=25).rotate(90*DEGREES)
        asymptote_text.next_to(line, LEFT, buff=0.1).shift(UP*2)
        line2 = Line(start=axes.c2p(-1, -1),end=axes.c2p(1, -1), color="#B96902", stroke_width=4)
        dot_top = Dot(line2.get_start(), color="#6832E3", radius=0.05)
        dot_bottom = Dot(line2.get_end(), color="#6832E3", radius=0.05)

        self.add( axes, x_label, y_label, left_curve, right_curve,line,func_label_1,func_label_2,up_arrow,down_arrow,up_text,down_text,
                 three_minus_arrow,three_minus_text,three_plus_arrow,three_plus_text,three_circle,top_dot, asymptote_text,bottom_dot,line2,dot_top,dot_bottom,
                 x_label1,y_label1)
