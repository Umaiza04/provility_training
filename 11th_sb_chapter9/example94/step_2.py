from manim import*
config.frame_height=10
config.frame_width=12
config.pixel_width=2800
config.pixel_height=2800

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[-4.5, 4.5, 1],
            y_range=[-4.5, 4.5, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": BLACK,
                          "include_tip": True,
                          "include_ticks":True,
                          "tip_length": 0.35,
                          "tip_width": 0.25,
                           "stroke_width":3}, )
        axes.move_to(ORIGIN)
        axes.add_coordinates(color=BLACK)
        axes.x_axis.add_tip(at_start=True)
        axes.y_axis.add_tip(at_start=True)
        axes.y_axis.shift(RIGHT*0.2)
        x_label = axes.get_x_axis_label(MathTex("x", color=BLACK)).shift(DOWN*0.35)
        y_label = axes.get_y_axis_label(MathTex("y", color=BLACK)).shift(UP*0.7+LEFT*0.4)
        y_label1 = axes.get_x_axis_label(MathTex("y'", color=BLACK)).shift(DOWN*5.8+LEFT*5.2)
        x_label1 = axes.get_y_axis_label(MathTex("x'", color=BLACK)).shift(DOWN*4.5+LEFT*5.8)

     
        line1 = axes.plot(lambda x: x - 1,
                          x_range=[-3.5, -1],
                          color="#26538D",
                          stroke_width=4).shift(UP*0.25+RIGHT*0.2)
        tip1 = Arrow(line1.point_from_proportion(0.2),line1.point_from_proportion(0.001),buff=0,color="#26538D",stroke_width=4).shift(DL*0.03)

        line2 = axes.plot(lambda x: x + 1,
                          x_range=[1, 3.5],
                          color="#A0025C",
                          stroke_width=4).shift(UP*0.12+RIGHT*0.13)
        tip2 = Arrow(line2.point_from_proportion(0.8),line2.point_from_proportion(0.99),buff=0,color="#A0025C",stroke_width=4).set_z_index(-1).shift(UR*0.06)
        def circled_dot(x, y):
            point = axes.c2p(x, y)
            circle = Circle(radius=0.13,color=BLACK,stroke_width=2).move_to(point)
            dot = Dot(point,radius=0.06,color="#6832E3")
            return VGroup(circle, dot)
        point1 = circled_dot(1, 2).shift(UP*0.12+RIGHT*0.13)
        point2 = circled_dot(2, 3).shift(UP*0.12+RIGHT*0.13)
        point3 = circled_dot(3,4).shift(UP*0.12+RIGHT*0.13)
        point4 = circled_dot(-1, -2).shift(UP*0.25+RIGHT*0.2)
        point5 = circled_dot(-2, -3).shift(UP*0.25+RIGHT*0.2)
        point6 = circled_dot(-3, -4) .shift(UP*0.25+RIGHT*0.2)
        label_dot1 = MathTex("(1,2)", color=BLACK).scale(0.7).next_to(point1, RIGHT)
        label_dot2 = MathTex("(2,3)", color=BLACK).scale(0.7).next_to(point2, RIGHT)
        label_dot3 = MathTex("(3,4)", color=BLACK).scale(0.7).next_to(point3, RIGHT)
        label_dot4 = MathTex("(-1,-2)", color=BLACK).scale(0.7).next_to(point4, LEFT)
        label_dot5 = MathTex("(-2,-3)", color=BLACK).scale(0.7).next_to(point5, LEFT)
        label_dot6 = MathTex("(-3,-4)", color=BLACK).scale(0.7).next_to(point6, LEFT)
        label1 = MathTex("f(x)=x-1", color=BLACK)\
        .rotate(PI/4)\
        .move_to(axes.c2p(-2.5, -2.2)).shift(DOWN*2+RIGHT*0.8)
        label2 = MathTex("f(x)=x+1", color=BLACK)\
        .rotate(PI/4)\
        .move_to(axes.c2p(2.5, 3.2)).shift(DOWN*1+RIGHT*0.7)
        self.add(
            axes,x_label,y_label,
            line1, line2,point1,point2,point3,point4,point5,point6,
            label_dot1, label_dot2,
            label_dot3, label_dot4,label_dot5,label_dot6,
            label1, label2,x_label1,y_label1,tip1,tip2
        )
        
        

       

        