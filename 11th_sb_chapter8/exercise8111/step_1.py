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
        triangle = Polygon(A, B, C, color="#C14A09", stroke_width=4.5)
        #median
        AD = Line(A, D, color="#990F4B", stroke_width=4)
        BE = Line(B, E, color="#990F4B", stroke_width=4)
        CF = Line(C, F, color="#990F4B", stroke_width=4)
        #labels
        labelA = Text("A", color=BLACK).scale(0.7).next_to(A, UP, buff=0.1)
        labelB = Text("B", color=BLACK).scale(0.7).next_to(B, DOWN+LEFT, buff=0.1)
        labelC = Text("C", color=BLACK).scale(0.7).next_to(C, DOWN+RIGHT, buff=0.1)
        labelD = Text("D", color=BLACK).scale(0.7).next_to(D, DOWN, buff=0.1)
        labelF = MathTex("F", color=BLACK).scale(0.9).shift(LEFT*1.7+UP*0.6)
        labelE = MathTex("E", color=BLACK).scale(0.9).shift(RIGHT*1.75+UP*0.6)
        self.add( AD,BE,CF,triangle,labelA, labelB, labelC, labelD,labelF,labelE)
      