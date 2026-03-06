from manim import*
config.frame_height=10
config.frame_width=15
config.pixel_width=2500
config.pixel_height=2500

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        line = NumberLine(
            x_range=[-5, 5, 1],
            length=10,
            include_ticks=False,
            include_numbers=False,
            color="#AC4F06",stroke_width=4)
        line.add_tip(tip_length=0.35,tip_width=0.25)
        line.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        zero = line.n2p(-1.7)
        pi_point = line.n2p(1.5)
        label1 = MathTex("-\\infty", color=BLACK).scale(0.9).next_to(line, LEFT).shift(DOWN*0.4+RIGHT*0.7)
        label2 = MathTex("\\infty", color=BLACK).scale(0.9).next_to(line, RIGHT).shift(DOWN*0.4+LEFT*0.7)

        zero_label = MathTex("0", color=BLACK).scale(0.9).next_to(zero, DOWN)
        pi_label = MathTex("\\pi", color=BLACK).scale(0.9).next_to(pi_point, DOWN).shift(DOWN*0.06)
        tick_zero = Line( zero + UP*0.15, zero + DOWN*0.15, color=BLACK)
        tick_pi = Line(pi_point + UP*0.15,pi_point + DOWN*0.15,color=BLACK)
        
        brace1 = BraceBetweenPoints(line.n2p(-4.8),line.n2p(-1.8),direction=DOWN,color=BLACK).shift(DOWN*0.7)
        brace2 = BraceBetweenPoints(line.n2p(-1.6),line.n2p(1.4),direction=DOWN,color=BLACK).shift(DOWN*0.7)
        brace3 = BraceBetweenPoints(line.n2p(1.6),line.n2p(4.8),direction=DOWN,color=BLACK).shift(DOWN*0.7)

        f1 = MathTex("x<0", color=BLACK).scale(0.8).next_to(brace1, DOWN).shift(UP*1)
        f2 = MathTex("0<=x<\\pi", color=BLACK).scale(0.8).next_to(brace2, DOWN).shift(UP*1)
        f3 = MathTex("x>\\pi", color=BLACK).scale(0.8).next_to(brace3, DOWN).shift(UP*1)

        shift_amt = 0.6
        zero_minus = MathTex("0^{-}", color=BLACK).scale(0.8).move_to(zero + LEFT*shift_amt + UP*0.6)
        zero_plus  = MathTex("0^{+}", color=BLACK).scale(0.8).move_to(zero + RIGHT*shift_amt + UP*0.6).shift(RIGHT*0.3)
        pi_minus = MathTex("\\pi^{-}", color=BLACK).scale(0.8).move_to(pi_point + LEFT*shift_amt + UP*0.6)
        pi_plus  = MathTex("\\pi^{+}", color=BLACK).scale(0.8).move_to(pi_point + RIGHT*shift_amt + UP*0.6).shift(RIGHT*0.3)

        height=0.6
        arrow1 = Arrow(start=zero + LEFT*0.8 + UP*height,end=zero + LEFT*0.05 + UP*height,buff=0,stroke_width=2,color="#030AA7").shift(DOWN*0.3+LEFT*0.2)
        arrow2 = Arrow(start=zero + RIGHT*0.8 + UP*height,end=zero + RIGHT*0.05 + UP*height,buff=0,stroke_width=2,color="#030AA7").shift(DOWN*0.3+RIGHT*0.2)
        arrow3 = Arrow(start=pi_point + LEFT*0.8 + UP*height,end=pi_point + LEFT*0.05 + UP*height,buff=0,stroke_width=2,color="#030AA7").shift(DOWN*0.3+LEFT*0.2)
        arrow4 = Arrow(start=pi_point + RIGHT*0.8 + UP*height,end=pi_point + RIGHT*0.05 + UP*height,buff=0,stroke_width=2,color="#030AA7").shift(DOWN*0.3+RIGHT*0.2)

        self.add(line,label1,label2,zero_label, pi_label,brace1, brace2, brace3,f1, f2, f3,
                 tick_zero,tick_pi,zero_minus,zero_plus,pi_minus,pi_plus,arrow1 ,arrow2,arrow3,arrow4)