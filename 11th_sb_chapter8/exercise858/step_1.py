from manim import*
config.frame_height=8
config.frame_width=10
config.pixel_width=1500
config.pixel_height=1000

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        A = LEFT*1.5 + DOWN*0.8
        B = RIGHT*2.0 + DOWN*1
        C = RIGHT*2.5 + UP*1
        D = LEFT*1.0 + UP*1.2
        quad = Polygon(A, B, C, D, color="#015482", stroke_width=4)
        #lines creation
        AB = Line(A, B, color="#015482", stroke_width=4)
        BC = Line(B, C, color="#015482", stroke_width=4)
        CD = Line(C, D, color="#015482", stroke_width=4)
        DA = Line(D, A, color="#015482", stroke_width=4)
        #labels
        label_A = MathTex("A", color=BLACK).scale(0.6).next_to(A, DOWN+LEFT, buff=0.05)
        label_B = MathTex("B", color=BLACK).scale(0.6).next_to(B, DOWN+RIGHT, buff=0.04)
        label_C = MathTex("C", color=BLACK).scale(0.6).next_to(C, UP+RIGHT, buff=0.04)
        label_D = MathTex("D", color=BLACK).scale(0.6).next_to(D, UP+LEFT, buff=0.0)
       
        def middle_tip(start, end, face_point, position=0.5):
             mid = interpolate(start, end, position)
             direction = face_point - mid
             angle = angle_of_vector(direction)
             tip = StealthTip(color=BLACK,stroke_width=0.2,length=0.25)
             tip.rotate(angle).move_to(mid)
             return tip
        tip1 = middle_tip(D, C,D).shift(DOWN*0.01)
        tip2 = middle_tip(A,B,B, position=0.5).shift(UP*0.01)
        tip3 = middle_tip(A,D,D, position=0.45).shift(LEFT*0.025)
        tip4 = middle_tip(B,C,B, position=0.45).shift(RIGHT*0.025)
        def tick_mark(start, end, position=0.4, size=0.3):
             point = interpolate(start, end, position)
             direction = end - start
             unit_dir = direction / np.linalg.norm(direction)
             perp = np.array([-unit_dir[1], unit_dir[0], 0])
             return Line( point - perp * size/2.5, point + perp * size/2.5, color=BLACK, stroke_width=2)
        tick1 = tick_mark(A,D ,0.59)
        tick2 = tick_mark(A,D, 0.63)
        tick3 = tick_mark(B,C, 0.63)
        tick4 = tick_mark(B,C, 0.59)
        tick5 = tick_mark(A,B ,0.75)
        tick6 = tick_mark(D,C, 0.75)

        self.add(quad,AB, BC, CD, DA, label_A, label_B, label_C, label_D,tip1,tip2,tip3,tip4,tick1,tick2,tick3,tick4,tick5,tick6)