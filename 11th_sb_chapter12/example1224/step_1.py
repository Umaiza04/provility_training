from manim import*
config.frame_height=10
config.frame_width=30
config.pixel_width=2800
config.pixel_height=2800

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        data = [
            ["Urn-I","8","4","12"],
            ["Urn-II","5","10","15"],
            ["Total","13","14","27"]]

        col_labels = [
            Text("",color=BLACK),
            Text("Red\nballs",color=RED),
            Text("Blue\nballs",color=BLUE),
            Text("Total",color=BLACK)]

        table = Table(
            data,
            col_labels=col_labels,
            include_outer_lines=False ).set_color(BLACK).shift(LEFT*6)
        table.scale(1.2)
        border = SurroundingRectangle(table,color="#2d6ea3",buff=0)
        border.set_stroke(width=8)

        table.get_vertical_lines().set_color("#2d6ea3")
        table.get_horizontal_lines().set_color("#2d6ea3")

        table.get_vertical_lines().set_stroke(width=5)
        table.get_horizontal_lines().set_stroke(width=5)

        table.get_entries((2,2)).set_color("#056EEE")
        table.get_entries((3,2)).set_color("#056EEE")
        table.get_entries((4,2)).set_color("#056EEE")

        table.get_entries((2,1)).set_color("#CF0234")
        table.get_entries((3,1)).set_color("#CF0234")
        table.get_entries((4,1)).set_color("#CF0234")

        table.get_entries((2,3)).set_color("#742802")
        table.get_entries((3,3)).set_color("#742802")
        table.get_entries((4,3)).set_color("#742802")

        pink = "#f4c2c2"
        for c in range(1,5):
         table.add_highlighted_cell((1,c), color=pink)
         for r in range(1,5):
            table.add_highlighted_cell((r,1), color=pink)
            for r in range(1,5):
               table.add_highlighted_cell((3,c), color=pink)
               self.add(table,border)

        #diagram 2
        rect = Rectangle(width=10, height=6)
        rect.set_fill("#EFEFC6", opacity=1)
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
        top_fill = Intersection(ellipse, top_mask, fill_color="#a4e4b7", fill_opacity=0.7, stroke_width=0)
        bottom_fill = Intersection(ellipse, bottom_mask, fill_color="#e3c1c1", fill_opacity=0.7, stroke_width=0)
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
        diagram_group = VGroup(curve,rect,ellipse_outline,top_fill,bottom_fill,arrow,S_label,label1,label2,label3,label4,B_label)
        diagram_group.shift(RIGHT*7)
        self.add(diagram_group)
