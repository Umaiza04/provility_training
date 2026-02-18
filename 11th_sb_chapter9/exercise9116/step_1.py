from manim import*
config.frame_height=10
config.frame_width=15
config.pixel_width=2500
config.pixel_height=2500

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[-3, 4.5, 1],
            y_range=[0, 4.5, 1],
            x_length=11,
            y_length=6,
            axis_config={"include_numbers": True,
                          "include_tip": True,"tip_length":0.15,"tip_width":0.25,"color": BLACK, "stroke_width":3},
                           x_axis_config={"numbers_to_include": [ 1, 2, 3, 4],
                           "decimal_number_config": {
                           "num_decimal_places": 0,
                           "color": BLACK, }, },
            y_axis_config={"numbers_to_include": [ 1, 2, 3,4],
                           "decimal_number_config": {
                           "num_decimal_places": 0,
                           "color": BLACK, },  }, ) 
        axes.x_axis.get_tick_marks()[0].set_opacity(0)
        axes.x_axis.get_tick_marks()[1].set_opacity(0)
        axes.x_axis.get_tick_marks()[2].set_opacity(0)

        x_label = axes.get_x_axis_label("x").set_color(BLACK).shift(DOWN*0.3)
        y_label = axes.get_y_axis_label("y").set_color(BLACK).shift(LEFT*0.3+UP*0.1)
        #parabola
        parabola = axes.plot_parametric_curve( lambda t: np.array([t, t**2, 0]), t_range=[-2, 2],color="#751973",stroke_width=5).set_z_index(-1)
        line = axes.plot( lambda x: 8 - 2*x, x_range=[2, 4],color="#751973",stroke_width=5)
        label1 = MathTex("y = x^2",color=BLACK).rotate(PI/2.7).next_to(   axes.coords_to_point(1, 1),)
        label2 = MathTex("y = 8-2x",color=BLACK).rotate(PI/-2.9).next_to(axes.coords_to_point(2.8, 1.6),)
        dot1 = Dot(axes.coords_to_point(2, 4))
        dot2 = Dot(axes.coords_to_point(3.6, 4))
        dot3 = Dot(axes.coords_to_point(4, 0))
        start_point = axes.coords_to_point(4, 4)
        end_point = start_point + RIGHT * 1.5
        arrow = Arrow( start=start_point, end=end_point, buff=0, stroke_width=3, color=BLACK,tip_length=0.25).shift(UP*0.06)
        dot4 = Dot(start_point, color=BLACK).shift(UP*0.06)
        label3 = MathTex("(2,4)",color=BLACK).next_to(dot1, UP)
        label4 = MathTex(r"(4,4)\; y=4",color=BLACK).next_to(dot2, UP + RIGHT*0.2+DOWN*1.2)
        label5 = MathTex("(4,0)",color=BLACK).next_to(dot3, DOWN*3)

        self.add(parabola,line,axes,x_label,y_label,label1,label2,label3,label4,label5,arrow,dot4)