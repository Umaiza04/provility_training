from manim import*
config.frame_height=10
config.frame_width=15
config.pixel_width=2500
config.pixel_height=2500

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        rect = Rectangle(width=10, height=6)
        rect.set_fill("#e9bdd0", opacity=1)
        rect.set_stroke("#B2713D", width=5)

        curve = CubicBezier(
            LEFT*5 + DOWN*0.25,
            LEFT*2 + UP*3,
            RIGHT*2 + DOWN*3,
            RIGHT*5 + UP*0.2).set_color(BLACK).set_z_index(1)
        
        ellipse = Ellipse(width=5.8, height=4).rotate(25 * DEGREES).set_stroke(RED, width=6)
        top_mask = VMobject()
        top_mask.set_points_as_corners([rect.get_corner(UL), rect.get_corner(UR)])
        top_mask.add_line_to(curve.get_points()[-1]) 
        top_mask.append_points(curve.get_points()[::-1]) 
        top_mask.add_line_to(rect.get_corner(UL))
        bottom_mask = VMobject()
        bottom_mask.set_points_as_corners([rect.get_corner(DL), rect.get_corner(DR)])
        bottom_mask.add_line_to(curve.get_points()[-1])
        bottom_mask.append_points(curve.get_points()[::-1])
        bottom_mask.add_line_to(rect.get_corner(DL))
        top_fill = Intersection(ellipse, top_mask, fill_color="#a8e0ef", fill_opacity=0.7, stroke_width=0)
        bottom_fill = Intersection(ellipse, bottom_mask, fill_color="#EFEFC6", fill_opacity=0.7, stroke_width=0)
        ellipse.set_fill(opacity=0) 
        ellipse.set_stroke(RED, width=4)
        ellipse_outline = ellipse.copy().set_fill(opacity=0).set_stroke(1).set_color(RED)
        
        arrow = CurvedArrow(
            start_point=ellipse.get_bottom()+UP*0.05,
            end_point=ellipse.get_bottom()+DOWN*1.8,
            angle=-TAU/4,
            color=RED)
        
        S_label = MathTex("S", color=BLACK).scale(1.2).next_to(rect, UP, buff=0.15)
        label1 = MathTex("A_1", color=BLACK).scale(1.2).move_to(rect.get_corner(UL) + RIGHT*1.2 + DOWN*0.6)
        label2 = MathTex("A_2", color=BLACK).scale(1.2).move_to(rect.get_corner(DR) + LEFT*1.4 + UP*0.6)
        label3 = MathTex("A_1 \\cap B", color=BLACK).scale(1.5).set_z_index(1).move_to(UP*1 + RIGHT*0.8)
        label4 = MathTex("A_2 \\cap B", color=BLACK).scale(1.5).set_z_index(1).move_to(DOWN*1 + LEFT*0.8)
        B_label = MathTex("B", color=BLACK).scale(1.2).next_to(arrow.get_end(), DOWN).shift(LEFT*0.5+UP*0.3)

        self.add(rect, ellipse_outline,curve,arrow, S_label,label1,label2,label3,label4, B_label,top_fill,bottom_fill)