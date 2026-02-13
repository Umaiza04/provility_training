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
        #labels
        labelA = Text("A", color=BLACK).scale(0.7).next_to(A, UP, buff=0.1)
        labelB = Text("B", color=BLACK).scale(0.7).next_to(B, DOWN+LEFT, buff=0.1)
        labelC = Text("C", color=BLACK).scale(0.7).next_to(C, DOWN+RIGHT, buff=0.1)
        labelD = Text("D", color=BLACK).scale(0.7).next_to(D, DOWN, buff=0.1)
        self.add( AD,triangle,labelA, labelB, labelC, labelD)