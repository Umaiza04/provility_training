from turtle import tiltangle
from manim import*
config.frame_height=8
config.frame_width=10
config.pixel_width=2500
config.pixel_height=2500

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        A = np.array([0, 3, 0])
        B = np.array([-3, -2, 0])
        C = np.array([3, -2, 0])
        triangle = Polygon(A, B, C, color="#A00498", stroke_width=4.5)
        labelA = Text("A", color=BLACK).next_to(A, UP*0.2).scale(0.7)
        labelB = Text("B", color=BLACK).next_to(B, DOWN*0.2).scale(0.7).shift(LEFT*0.1)
        labelC = Text("C", color=BLACK).next_to(C, DOWN*0.2).scale(0.7)
        D = interpolate(A, B, 0.45)   
        E = interpolate(A, C, 0.45)   
        DE = Line(D, E, color=BLACK, stroke_width=4).set_length(2.6)
        DE.add_tip(tip_shape=StealthTip,tip_length=0.11,   tip_width = 0.02)
        DE.add_tip(tip_shape=StealthTip,tip_length=0.11, at_start=True)
        labelD = MathTex("D", color=BLACK).scale(0.8).shift(LEFT*1.8+UP*0.74)
        labelE = MathTex("E", color=BLACK).next_to(DE).scale(0.8)
        vector1 = MathTex(r"(\vec{a})", color=BLACK).next_to(A,buff=0.2).shift(UP*0.2)
        vector2 = MathTex(r"(\vec{b})", color=BLACK).next_to(B,buff=0.3).shift(DOWN*0.35+LEFT*0.15)
        vector3 = MathTex(r"(\vec{c})", color=BLACK).next_to(C,buff=0.2).shift(DOWN*0.3)
        self.add(triangle,labelA,labelB,labelC,labelD,labelE,DE,vector1,vector2,vector3)
        