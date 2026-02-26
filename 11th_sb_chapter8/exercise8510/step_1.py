from manim import *
import numpy as np

config.frame_height = 8
config.frame_width = 10
config.pixel_height = 2800
config.pixel_width = 2800
config.background_color = WHITE

class Step_1(Scene):
    def construct(self):
        A = np.array([-3, 2, 0])
        B = np.array([ 3, 2, 0])
        O = np.array([ 0,-2.5, 0])
        P = np.array([ 0, 2, 0])
        #triangle creation
        AB = Line(A, B, color="#0343DF", stroke_width=3)
        OA = Line(O, A, color="#0343DF", stroke_width=3)
        OB = Line(O, B, color="#0343DF", stroke_width=3)
        OP = Line(O, P, color="#E53935", stroke_width=3)
        for line in [AB, OA, OB, OP]:
            line.set_cap_style(CapStyleType.ROUND)

        def mid_tip(line, color=BLACK):
            mid = line.point_from_proportion(0.5)
            angle = line.get_angle()
            tip = StealthTip(length=0.25, color=color)
            tip.rotate(angle)
            tip.move_to(mid)
            return tip
        tip1 = mid_tip(OA).shift(RIGHT*0.03)
        tip2 = mid_tip(OB).shift(LEFT*0.03)
        tip3 = mid_tip(OP)
        tip4=mid_tip(AB).shift(LEFT*1.5)
        #labels
        label_A = MathTex("A",color=BLACK).next_to(A, LEFT)
        label_B = MathTex("B",color=BLACK).next_to(B, RIGHT)
        label_C = MathTex("C",color=BLACK).next_to(P, UP*0.6)
        label_O = MathTex("O",color=BLACK).next_to(O, DOWN)
        label_a = MathTex(r"\vec a",color=BLACK).next_to(OA, LEFT).shift(RIGHT*1.2)
        label_b = MathTex(r"\vec b",color=BLACK).next_to(OB, RIGHT).shift(LEFT*1.2)
        label_mn = MathTex("m : n", color="#E53935").next_to(P, UP*4.7)
        label = MathTex("1 : 2", color=BLACK).next_to(P, UP*2.7).shift(RIGHT*0.05)
        #curve
        curve_start = P + UP*1.4+RIGHT*0.4          
        curve_control1 = curve_start + UP*1.8
        curve_control2 = np.array([-7, 3, 0])  
        curve_end = np.array([-2.7, -0.2, 0])     
        curve1 = CubicBezier(
            curve_start,
            curve_control1,
            curve_control2,
            curve_end,
            color="#E53935",
            stroke_width=3).shift(UP*0.2)
        p1 = curve1.point_from_proportion(0.9)
        p2 = curve1.point_from_proportion(1.0)
        angle = np.arctan2(p2[1] - p1[1], p2[0] - p1[0])
        curve_tip = StealthTip(color="#E53935", length=0.25)
        curve_tip.rotate(angle)
        curve_tip.move_to(curve_end).shift(UP*0.2)
        #curve2
        curve2_start = P + UP*1.4 + LEFT*0.4
        curve2_control1 = curve2_start + UP*1.8
        curve2_control2 = np.array([7, 3, 0])
        curve2_end = np.array([2.7, -0.2, 0])
        curve2 = CubicBezier(
            curve2_start,
            curve2_control1,
            curve2_control2,
            curve2_end,
            color="#E53935",
            stroke_width=3).shift(UP*0.2)
        q1 = curve2.point_from_proportion(0.9)
        q2 = curve2.point_from_proportion(1.0)
        angle2 = np.arctan2(q2[1] - q1[1], q2[0] - q1[0])
        tip5 = StealthTip(color="#E53935", length=0.25).rotate(angle2).move_to(curve2_end).shift(UP*0.2)

        self.add(OP, AB, OA, OB,tip1, tip2, tip3,label_A, label_B, label_C, label_O,label_a, label_b,
            label_mn,label,curve1, curve_tip,curve2,tip4,tip5)