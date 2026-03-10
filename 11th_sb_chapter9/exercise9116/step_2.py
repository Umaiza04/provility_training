from manim import*
config.frame_height=10
config.frame_width=15
config.pixel_width=2500
config.pixel_height=2500

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[-4.5, 8, 1],
            y_range=[-4.5, 10, 1],
            x_length=13,
            y_length=13,
            axis_config={"include_tip": True, "color": BLACK, "stroke_width": 2,"include_numbers":True,"tip_length": 0.35,
                          "tip_width": 0.25,"stroke_width":3},
        ).add_coordinates(color=BLACK)
        axes.y_axis.shift(RIGHT*0.11)
        axes.x_axis.shift(UP*0.13)
        axes.x_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        axes.y_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        x_label = MathTex("x", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT).scale(1)
        y_label = MathTex("y", color=BLACK).next_to(axes.y_axis.get_end(), UP).scale(1)
        x_label1= MathTex("x'", color=BLACK).next_to(axes.x_axis.get_start(), LEFT).scale(1)
        y_label1 = MathTex("y'", color=BLACK).next_to(axes.y_axis.get_start(), DOWN).scale(1)

        #parabola
        parabola = axes.plot(
            lambda x: x**2, 
            x_range=[-3, 2], 
            color="#CF0234" 
        ).shift(UP*0.13)
        parabola_label = MathTex("f(x)=x^2", color=BLACK).scale(0.8).next_to(axes.c2p(-2.5, 6.25), LEFT).rotate(PI/1.8).shift(RIGHT*0.6)

        #line
        line = axes.plot(
            lambda x: 8 - 2*x, 
            x_range=[2, 4], 
            color="#5F8112"
        ).shift(UP*0.13)
        line_label = MathTex("f(x)=8-2x", color=BLACK).scale(0.8).next_to(axes.c2p(3, 2), UR, buff=0.1).shift(UP*1+LEFT*0.5)
        circle1 = Circle(radius=0.2, color="#AC4F06", stroke_width=3).move_to(axes.c2p(2, 0)).shift(DOWN*0.25+RIGHT*0.06)
        circle2 = Circle(radius=0.2, color="#AC4F06", stroke_width=3).move_to(axes.c2p(4, 0)).shift(DOWN*0.25+RIGHT*0.02)

        #arrows creation
        arrow1 = Arrow(start=axes.coords_to_point(1.2, -0.6),
                      end=axes.coords_to_point(2, -0.6),
                      buff=0,
                      stroke_width=6,
                      color=BLUE,
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.25)
        
        arrow2 = Arrow(start=axes.coords_to_point(2.1, -0.6),
                      end=axes.coords_to_point(2.8, -0.6),
                      buff=0,
                      stroke_width=6,
                      color=BLUE,
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.3).rotate(PI/-1)
        
        arrow3 = Arrow(start=axes.coords_to_point(3.3, -0.6),
                      end=axes.coords_to_point(4.0, -0.6),
                      buff=0,
                      stroke_width=6,
                      color=BLUE,
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.3)
        
        arrow4 = Arrow(start=axes.coords_to_point(4.1, -0.6),
                      end=axes.coords_to_point(4.8, -0.6),
                      buff=0,
                      stroke_width=6,
                      color=BLUE,
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.3).rotate(PI/-1)
        
        limit_left = MathTex("2^-", color=BLACK).scale(0.6).next_to(arrow1, DOWN, buff=0.1).shift(DOWN*0.04)
        limit_right = MathTex("2^+", color=BLACK).scale(0.6).next_to(arrow2, DOWN, buff=0.1)
        limit_left1 = MathTex("4^-", color=BLACK).scale(0.6).next_to(arrow3, DOWN, buff=0.1).shift(DOWN*0.04)
        limit_right1 = MathTex("4^+", color=BLACK).scale(0.6).next_to(arrow4, DOWN, buff=0.1)

        points_coords = [(-3, 9), (-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4), (3, 2), (4, 0),(4,4)]
        dots = VGroup()
        for coord in points_coords:
            dot = Dot(axes.c2p(*coord), color="#CF0234", radius=0.08).shift(UP*0.13)
            circle = Circle(radius=0.15, color=BLACK, stroke_width=3).move_to(dot.get_center())
            dots.add(dot, circle)
        labels = VGroup(
            MathTex("(-3,9)", color=BLACK).scale(0.6).next_to(axes.c2p(-3, 9), LEFT),
            MathTex("(-2,4)", color=BLACK).scale(0.6).next_to(axes.c2p(-2, 4), LEFT),
            MathTex("(-1,1)", color=BLACK).scale(0.6).next_to(axes.c2p(-1, 1), LEFT),
            MathTex("(0,0)", color=BLACK).scale(0.6).next_to(axes.c2p(-0, 0),UP),
            MathTex("(3,2)", color=BLACK).scale(0.6).next_to(axes.c2p(3, 2), RIGHT),
            MathTex("(2,4)", color=BLACK).scale(0.6).next_to(axes.c2p(2, 4), UR),
            MathTex("(4,0)", color=BLACK).scale(0.6).next_to(axes.c2p(4, 0), UR),
            MathTex("(4,4)", color=BLACK).scale(0.6).next_to(axes.c2p(4, 4), UR),
           )
        
        #function
        function = axes.plot(
            lambda x: 4, 
            x_range=[0, 7],
            color="#1F2A7C").shift(UP*0.145).set_z_index(-1)
        end_point = function.get_end()
        micro_tip = ArrowTriangleFilledTip(length=0.35, width=0.25, color="#1F2A7C")
        micro_tip.move_to(end_point).rotate(PI/1)
        function.add(micro_tip)
        func_label = MathTex("f(x)=4", color=BLACK).scale(0.8).next_to(axes.c2p(0, 4), DOWN, buff=0.2).shift(UR*1)

        self.add(axes, parabola, line, dots, parabola_label, line_label, labels,circle1,circle2,
        arrow1,arrow2,arrow3,arrow4,limit_left ,limit_right,limit_left1 ,limit_right1,function,func_label,
        x_label,y_label,x_label1,y_label1)