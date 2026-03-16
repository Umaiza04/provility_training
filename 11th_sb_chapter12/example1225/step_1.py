from manim import*
config.frame_height=10
config.frame_width=30
config.pixel_width=2800
config.pixel_height=2800

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        rect = Rectangle(width=10, height=6)
        rect.set_fill("#F1F1D2", opacity=1)
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
        top_fill = Intersection(ellipse, top_mask, fill_color="#f1aed5", fill_opacity=0.7, stroke_width=0)
        bottom_fill = Intersection(ellipse, bottom_mask, fill_color="#d2abec", fill_opacity=0.7, stroke_width=0)
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
        diagram_group = VGroup(rect,curve,ellipse_outline,top_fill,bottom_fill,arrow,S_label,label1,label2,label3,label4,B_label)
        diagram_group.shift(LEFT*8.5)
        self.add(diagram_group)
        
        #diagram2
        outer_box = Rectangle(width=12, height=6, color="#FE46A5",stroke_width=5)

        label1 = Text("Factory", color=BLACK).scale(0.7).next_to(outer_box, UP, buff=0.2)
        A1 = Text("A1", color=BLACK).scale(0.6).move_to(outer_box.get_top() + DOWN*0.8 + LEFT*3)
        machine1 = Text("Machine I", color=BLACK).scale(0.6).next_to(A1, DOWN, buff=0.15)
        box1 = Rectangle(width=3, height=2, color="#7695E2",stroke_width=5).move_to(LEFT*3)
        p1 = Text("O/P : 40%", color=BLACK).scale(0.55)
        d1 = Text("Defective : 4%", color=BLACK).scale(0.55)
        text1 = VGroup(p1, d1).arrange(DOWN, buff=0.2).move_to(box1.get_center())

        A2 = Text("A2", color=BLACK).scale(0.6).move_to(outer_box.get_top() + DOWN*0.8 + RIGHT*3)
        machine2 = Text("Machine II", color=BLACK).scale(0.6).next_to(A2, DOWN, buff=0.15)
        box2 = Rectangle(width=3, height=2, color="#7695E2",stroke_width=5).move_to(RIGHT*3)
        p2 = Text("O/P : 60%", color=BLACK).scale(0.55)
        d2 = Text("Defective : 5%", color=BLACK).scale(0.55)
        text2 = VGroup(p2, d2).arrange(DOWN, buff=0.2).move_to(box2.get_center())

        label2 = Text("A1 \u2192 Item from Machine 1", color=BLACK).scale(0.5)
        label3 = Text("A2 \u2192 Item from Machine 2", color=BLACK).scale(0.5)
        label4 = Text("B \u2192 Selecting defective item", color=BLACK).scale(0.5)

        explanation = VGroup(label2,label3,label4).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(outer_box, RIGHT, buff=0.5)

        meet_point = DOWN*2.7
        line1 = Line(box1.get_bottom(), meet_point, color="#E49558").set_z_index(-1)
        line2 = Line(box2.get_bottom(), meet_point, color="#E49558").set_z_index(-1)
        arrow = Arrow(meet_point, meet_point + DOWN*1.5, buff=0, color="#E49558",stroke_width=3.5)

        result_box = Rectangle(width=4, height=1.2, color="#DE0C62")
        result_box.next_to(arrow, DOWN, buff=0.2).shift(UP*0.2)
        result_text1 = Text("Defective = ?", color=BLACK).scale(0.55)
        result_text2 = Text("P(B)", color=BLACK).scale(0.55)
        result_text = VGroup(result_text1, result_text2).arrange(DOWN, buff=0.1)
        result_text.move_to(result_box.get_center())
        B1 = Text("B :", color=BLACK).scale(0.6).next_to(box1, LEFT, buff=0.3)
        B2 = Text("B :", color=BLACK).scale(0.6).next_to(box2, LEFT, buff=0.3)

        factory_diagram = VGroup( outer_box,label1, A1, machine1, A2, machine2, box1, box2, text1, text2,
            explanation,line1, line2,arrow,result_box,result_text,B1,B2 ).shift(RIGHT*4)
        self.add(factory_diagram)