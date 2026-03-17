from manim import*
config.frame_height=10
config.frame_width=15
config.pixel_width=2800
config.pixel_height=2800

class Step_3(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        rectangle = Rectangle(width=10, height=6.5, stroke_color="#990F4B" , 
                         fill_color="#FFF9E5", fill_opacity=1, stroke_width=3)
        
        s_label = Text("U", color="black", font_size=45).next_to(rectangle, UR, buff=0.2).shift(LEFT*1)
    
        circle_1 = Circle(radius=2.4, stroke_color="#990F4B" , stroke_width=3,
                          fill_color="#FCE4EC" , fill_opacity=1).shift(LEFT * 1.3)
        
        circle_2 = Circle(radius=2.4, stroke_color="#990F4B" , stroke_width=3,
                          fill_color="#9ACDED" , fill_opacity=1).shift(RIGHT * 1.3)
        
        intersection = Intersection(circle_1, circle_2, stroke_width=0, 
                                    fill_color=WHITE , fill_opacity=1)
        
        label1 = Text("S", color="black", font_size=40).move_to(circle_1).shift(UP*2.7)
        label2 = Text("C", color="black", font_size=40).move_to(circle_2).shift(UP*2.7)
        
        label3 = MathTex(r"S \cap \overline{C}", color="black").scale(1.4).move_to(circle_1.get_center() + LEFT * 0.9)
        label4 = MathTex(r"\overline{S} \cap C", color="black").scale(1.4).move_to(circle_2.get_center() + RIGHT * 0.9)
        
        circle_i_outline = circle_1.copy().set_fill(opacity=0)
        circle_c_outline = circle_2.copy().set_fill(opacity=0)
        start_s = circle_1.get_top() + LEFT*0.2
        end_s = rectangle.get_top() + UP * 1 + LEFT * 2.5
        
        start_c = circle_2.get_top() + RIGHT*0.2
        end_c = rectangle.get_top() + UP * 1 + RIGHT * 2.5

        arrow_1 = CurvedArrow(start_s, end_s, color="#DF6625", angle=-TAU/12, tip_length=0.2)
        arrow_2 = CurvedArrow(start_c, end_c, color="#DF6625", angle=TAU/12, tip_length=0.2)
        
        label5 = Text("Only S", color="black", font_size=38).next_to(arrow_1.get_end(), LEFT, buff=0.1).shift(UP*0.3+RIGHT*0.6)
        label6 = Text("Only C", color="black", font_size=38).next_to(arrow_2.get_end(), RIGHT, buff=0.1).shift(UP*0.3+LEFT*0.6)
        label7 = Text("Only one of the two jobs",color="black", font_size=30).next_to(rectangle, DOWN)

        self.add(rectangle, s_label,label1, label2,label5,label6,arrow_1, arrow_2,circle_1, circle_2,label3, 
                 label4,intersection,circle_i_outline, circle_c_outline,label7) 
        
        
       
        
