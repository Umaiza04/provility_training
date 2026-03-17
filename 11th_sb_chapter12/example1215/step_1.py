from manim import*
config.frame_height=10
config.frame_width=15
config.pixel_width=2800
config.pixel_height=2800

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        rectangle = Rectangle(width=10, height=6.5, stroke_color="#8D6E63" , 
                         fill_color="#FFF9E5", fill_opacity=1, stroke_width=3)
        
        s_label = Text("U", color="black", font_size=45).next_to(rectangle, UR, buff=0.2).shift(LEFT*1)
    
        circle_1 = Circle(radius=2.4, stroke_color="#8D6E63" , stroke_width=3,
                          fill_color="#FFF9C4" , fill_opacity=1).shift(LEFT * 1.3)
        
        circle_2 = Circle(radius=2.4, stroke_color="#8D6E63" , stroke_width=3,
                          fill_color="#E8F5E9" , fill_opacity=1).shift(RIGHT * 1.3)
        
        intersection = Intersection(circle_1, circle_2, stroke_width=0, 
                                    fill_color="#FCE4EC" , fill_opacity=1)
        
        label1 = Text("S", color="black", font_size=40).move_to(circle_1).shift(UP*2.7)
        label2 = Text("C", color="black", font_size=40).move_to(circle_2).shift(UP*2.7)
        
        label3 = MathTex("0.12", color="black").scale(1.4).move_to(circle_1.get_center() + LEFT * 0.8)
        label4 = MathTex("0.25", color="black").scale(1.4).move_to(circle_2.get_center() + RIGHT * 0.7)
        label5 = MathTex("0.07", color="black").scale(1.4).move_to(intersection.get_center())
        
        circle_i_outline = circle_1.copy().set_fill(opacity=0)
        circle_c_outline = circle_2.copy().set_fill(opacity=0)

        self.add(rectangle, s_label,circle_1, circle_2,intersection,circle_i_outline, circle_c_outline,
                 label1, label2, label3, label4,label5) 
        
        
       
        
