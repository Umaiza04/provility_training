from manim import*
config.frame_height=12
config.frame_width=15
config.pixel_width=2500
config.pixel_height=2500

class step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        polygon = RegularPolygon(n=6,color="#A00498",stroke_width=6).scale(3.0)
        labels = VGroup(
            MathTex("A", color=BLACK).shift(DOWN*3+LEFT*1.5),
            MathTex("B", color=BLACK).shift(DOWN*3+RIGHT*1.5),
            MathTex("C",color=BLACK).shift(RIGHT*3.4),
            MathTex("F",color=BLACK).shift(LEFT*3.4),
            MathTex("E",color=BLACK).shift(UP*3+LEFT*1.5),
            MathTex("D",color=BLACK).shift(UP*3+RIGHT*1.5) )
        
        vector1 = MathTex(r"\vec{a}", color=BLACK).shift(DOWN*3.1)
        vector2 = MathTex(r"\vec{b}", color=BLACK).shift(RIGHT*2.8+DOWN*1.3)
        vector3 = MathTex(r"-\vec{a}", color=BLACK).shift(UP*3.1)
        vector4 = MathTex(r"-\vec{b}", color=BLACK).shift(LEFT*2.8+UP*1.6)
        vector5 = MathTex(r"\vec{b}-\vec{a}}", color=BLACK).shift(RIGHT*3.1+UP*1.5)
        vector6 = MathTex(r"-\vec{b}-\vec{a}}", color=BLACK).shift(LEFT*3.2+DOWN*1.5)
        vector7 = MathTex(r"2\vec{b}", color=BLACK).shift(UP*0.5+LEFT*0.3)
        vector8 = MathTex(r"\vec{a}+\vec{b}}", color=BLACK).shift(DOWN*0.5+RIGHT*1).rotate(PI/5.5)

        vertices = polygon.get_vertices()
        tips = VGroup()
        for i in range(len(vertices)):
            side = Line(vertices[i], vertices[(i+1) % len(vertices)])
            mid = side.get_midpoint()
            direction = side.copy().rotate(-PI/250).get_unit_vector()
            tipline = Line(mid - 0.25*direction, mid + 0.25*direction).set_stroke(width=0).add_tip(tip_length=0.32,tip_width=0.25).set_color(BLACK)
            tips.add(tipline)

        diag1 = Line(vertices[4], vertices[0], color="#1D5DEC", stroke_width=4).shift(UP*0.03)
        mid1 = diag1.get_midpoint()
        dir1 = diag1.get_unit_vector()
        diag1_tip = Line( mid1 - 0.75*dir1, mid1 + 0.75*dir1).set_stroke(width=0).add_tip(tip_length=0.32,tip_width=0.25).set_color(BLACK)
         
        diag2 = Line(vertices[4], vertices[1], color="#1D5DEC", stroke_width=4)
        mid2 = diag2.get_midpoint()
        dir2 = diag2.get_unit_vector()
        diag2_tip = Line(  mid2 - 0.25 * dir2,  mid2 + 0.25 * dir2).set_stroke(width=0).add_tip(tip_length=0.32,tip_width=0.25).set_color(BLACK)
          
        self.add(diag1,diag2,polygon,labels,vector1,vector2,tips,vector3,vector4,vector5,vector6,vector7,vector8,diag1_tip,diag2_tip)