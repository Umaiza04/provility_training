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
        D = np.array([0, -2, 0])  
        triangle = Polygon(A, B, C, color="#A00498", stroke_width=4.5)
        #median
        AD = Line(A, D, color="#990F4B", stroke_width=4)
        DB = Line(D, B)
        DC = Line(D, C)
        right_angle_left = RightAngle( AD, DB,length=0.35, color="#990F4B", stroke_width=4, quadrant=(-1, -1)  )
        right_angle_right = RightAngle( AD, DC, length=0.35, color="#990F4B", stroke_width=4, quadrant=(-1, -1) )
        #labels
        labelA = Text("A", color=BLACK).scale(0.7).next_to(A, UP, buff=0.1)
        labelB = Text("B", color=BLACK).scale(0.7).next_to(B, DOWN+LEFT, buff=0.1)
        labelC = Text("C", color=BLACK).scale(0.7).next_to(C, DOWN+RIGHT, buff=0.1)
        labelD = Text("D", color=BLACK).scale(0.7).next_to(D, DOWN, buff=0.1)
        vector1 = MathTex(r"\vec{a}", color=BLACK).next_to(A,buff=0.3).shift(UP*0.25).scale(1)
        vector2 = MathTex(r"\vec{b}", color=BLACK).next_to(B,buff=0.3).shift(DOWN*0.75+LEFT*0.65).scale(1)
        vector3 = MathTex(r"\vec{c}", color=BLACK).next_to(C,buff=0.2).shift(DOWN*0.69+LEFT*0.08).scale(1)
        vector4 = MathTex(r"(\vec{d})", color=BLACK).next_to(D,buff=0.2).shift(DOWN*0.8+LEFT*0.5).scale(1)
        def middle_tip(start, end, face_point, position=0.5):
             mid = interpolate(start, end, position)
             direction = face_point - mid
             angle = angle_of_vector(direction)
             tip = StealthTip(color=BLACK,stroke_width=0.35,length=0.25)
             tip.rotate(angle).move_to(mid)
             return tip
        tip1 = middle_tip(A,B,B,position=0.55).shift(RIGHT*0.033)
        tip2 = middle_tip(A,D,D,position=0.55)
        tip3 = middle_tip(A,C,C,position=0.55).shift(LEFT*0.033)
        tip4=middle_tip(B,D,D,position=0.55)
        tip5=middle_tip(D,C,C,position=0.65)
        def tick_mark(start, end, position=0.4, size=0.3):
             point = interpolate(start, end, position)
             direction = end - start
             unit_dir = direction / np.linalg.norm(direction)
             perp = np.array([-unit_dir[1], unit_dir[0], 0])
             return Line( point - perp * size/2, point + perp * size/2, color=BLACK, stroke_width=3)
        tick1 = tick_mark(B,D ,0.30)
        tick2 = tick_mark(B,D, 0.34)
        tick3 = tick_mark(D,C, 0.40)
        tick4 = tick_mark(D,C, 0.44)
        self.add( AD,right_angle_left,right_angle_right,triangle,labelA, labelB, labelC, labelD,vector1,vector2,vector3,vector4,
                 tip1,tip2,tip3,tip4,tip5,tick1,tick2,tick3,tick4)