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
        triangle = Polygon(A, B, C, color="#BD6C48", stroke_width=4.5)
        D = interpolate(A, B, 0.5) 
        E = interpolate(A, C, 0.5)   
        DE = Line(D, E, color=BLACK)
        BE = Line(B, E, color=BLACK)
        CD = Line(C, D, color=BLACK)
        labelA = Text("A", color=BLACK).next_to(A, UP,buff=0.03).scale(0.6)
        labelB = Text("B", color=BLACK).next_to(B, DOWN, buff=0.03).scale(0.6)
        labelC = Text("C", color=BLACK).next_to(C, DOWN,buff=0.03).scale(0.6)
        labelD = Text("D", color=BLACK).next_to(D, LEFT,buff=0.05).scale(0.6)
        labelE = Text("E", color=BLACK).next_to(E, RIGHT,buff=0.07).scale(0.6)
        vector1 = MathTex(r"(\vec{a})", color=BLACK).next_to(A,buff=0.2).shift(UP*0.25)
        vector2 = MathTex(r"(\vec{b})", color=BLACK).next_to(B,buff=0.3).shift(DOWN*0.8+LEFT*0.6)
        vector3 = MathTex(r"(\vec{c})", color=BLACK).next_to(C,buff=0.2).shift(DOWN*0.75+LEFT*0.48)
        def middle_tip(start, end, face_point, position=0.5):
             mid = interpolate(start, end, position)
             direction = face_point - mid
             angle = angle_of_vector(direction)
             tip = StealthTip(color=BLACK,stroke_width=0.3,length=0.2)
             tip.rotate(angle).move_to(mid)
             return tip
        DE = Line(D, E, color="#9A3001", stroke_width=3.5)
        BE = Line(B, E, color="#9A3001", stroke_width=3.5)
        CD = Line(C, D, color="#9A3001", stroke_width=3.5)
        tip1 = middle_tip(D, E, E)
        tip2 = middle_tip(B, E, E, position=0.35).shift(DOWN*0.028)
        tip3 = middle_tip(C, D, C, position=0.35).shift(UP*0.03) 
        tip4 = middle_tip(A, D, D, position=0.4).shift(RIGHT*0.026)
        tip5 = middle_tip(B, D, B, position=0.7).shift(RIGHT*0.026)
        tip6 = middle_tip(A, E, E, position=0.4).shift(LEFT*0.026)
        tip7 = middle_tip(E, C, C, position=0.31).shift(LEFT*0.026)
        tip8 = middle_tip(B, C, C, position=0.5)
        def tick_mark(start, end, position=0.4, size=0.3):
             point = interpolate(start, end, position)
             direction = end - start
             unit_dir = direction / np.linalg.norm(direction)
             perp = np.array([-unit_dir[1], unit_dir[0], 0])
             return Line( point - perp * size/2, point + perp * size/2, color=BLACK, stroke_width=3)
        tick1 = tick_mark(A, D, 0.57)
        tick2 = tick_mark(A, D, 0.60)
        tick3 = tick_mark(B, D, 0.41)
        tick4 = tick_mark(B, D, 0.44)
        tick5 = tick_mark(A, E, 0.57)
        tick6 = tick_mark(E, C, 0.57)
        self.add(DE,BE,CD,triangle,labelA,labelB, labelC,labelD, labelE,tip1, tip2,tip3,tip4,tip5,tip6,tip7,tip8,
                 vector1,vector2,vector3,tick1,tick2,tick3,tick4,tick5,tick6)

