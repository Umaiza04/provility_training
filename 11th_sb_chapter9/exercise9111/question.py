from manim import*
config.frame_height=10
config.frame_width=12
config.pixel_width=2800
config.pixel_height=2800

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[-2, 6, 1],
            y_range=[-4, 4, 1],
            x_length=10,
            y_length=8,
            axis_config={"color": "#0B7A2F",
                         "include_tip": True,
                         "tip_length": 0.35,
                         "tip_width": 0.25,
                         "stroke_width": 10,},
            x_axis_config={"numbers_to_include": [-2, -1, 1, 2, 3, 4, 5],
                           "decimal_number_config": {
                           "num_decimal_places": 0,
                           "color": BLACK, }, },
            y_axis_config={"numbers_to_include": [-3, -2, -1, 1, 2, 3],
                           "decimal_number_config": {
                           "num_decimal_places": 0,
                           "color": BLACK, },  }, )

        axes.y_axis.get_tick_marks()[0].set_opacity(0)

        for num in axes.y_axis.numbers:
            if num.get_value() < 0:
                num.next_to( axes.y_axis.number_to_point(num.get_value()), RIGHT, buff=0.12  )

        x_label = axes.get_x_axis_label(Text("x", color=BLACK)).shift(DOWN*0.4)
        y_label = axes.get_y_axis_label(Text("y", color=BLACK)).shift(UP*0.25+LEFT*0.7)

        f = lambda x: 1/(x-3)
        y_top = axes.y_range[1]
        y_bottom = axes.y_range[0]
        x_right_limit = 3 + 1/y_top
        x_left_limit = 3 + 1/y_bottom
        left_curve = axes.plot(f,x_range=[axes.x_range[0], x_left_limit],color="#1F2A7C",stroke_width=6,use_smoothing=False)
        right_curve = axes.plot( f, x_range=[x_right_limit, axes.x_range[1]], color="#1F2A7C", stroke_width=6, use_smoothing=False)

        dashline = DashedLine(
            axes.c2p(3, -4),
            axes.c2p(3, 4),
            color="#BB3F3F",
            stroke_width=8,
            dash_length=0.15 )

        dashlabel = MathTex("x=3", color=BLACK).scale(1.0).next_to(axes.c2p(3, -2), RIGHT, buff=0.3)

        self.add( axes, x_label, y_label, left_curve, right_curve, dashline, dashlabel)