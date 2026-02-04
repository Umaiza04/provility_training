from manim import *
import numpy as np
config.frame_height=16
config.frame_width=18
config.pixel_width=2500
config.pixel_height=2500

class step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        P = np.array([-6, -2, 0])
        A = np.array([ 2, -2, 0])
        B = A + np.array([8*np.cos(PI/3), 8*np.sin(PI/3), 0])
        Pdot = Dot(P, color=("#0343DF")).scale(1.6)
        Adot = Dot(A, color=("#0343DF")).scale(1.6)
        Bdot = Dot(B, color=("#0343DF")).scale(1.6)
        #labels
        Plabel = MathTex("P", color=BLACK).next_to(Pdot, DOWN)
        Alabel = MathTex("A", color=BLACK).next_to(Adot, DOWN)
        Blabel = MathTex("B", color=BLACK).next_to(Bdot, UP)
        label1 = Text("Port", color=BLACK,font_size=30).next_to(Pdot, LEFT*2.5).shift(DOWN*0.6)
        #boat image
        boat = ImageMobject("boat.png")
        boat.scale(0.5)
        boat.next_to(Bdot,LEFT).shift(RIGHT*4.6)
        # Lines
        PA = Line(P, A, color="#C68642", stroke_width=5)
        AB = Line(A, B, color="#C68642", stroke_width=5)
        PBline = DashedVMobject(Line(P, B, color="#C68642"),num_dashes=65)
        Aline = DashedLine(A, A + RIGHT*2.5, color="#6B7C85")
        #A angle
        angle = Angle(Aline, AB,radius=1.0, color="#0343DF")
        label2 = MathTex("10\\ \\text{km}", color=BLACK).next_to(PA, DOWN)
        label3 = MathTex("8\\ \\text{km}", color=BLACK).rotate(AB.get_angle()).move_to(AB.get_midpoint()).shift(LEFT*0.5)
        label4 = MathTex("60^\\circ", color=BLACK).next_to(angle).shift(UP)
        self.add( PA, AB, PBline, Aline, angle, Pdot, Adot, Bdot,
            Plabel, Alabel, Blabel, label1, label2, label3, label4,boat)
