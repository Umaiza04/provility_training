
from manim import *
import numpy as np
config.frame_height=13
config.frame_width=18
config.pixel_width=2500
config.pixel_height=2800

class step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        P = np.array([-4, 0, 0])        
        A = np.array([4, 0, 0])        
        B = np.array([4, 5, 0])        
        C = np.array([4, 9, 0])       
        
        Pdot = Dot(P, color=("#0343DF")).scale(1.6)
        Adot = Dot(A, color=("#0343DF")).scale(1.6)
        Bdot = Dot(B, color=("#0343DF")).scale(1.6)
        Cdot = Dot(C, color=("#0343DF")).scale(1.6)

        Plabel = MathTex("P", color=BLACK).next_to(Pdot,DOWN)
        Alabel = MathTex("A", color=BLACK).next_to(Adot,DOWN)
        Blabel = MathTex("B", color=BLACK).next_to(Bdot,RIGHT)
        Clabel=MathTex("C",color=BLACK).next_to(Cdot)

        PA = Line(P, A, color="#937C00",stroke_width=5)
        PB = Line(P, B, color="#937C00",stroke_width=5)
        PC = Line(P, C, color="#937C00",stroke_width=5)
        AB = Line(A, B, color="#937C00",stroke_width=5)
        BC = Line(B,C,color="#937C00",stroke_width=5)
        P_label = Tex("Car parked point", color=BLACK,font_size=60).scale(0.6).next_to(P, DOWN*4)
        A_label = Tex("Ground point", color=BLACK,font_size=60).scale(0.6).next_to(A, DOWN*4)
        PA_label = MathTex("100\\,m", color=BLACK).next_to(PA, DOWN, buff=0.15)
        AB_label = MathTex("100\\,m",color=BLACK).next_to(AB,RIGHT)
        P_angle = Angle(PA, PB, radius=1.5, color=BLACK)
        P_anglelabel = MathTex("45^\\circ", color="#653700").next_to(P_angle,RIGHT, buff=0.3)
        right_angle = RightAngle(Line(A, P),Line(A, B),quadrant=(1, 1),length=0.6,color=BLACK).shift(0.03 * RIGHT + 0.03 * UP)
        dashed_line = DashedLine( start=B, end=B + LEFT * 7, dash_length=0.15, color=BLACK,stroke_width=5)
        B_ref = Line(B,B + LEFT * 7,stroke_opacity=0)
        B_angle = Angle(B_ref, Line(B, P), radius=1.57, color=BLACK)
        line=Line([0,0.048,0],[0.022,0,0],color=BLACK).add_tip().shift(UP*4.17+RIGHT*3+LEFT*0.36).scale(1.0)
        t_label = MathTex("t = 15\\,s", color=BLACK).next_to(AB, RIGHT*2.7, buff=1)
        x_label = MathTex("x = ?", color=BLACK,font_size=70).next_to(Line(B, C).get_center(), RIGHT, buff=0.4)
        arrow = Arrow(start=A,end=B,stroke_width=2,color=BLACK).shift(RIGHT*2.3+DOWN*0.14)
        balloon1=ImageMobject("step_1.png").scale(0.2).next_to(Bdot,buff=0.1)
        balloon2=ImageMobject("step_1.png").scale(0.2).next_to(Cdot,buff=0.1)
        angle_label = MathTex(r"45^\circ", color="#653700").shift(UP*4.4+RIGHT*2)

    

        self.add(PA,line,B_angle,PB,PC,AB,BC,Pdot,Adot,Cdot,Plabel,Alabel,Blabel,Clabel,P_label,A_label,PA_label,AB_label,
                 P_angle,P_anglelabel,right_angle,dashed_line,Bdot,t_label,x_label,arrow,balloon1,balloon2,angle_label,B_ref)