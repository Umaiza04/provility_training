from manim import*
config.frame_height=10
config.frame_width=12
config.pixel_width=2800
config.pixel_height=2800

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=9,
            y_length=9,
            axis_config={"color": "#02590F",
                          "include_tip": True,
                          "tip_length": 0.35,
                          "tip_width": 0.25 },
            x_axis_config={"numbers_to_include": list(range(-3, 4)),
                           "decimal_number_config": {
                           "num_decimal_places": 0,  
                           "color": BLACK, }, },
            y_axis_config={"numbers_to_include": list(range(-3, 4)),
                           "decimal_number_config": {
                           "num_decimal_places": 0,  
                           "color": BLACK, }, }, )
        axes.y_axis.get_tick_marks()[0].set_opacity(0)
        axes.y_axis.get_tick_marks()[3].set_opacity(0)
        axes.y_axis.get_tick_marks()[4].set_opacity(0)
        axes.x_axis.get_tick_marks()[0].set_opacity(0)
        for num in axes.y_axis.numbers:
          if num.get_value() == 1:
           num.set_opacity(0)  
          if num.get_value() < 0:
            num.next_to( axes.y_axis.number_to_point(num.get_value()), RIGHT, buff=0.12)

        x_label = axes.get_x_axis_label(MathTex("x",color=BLACK)).shift(DOWN*0.3+RIGHT*0.07)
        y_label = axes.get_y_axis_label(MathTex("y",color=BLACK)).shift(UP*0.2+LEFT*0.7)
        line1 = axes.plot(lambda x: x - 1, x_range=[-2.5, 0], color="#26538D", stroke_width=5)
        line2 = axes.plot(lambda x: x + 1, x_range=[0, 2.5], color="#A0025C", stroke_width=5)

        circle1 = Circle(radius=0.05, color=BLACK,fill_color=WHITE, fill_opacity=1,stroke_width=1.5).move_to(axes.c2p(0, -1)).set_fill(opacity=1)
        circle2 = Circle(radius=0.05, color=BLACK,fill_color=WHITE, fill_opacity=1,stroke_width=1.5).move_to(axes.c2p(0, 1)).set_fill(opacity=1)

        label1 = MathTex("f(x)=x-1", color=BLACK).rotate(PI/4).move_to(axes.c2p(-2.5, -2.5)).scale(1).shift(UP*0.08+RIGHT*0.75)
        label2 = MathTex("f(x)=x+1", color=BLACK).rotate(PI/4).move_to(axes.c2p(2.2, 2.7)).scale(1).shift(UP+LEFT*0.9+DOWN*0.8)
        self.add(axes,x_label,y_label,line1, line2,circle1, circle2, label1, label2)

        