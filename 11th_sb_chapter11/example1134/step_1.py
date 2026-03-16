from manim import*
config.frame_height=8
config.frame_width=10
config.pixel_width=2500
config.pixel_height=2500

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
       
        A = LEFT * 4.5 + DOWN * 2    
        B = RIGHT * 2 + DOWN * 2  
        C = RIGHT * 2 + UP * 1.5   
        triangle = Polygon(A, B, C, color="#DF6625")

        label1 = MathTex("1",color=BLACK).next_to(Line(A, B), DOWN, buff=0.2).shift(DOWN*0.5)
        label2 = MathTex("x",color=BLACK).next_to(Line(B, C), RIGHT, buff=0.2).shift(RIGHT*0.5)
        label3 = MathTex(r"\sqrt{1+x^2}",color=BLACK).move_to((A + C) / 2 + UP * 1.3 + RIGHT*1)
        label4 = Text("Hypotenuse", color=BLACK).scale(0.45).next_to(label3, LEFT, buff=0.2).rotate(PI/6.3).shift(DOWN*1.3+RIGHT*0.3)
        label5 = Text("Adjacent", color=BLACK).scale(0.45).next_to(label1, UP, buff=0.2)
        label6 = Text("Opposite", color=BLACK).scale(0.45).next_to(label2, UP, buff=0.2)

        angle = Angle(Line(A, B), Line(A, C), radius=0.8, color=BLACK).set_z_index(-1)
        theta = MathTex(r"\theta",color=BLACK).next_to(angle, RIGHT, buff=0.3).shift(UP*0.09)
        right_angle = RightAngle(Line(B,C), Line(A,B), length=0.4, color=BLACK).rotate(PI/2).shift(LEFT*0.4).set_z_index(-1)

        self.add(triangle,label1,label2,label3, angle, theta,label4,label5,label6,right_angle )