from manim import*
config.frame_height=10
config.frame_width=30
config.pixel_width=2800
config.pixel_height=2800

class Step_2(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        outer_box = Rectangle(width=12, height=6, color="#7E4071",stroke_width=4).set_fill("#F8F7C5",opacity=1)

        title1 = Tex(r"Urn-I", color=BLACK).scale(0.8).move_to(outer_box.get_top()+DOWN*0.5+LEFT*3)
        title2 = Tex(r"Urn-II", color=BLACK).scale(0.8).move_to(outer_box.get_top()+DOWN*0.5+RIGHT*3)
        A1 = MathTex(r"A_1", color=BLACK).scale(0.8).next_to(title1, DOWN, buff=0.2)
        A2 = MathTex(r"A_2", color=BLACK).scale(0.8).next_to(title2, DOWN, buff=0.2)

        box1 = Rectangle(width=4.2, height=3.2, color="#FF69AF",stroke_width=4).move_to(LEFT*3).set_fill("#FFBBDB",opacity=1)
        box2 = Rectangle(width=4.2, height=3.2, color="#FF69AF",stroke_width=4).move_to(RIGHT*3).set_fill("#FFBBDB",opacity=1)
        B1 = Tex("B :", color=BLACK).scale(0.6).next_to(box1, LEFT, buff=0.3)
        B2 = Tex("B :", color=BLACK).scale(0.6).next_to(box2, LEFT, buff=0.3)

        pA1 = MathTex(r"P(A_1)=\frac{1}{2}", color=BLACK).scale(0.7)
        pB1 = MathTex(r"P(2\,\text{red} | \text{urnI})", color=BLACK).scale(0.7)
        pB12 = MathTex(r"(or) ", color=BLACK).scale(0.7)
        pB3=MathTex(r"P(B|A_1)", color=BLACK).scale(0.7)
        pB5=MathTex(r"=\frac{^{8}C_{2}}{^{12}C_{2}}", color=BLACK).scale(0.7).next_to(pB12,LEFT).shift(DOWN*0.45+LEFT*0.8)
        text1 = VGroup(pA1, pB1,pB12,pB3).arrange(DOWN, buff=0.3)
        text1.move_to(box1.get_center())
        pA1.shift(LEFT*0.7)
        pB3.shift(LEFT*0.9)
        pB12.shift(LEFT*1.2)
        pB1.shift(LEFT*0.55)

        pA2 = MathTex(r"P(A_2)=\frac{1}{2}", color=BLACK).scale(0.7)
        pB2 = MathTex(r"P(2\,\text{red} | \text{urnII}) ", color=BLACK).scale(0.7)
        pB21 = MathTex(r"(or) ", color=BLACK).scale(0.7)
        pB4=MathTex(r"P(B|A_2)", color=BLACK).scale(0.7)
        pB6=MathTex(r"=\frac{^{5}C_{2}}{^{15}C_{2}}", color=BLACK).scale(0.7).next_to(pB21,LEFT).shift(DOWN*0.45+RIGHT*5.2)
        text2 = VGroup(pA2, pB2,pB21,pB4).arrange(DOWN, buff=0.3)
        text2.move_to(box2.get_center())
        pA2.shift(LEFT*0.7)
        pB4.shift(LEFT*0.9)
        pB21.shift(LEFT*1.2)
        pB2.shift(LEFT*0.55)

        labels_group = VGroup(
            MathTex(r"A_1 \rightarrow \text{Selecting urn-I}", color=BLACK).scale(0.7),
            MathTex(r"A_2 \rightarrow \text{Selecting urn-II}", color=BLACK).scale(0.7),
            MathTex(r"B \rightarrow \text{Selecting 2 red balls}", color=BLACK).scale(0.7),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(outer_box, RIGHT, buff=0.5)

        meet_point = DOWN*3
        line1 = Line(box1.get_bottom(), meet_point, color="#FF388B")
        line2 = Line(box2.get_bottom(), meet_point, color="#FF388B")
        arrow = Arrow(meet_point, meet_point + DOWN*1.5, color="#FF388B", buff=0,stroke_width=3.5)

        result_box = Rectangle(width=4, height=1.2, color="#7E4071",stroke_width=5)
        result_box.next_to(arrow, DOWN, buff=0.2).shift(UP*0.2).set_fill("#E6C0DE",opacity=1)
        result_text1 = Tex("2 Red ball = ?", color=BLACK).scale(0.7)
        result_text2 = Tex("P(B)", color=BLACK).scale(0.7)
        result_text = VGroup(result_text1, result_text2).arrange(DOWN, buff=0.1)
        result_text.move_to(result_box.get_center())
        
        self.add(outer_box,title1, title2,A1, A2,  B1,B2,labels_group,line1, line2,box1, box2,text1, text2,pB5,pB6,
                 result_box,result_text)