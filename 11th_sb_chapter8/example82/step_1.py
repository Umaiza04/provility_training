from manim import*
config.frame_height=16
config.frame_width=18
config.pixel_width=2500
config.pixel_height=2500

class step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        polygon = RegularPolygon(n=6,color="#A00498",stroke_width=8).scale(4.0)
        labels = VGroup(
            MathTex("A", color=BLACK).shift(DOWN*4+LEFT*2),
            MathTex("B", color=BLACK).shift(DOWN*4+RIGHT*2),
            MathTex("C",color=BLACK).shift(RIGHT*4.4),
            MathTex("F",color=BLACK).shift(LEFT*4.4),
            MathTex("E",color=BLACK).shift(UP*4+LEFT*2),
            MathTex("D",color=BLACK).shift(UP*4+RIGHT*2) )
        vector1 = MathTex(r"\vec{a}", color=BLACK).shift(DOWN*4.2).scale(1.3)
        vector2 = MathTex(r"\vec{b}", color=BLACK).shift(RIGHT*3.7+DOWN*1.8).scale(1.3)
        vertices = polygon.get_vertices()
        tips = VGroup()
        for i in range(len(vertices)):
            side = Line(vertices[i], vertices[(i+1) % len(vertices)])
            mid = side.get_midpoint()
            direction = side.copy().rotate(-PI/64).get_unit_vector()
            tipline = Line(mid - direction, mid + 0.25*direction).set_stroke(width=0).add_tip(tip_length=0.32).set_color(BLACK)
            tips.add(tipline)
        self.add(polygon,labels,vector1,vector2,tips)