from manim import*
config.frame_height=10
config.frame_width=12
config.pixel_width=2800
config.pixel_height=2800

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        number_line = NumberLine(
            x_range=[-5, 5, 1],
            length=10,
            include_ticks=False,
            include_numbers=False,
            color=BLACK)

        number_line.add_tip(tip_length=0.35,tip_width=0.25)
        number_line.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        left_tip = StealthTip(color=BLACK).scale(0.9).move_to(number_line.n2p(0) + LEFT * 1).rotate(PI)
        right_tip = StealthTip(color=BLACK).scale(0.9).move_to(number_line.n2p(0) + RIGHT * 1)
        
        middle_line = Line(UP * 0.15,DOWN * 0.15,stroke_width=3,color=BLACK).move_to(number_line.n2p(0))
        #labels
        label1 = MathTex("0", color=BLACK).next_to(number_line.n2p(0), DOWN)
        label2 = MathTex("0^-", color=BLACK).next_to(number_line.n2p(-1), UP)
        label3 = MathTex("0^+", color=BLACK).next_to(number_line.n2p(1), UP)
        label4 = MathTex("L.H.L", color=BLACK).next_to(label2, UP*1.4).shift(LEFT)
        label5 = MathTex("R.H.L", color=BLACK).next_to(label3, UP*1).shift(RIGHT)
        left_func = MathTex("f(x)=x-1", color=BLACK).next_to(number_line.n2p(-2.5), DOWN*2)
        right_func = MathTex("f(x)=x+1", color=BLACK).next_to(number_line.n2p(2.5), DOWN*2)
        #braces
        left_brace = BraceBetweenPoints(
            number_line.n2p(-4),
            number_line.n2p(-1),
            direction=DOWN,color=BLACK)

        right_brace = BraceBetweenPoints(
            number_line.n2p(1),
            number_line.n2p(4),
            direction=DOWN,color=BLACK)

        self.add(
            number_line,label1,label2,label3,label4,label5,
            left_func,
            right_func,
            left_brace,
            right_brace,  middle_line,left_tip, right_tip
        )