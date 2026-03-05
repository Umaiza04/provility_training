from manim import*
config.frame_height=10
config.frame_width=15
config.pixel_width=2800
config.pixel_height=2800

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        rectangle = Rectangle(width=9, height=5.5, stroke_color="#8D6E63" , 
                         fill_color="#FFF9E5", fill_opacity=1, stroke_width=3)
        s_label = Text("S", color="black", font_size=45).next_to(rectangle, UP, buff=0.2)
    
        circle_1 = Circle(radius=2.0, stroke_color="#8D6E63" , stroke_width=3,
                          fill_color="#FFF9C4" , fill_opacity=1).shift(LEFT * 1.3)
        
        circle_2 = Circle(radius=2.3, stroke_color="#8D6E63" , stroke_width=3,
                          fill_color="#E8F5E9" , fill_opacity=1).shift(RIGHT * 1.3)
        
        intersection = Intersection(circle_1, circle_2, stroke_width=0, 
                                    fill_color="#FCE4EC" , fill_opacity=1)
        
        label1 = Text("I", color="black", font_size=40).move_to(rectangle.get_corner(UL) + RIGHT * 0.6 + DOWN * 0.6)
        label2 = Text("C", color="black", font_size=40).move_to(rectangle.get_corner(UR) + LEFT * 0.6 + DOWN * 0.6)
        
        label3 = MathTex(r"I \cap \overline{C}", color="black").scale(1.4).move_to(circle_1.get_center() + LEFT * 0.8)
        label4 = MathTex(r"\overline{I} \cap C", color="black").scale(1.4).move_to(circle_2.get_center() + RIGHT * 0.7)
        
        start_i = circle_1.get_bottom() + RIGHT * 0.5 + UP * 0.06
        end_i = rectangle.get_bottom() + DOWN * 0.5 + LEFT * 2.5
        
        start_c = circle_2.get_bottom() + LEFT * 0.5 + UP * 0.055
        end_c = rectangle.get_bottom() + DOWN * 0.5 + RIGHT * 2.5

        arrow_1 = CurvedArrow(start_i, end_i, color="#8D6E63", angle=-TAU/12, tip_length=0.2)
        arrow_2 = CurvedArrow(start_c, end_c, color="#8D6E63", angle=TAU/12, tip_length=0.2)
        
        label5 = Text("Only I", color="black", font_size=38).next_to(arrow_1.get_end(), LEFT, buff=0.1)
        label6 = Text("Only C", color="black", font_size=38).next_to(arrow_2.get_end(), RIGHT, buff=0.1)
        circle_i_outline = circle_1.copy().set_fill(opacity=0)
        circle_c_outline = circle_2.copy().set_fill(opacity=0)

        self.add(rectangle, s_label,circle_1, circle_2,intersection,circle_i_outline, circle_c_outline,
                 label1, label2, label3, label4,arrow_1, arrow_2, label5, label6) 
        
        
       
        
