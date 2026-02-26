from manim import *

config.frame_height = 6
config.frame_width = 10
config.pixel_width = 2500
config.pixel_height = 2500

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        origin = ORIGIN

        #vector b
        vec_b = Line(origin,RIGHT*3.5, stroke_width=3, color="#076808").add_tip(tip_length=0.25, tip_width=0.2).set_z_index(5).shift(LEFT*0.015)

        #two perpendicular vectors
        #vector a
        vec_a = Line(origin, UP*1.5, stroke_width=3, color=BLUE).add_tip(tip_length=0.25, tip_width=0.2).set_z_index(1)
        vec_a1 = Line(origin, DOWN*1.5, stroke_width=3, color=BLUE).add_tip(tip_length=0.25, tip_width=0.2).set_z_index(1)
        #vec bc
        vec_bc = origin
        vec_bc1=origin
        vec_bc = Line(vec_bc,vec_bc + UP*3.0, stroke_width=3, color="#937C00").add_tip(tip_length=0.25, tip_width=0.2).set_z_index(-1)
        vec_bc1 = Line(vec_bc,vec_bc1 + DOWN*3.0, stroke_width=3, color="#937C00").add_tip(tip_length=0.25, tip_width=0.2)
        L=2.1
        vec_c = Line(origin, RIGHT*1.7 + L*UP*1.4, stroke_width=3, color="#DF6625").add_tip(tip_length=0.25, tip_width=0.2)
        label_a = MathTex(r"\vec{a}", color=BLACK).next_to(vec_a, LEFT).shift(UP*0.7)
        label_a1 = MathTex(r"-\vec{a}", color=BLACK).next_to(vec_a1, LEFT).shift(DOWN*0.5)
        label_b = MathTex(r"\vec{b}", color=BLACK).next_to(vec_b.get_end(),RIGHT*0.4)
        label_c = MathTex(r"\vec{c}", color=BLACK).next_to(vec_c.get_end(), RIGHT*0.4)
        label_bc = MathTex(r"\vec{b}\times\vec{c}", color=BLACK).next_to(vec_bc,UP).shift(LEFT*0.8+DOWN*0.5)
        label_bc1 = MathTex(r"-(\vec{b}\times\vec{c})", color=BLACK).next_to(vec_bc1,DOWN).shift(LEFT*1.15+UP*0.7)
        angle_bc = Angle(vec_b,vec_c, radius=1,color=PURPLE,stroke_width=3).set_z_index(-1)
        sector_bc = Sector(start_angle=0,angle=PI / 3,fill_opacity=0.35,stroke_width=0).set_fill(PURPLE, opacity=0.35).set_z_index(-1)
        angle_label = MathTex(r"\pi/3",color=BLACK).move_to(angle_bc.point_from_proportion(0.7) + 0.4 * RIGHT).scale(0.7)
        right_angle1 = RightAngle(vec_b,vec_a, length=0.3,color=BLACK,stroke_width=2.5)
        right_angle2 = RightAngle(vec_b,vec_bc, length=0.35,quadrant=(1, 1),color=BLACK,stroke_width=2.5).shift(UP*0.6).set_z_index(-1)

        self.add(vec_b,vec_a,vec_a1, vec_bc,vec_bc1, vec_c,label_a,label_a1, label_b, label_c, label_bc,label_bc1,angle_label,angle_bc,right_angle1,right_angle2,sector_bc )