from manim import*
config.frame_height=8
config.frame_width=20
config.pixel_width=2500
config.pixel_height=2500

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        A = np.array([0, 3, 0])
        B = np.array([-3, -2, 0])
        C = np.array([3, -2, 0])
        D = np.array([0, -2, 0])  
        F = A + 0.5 * (B - A)           
        E = A + 0.5 * (C - A)        
        triangle = Polygon(A, B, C, color="#C760FF", stroke_width=4.5)
        #median
        AD = Line(A, D, color="#FE01B1", stroke_width=4)
        BE = Line(B, E, color="#FE01B1", stroke_width=4)
        CF = Line(C, F, color="#FE01B1", stroke_width=4)
        #labels
        labelA = Text("A", color=BLACK).scale(0.7).next_to(A, UP, buff=0.1)
        labelB = Text("B", color=BLACK).scale(0.7).next_to(B, DOWN+LEFT, buff=0.1)
        labelC = Text("C", color=BLACK).scale(0.7).next_to(C, DOWN+RIGHT, buff=0.1)
        labelD = Text("D", color=BLACK).scale(0.7).next_to(D, DOWN, buff=0.1)
        labelF = MathTex("F", color=BLACK).scale(0.9).shift(LEFT*1.7+UP*0.6)
        labelE = MathTex("E", color=BLACK).scale(0.9).shift(RIGHT*1.75+UP*0.6)
        label_A = MathTex(r"(1,0,0)",color=BLACK).next_to(A, UP,buff=0.5).scale(0.8)
        label_B = MathTex(r"(0,1,0)",color=BLACK).next_to(B, DOWN,buff=0.7).shift(LEFT*0.1).scale(0.8)
        label_C = MathTex(r"(0,0,1)",color=BLACK).next_to(C, DOWN,buff=0.7).shift(RIGHT*0.2).scale(0.8)
        vector1 = MathTex(r"(\vec{a})", color=BLACK).next_to(A,buff=0.3).shift(UP*0.2).scale(1)
        vector2 = MathTex(r"(\vec{b})", color=BLACK).next_to(B,buff=0.3).shift(DOWN*0.38+LEFT*0.25).scale(1)
        vector3 = MathTex(r"(\vec{c})", color=BLACK).next_to(C,buff=0.2).shift(DOWN*0.35+RIGHT*0.3).scale(1)
        vector4 = MathTex(r"(\vec{d})", color=BLACK).next_to(D,buff=0.2).shift(DOWN*0.8+LEFT*0.5).scale(1)

        def middle_tip(start, end, face_point, position=0.5):
             mid = interpolate(start, end, position)
             direction = face_point - mid
             angle = angle_of_vector(direction)
             tip = StealthTip(color=BLACK,stroke_width=0.35,length=0.25)
             tip.rotate(angle).move_to(mid)
             return tip
        tip1 = middle_tip(A,B,B,position=0.6).shift(RIGHT*0.035)
        tip2 = middle_tip(A,C,C, position=0.6).shift(LEFT*0.035)
        tip3 = middle_tip(C, D, C, position=0.65) 
        tip4 = middle_tip(A, D, D, position=0.4)
        tip5 = middle_tip(C,F,F, position=0.4).shift(DOWN*0.04)
        tip6 = middle_tip(B,E,E, position=0.4).shift(DOWN*0.04)

        def tick_mark(start, end, position=0.4, size=0.3):
             point = interpolate(start, end, position)
             direction = end - start
             unit_dir = direction / np.linalg.norm(direction)
             perp = np.array([-unit_dir[1], unit_dir[0], 0])
             return Line( point - perp * size/2, point + perp * size/2, color=BLACK, stroke_width=3)
        tick1 = tick_mark(A,F ,0.47)
        tick2 = tick_mark(A,F, 0.51)
        tick3 = tick_mark(A,F, 0.55)
        tick4 = tick_mark(B,F, 0.47)
        tick5 = tick_mark(B,F ,0.51)
        tick6 = tick_mark(B,F, 0.55)
        tick7 = tick_mark(D,C, 0.50)
        tick8 = tick_mark(B,D, 0.46)
        tick9 = tick_mark(A,E ,0.50)
        tick10 = tick_mark(A,E, 0.46)
        tick11 = tick_mark(C,E, 0.50)
        tick12 = tick_mark(C,E, 0.46)

        rect = Rectangle(height=1, width=6,color=BLACK,stroke_width=1.5).shift(RIGHT * 5.5+UP*1)
        rect_text = MathTex( r"{AD},{BE},{CF}\ \rightarrow\ \text{Median}",color=BLACK,font_size=50).shift(RIGHT * 5.5+UP*1 )

        self.add( AD,BE,CF,triangle,labelA, labelB, labelC, labelD,labelF,labelE,label_A,label_B,label_C,vector1,vector2,vector3,vector4,
                 tip1, tip2,tip3,tip4,tip5,tip6,tick1,tick2,tick3,tick4,tick5,tick6,tick7,tick8,tick9,tick10,tick11,tick12,rect,rect_text)