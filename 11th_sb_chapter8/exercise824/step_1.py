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
        label_A = MathTex(r"(1,0,0)",color=BLACK).next_to(A, UP,buff=0.4).scale(0.8)
        label_B = MathTex(r"(0,1,0)",color=BLACK).next_to(B, DOWN,buff=0.5).shift(LEFT*0.1).scale(0.8)
        label_C = MathTex(r"(0,0,1)",color=BLACK).next_to(C, DOWN,buff=0.5).shift(RIGHT*0.2).scale(0.8)
        self.add( AD,BE,CF,triangle,labelA, labelB, labelC, labelD,labelF,labelE,label_A,label_B,label_C)