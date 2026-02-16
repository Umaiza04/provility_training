from manim import*
config.frame_height=4
config.frame_width=8
config.pixel_width=1500
config.pixel_height=1000

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        A = LEFT * 3
        B = RIGHT * 3
        P = A + (1/3) * (B - A)
        AB = Line(A, B, color="#030764", stroke_width=5).add_tip(tip_width=0.25)
        tick = Line(P + UP*0.15, P + DOWN*0.15, color="#9D0759", stroke_width=6)
        #labels
        label_A = MathTex("A", color=BLACK).next_to(A, DOWN, buff=0.1).scale(0.8)
        label_B = MathTex("B", color=BLACK).next_to(B, DOWN, buff=0.1).scale(0.8)
        label_P = MathTex("P", color=BLACK).next_to(P, DOWN, buff=0.2).scale(0.8)
        ratio = MathTex("1:2", color=BLACK).next_to(P, UP, buff=0.3).scale(1)

        vec_a = MathTex(r"\vec{a}", color=BLACK).next_to(A, DOWN*2,buff=0.25)
        vec_b = MathTex(r"\vec{b}", color=BLACK).next_to(B, DOWN*2,buff=0.25)

        self.add(AB, tick, label_A, label_B, label_P, ratio, vec_a, vec_b)