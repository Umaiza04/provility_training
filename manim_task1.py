from manim import *

class ParabolaDiagram(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        txt_color = BLACK 

        axes = Axes(
            x_range=[-6, 15, 1], 
            y_range=[-14, 14, 1], 
            y_length=8.5, 
            axis_config={
                "include_tip": True,
                "color": txt_color,
                "stroke_width": 2,
                "include_ticks": False,
            },
        ).scale(0.75) 

       
        for axis in [axes.x_axis, axes.y_axis]:
            axis.set_tick_custom_length(0.2)
        # Labels for X, X', Y, Y'
        x_labels = MathTex("X", color=txt_color).next_to(axes.x_axis.get_end())
        y_labels = MathTex("Y", color=txt_color).next_to(axes.y_axis.get_end()).shift(UP*0.3,LEFT*0.4)
        x_prime = MathTex("X'", color=txt_color).next_to(axes.x_axis.get_start(), LEFT)
        y_prime = MathTex("Y'", color=txt_color).next_to(axes.y_axis.get_start(), DOWN)
        axis_label = Text("Axis of parabola", font_size=20, color=txt_color).next_to(axes.x_axis.get_end(), UP, buff=0.3)

        #The Parabola 
        parabola = axes.plot_parametric_curve(
            lambda t: np.array([t**2 / 25, t, 0]),
            t_range=[-13, 13],
            color="#1D5DEC",
            stroke_width=5
        )
        eqn_label = MathTex("y^2 = 12x", color=txt_color,font_size=35).move_to(axes.c2p(10, -5)).shift(DOWN*1.8)

        #Vertex and Focus
        v_dot = Dot(axes.c2p(0, 0), color="#CF0234")
        v_label = VGroup(
            MathTex("V", color=txt_color, font_size=30),
            MathTex("(0, 0)", color=txt_color, font_size=28)
        ).arrange(DOWN, buff=0.1).next_to(v_dot, DL, buff=0)

        f_dot = Dot(axes.c2p(3, 0), color="#CF0234")
        f_coords = MathTex("(3, 0)", color=txt_color, font_size=28).next_to(f_dot, DL, buff=0.10)
        f_text = MathTex(r"\text{Focus}", color=txt_color, font_size=30).next_to(f_dot, DR, buff=0.1)

        #Directrix (x = -3)
        directrix = DashedLine(
            start=axes.c2p(-3, -11),
            end=axes.c2p(-3, 11),
            color="#CF0234",
            dash_length=0.10
        )
        directrix.add_tip() 
        directrix.add_tip(at_start=True)

        dir_label = Text("Equation of \n   Directrix", color=txt_color, font_size=18,line_spacing=0.5).move_to(axes.c2p(-4, -4)).rotate(90 * DEGREES).shift(DOWN*0.3)
        dir_eqn = MathTex("x = -3", color=txt_color, font_size=28).next_to(dir_label, DOWN, buff=0.1).shift(DOWN*0.6,RIGHT*0.4)
        

        #Latus Rectum
        latus_rectum = Line(
            start=axes.c2p(3, -8.5),
            end=axes.c2p(3, 8.5),
            color=GREEN_E,
            stroke_width=4
        )
        
        # Brace and Length Label
        brace = Brace(latus_rectum, direction=RIGHT, color=txt_color,buff=1.0)
        brace_text = Text("  Length of  \n  Latus Rectum = 12", color=txt_color, font_size=20, line_spacing=0.8).next_to(brace, RIGHT, buff=0.5)

        # Add everything to Scene
        self.add(
            axes, x_labels,y_labels, x_prime, y_prime, axis_label,
            parabola, eqn_label,
            v_dot, v_label,
            f_dot, f_coords, f_text,
            directrix, dir_label, dir_eqn,
            latus_rectum, brace, brace_text)