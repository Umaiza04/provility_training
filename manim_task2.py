from manim import *

config.frame_height=5
config.frame_width=10
config.pixel_width=1500
config.pixel_height=1500

class Shapes(Scene):
    def construct(self):
        self.camera.background_color=WHITE
        #circle creation
        circle=Circle(color="#9B5FC0").to_edge(UR).scale(1.0).shift(UP*0.3)
        label1=Text("Circle",color=BLACK,font_size=30).shift(RIGHT*3.5)
        #ellipse creation
        ellipse=Ellipse(color="#3D0734").shift(UP).scale(1.5)
        label2=Text("Ellipse",color=BLACK,font_size=30)
        #rectangle creation
        rectangle=Rectangle(width=4.0, height=2.0,color=RED).shift(DOWN*2)
        label3=Text("Rectangle",color=BLACK,font_size=30).shift(DOWN*3.5)
        #square creation
        square=Square(side_length=2,color="#DEEC15").to_edge(DL).shift(DOWN)
        label4=Text("Square",color=BLACK,font_size=30).to_edge(DL).shift(DOWN*1.5)
        #triangle creation
        triangle=Triangle(color="#533CC6").to_edge(UL).scale(1.3)
        label5=Text("Triangle",color=BLACK,font_size=30).shift(LEFT*3.5)
        #polygon creation
        polygon=Polygon([-4, 1.5, 0], [-2, 0.5, 0], [-2.5, -1, 0]).to_edge(DR).shift(DOWN*1.5)
        label6=Text("Polygon",color=BLACK,font_size=30).to_edge(DR,buff=0.1).shift(DOWN*1.7)
        self.add(circle,ellipse,rectangle,square,triangle,label1,label2,label3,label4,label5,polygon,label6)
