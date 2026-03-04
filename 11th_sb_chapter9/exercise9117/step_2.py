from manim import*
config.frame_height=10
config.frame_width=35
config.pixel_width=2800
config.pixel_height=2800

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[-2.5*np.pi, 2.8*np.pi, np.pi/2],
            y_range=[-4, 4, 1],
            x_length=11,
            y_length=10,
            axis_config={"include_tip":False,
                         "color": BLACK,
                         "stroke_width": 4 }, ) 
        axes.y_axis.shift(RIGHT*0.09)
        axes.scale(1.6)
        axes.shift(LEFT*7.5+UP*2.5)
        axes_origin = MathTex("0", color=BLACK).scale(0.7).next_to(axes.c2p(0, 0), DOWN+RIGHT, buff=0.15).shift(UP*0.02)
        axes.x_axis.get_tick_marks()[9].set_opacity(0)
        axes.y_axis.get_tick_marks()[0].set_opacity(0)
        axes.y_axis.get_tick_marks()[1].set_opacity(0)
        axes.y_axis.get_tick_marks()[2].set_opacity(0)
        axes.y_axis.get_tick_marks()[3].set_opacity(0)
        axes.y_axis.get_tick_marks()[4].set_opacity(0)
        axes.y_axis.get_tick_marks()[5].set_opacity(0)
        axes.y_axis.get_tick_marks()[6].set_opacity(0)
        axes.y_axis.get_tick_marks()[7].set_opacity(0)
        axes.x_axis.get_tick_marks()[0].set_opacity(0)
        axes.x_axis.get_tick_marks()[7].set_opacity(0)
        axes.x_axis.get_tick_marks()[8].set_opacity(0)
        axes.x_axis.get_tick_marks()[6].shift(RIGHT*0.255)
        axes.x_axis.get_tick_marks()[5].shift(RIGHT*0.1)
        axes.x_axis.get_tick_marks()[1].shift(LEFT*0.1)
        axes.x_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        axes.x_axis.add_tip(at_start=False,tip_length=0.35,tip_width=0.25)
        axes.y_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        axes.y_axis.add_tip(at_start=False,tip_length=0.35,tip_width=0.25)
        xticks = [ -2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi ]
       
        xtick_labels = [
            MathTex("-2\\pi", color=BLACK),
            MathTex("-\\frac{3\\pi}{2}", color=BLACK),
            MathTex("-\\pi", color=BLACK),
            MathTex("-\\frac{\\pi}{2}", color=BLACK),
            MathTex("\\frac{\\pi}{2}", color=BLACK),
            MathTex("\\pi", color=BLACK),]
        xlabels = VGroup()
        for x, label in zip(xticks, xtick_labels):
            label.scale(0.7)
            label.next_to(axes.coords_to_point(x, 0), DOWN)
            xlabels.add(label)
        x_label = MathTex("x", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT).scale(1)
        y_label = MathTex("y", color=BLACK).next_to(axes.y_axis.get_end(), UP).scale(1)
        x_label1 = MathTex("x'", color=BLACK).next_to(axes.x_axis.get_start(), LEFT).scale(1)
        y_label1= MathTex("y'", color=BLACK).next_to(axes.y_axis.get_start(), DOWN).scale(1)
        
        sin_curve = axes.plot( lambda x: 1.5*np.sin(x),x_range=[-2.1*np.pi, -0],color="#CF0234")
        end_point = sin_curve.get_start()
        micro_tip = ArrowTriangleFilledTip(length=0.2, width=0.15, color="#CF0234")
        micro_tip.move_to(end_point).rotate(PI/2.5)
        sin_curve.add(micro_tip)
        label1 = MathTex("f(x)=\\sin x", color=BLACK).next_to(axes.coords_to_point(-0.7*np.pi, -2.3), LEFT,buff=0.0001).rotate(-PI/2.6).shift(UP*6+RIGHT*0.3)
       
        p = 1.7
        shift=0.1
        cos_curve2 = axes.plot(lambda x: 2 * ((1 - np.cos(x+shift)) / 2) ** p, x_range=[0, np.pi],color="#166725")
        dot = Dot(axes.coords_to_point(np.pi, 2),color="#CF0234")
        label2 = MathTex("f(x)=1-\\cos x", color=BLACK).next_to(axes.coords_to_point(np.pi/2, 3), RIGHT).rotate(PI/3).shift(DOWN*3.4+LEFT*2)
       
        x_shift = 0.08
        cos_curve = axes.plot(lambda x: np.cos(x),x_range=[np.pi + x_shift, 2.5*np.pi],color="#056EEE").shift(UP*0.05)
        end_point = cos_curve.get_end()
        micro_tip = ArrowTriangleFilledTip(length=0.2, width=0.15, color="#056EEE")
        micro_tip.move_to(end_point).rotate(PI/1.5).shift(UP*0.05+LEFT*0.027)
        cos_curve.add(micro_tip)
        dot1 = Dot(axes.coords_to_point(np.pi, -1),color="#CF0234").shift(UP*0.05)
        vertical_dash = DashedLine(start=axes.coords_to_point(np.pi, 2),end=axes.c2p(PI, 0),color="#AC4F06",dash_length=0.11,stroke_width=4).set_z_index(-1)
        zero_plus = MathTex(r"0^+",color=BLACK).scale(0.8).move_to(axes.c2p(-1.8, 0.8)).shift(DOWN*4+RIGHT*0.3)
        zero_minus = MathTex(r"0^-",color=BLACK).scale(0.8).move_to(axes.c2p(0.2, 0.45)).shift(DOWN*3.35+RIGHT*0.2)
        pi_plus = MathTex("\\pi^+",color=BLACK).scale(0.8).move_to(axes.c2p(-1.8, 0.8)).shift(DOWN*4+RIGHT*4)
        pi_minus = MathTex("\\pi^-",color=BLACK).scale(0.8).move_to(axes.c2p(0.2, 0.45)).shift(DOWN*3.35+RIGHT*4)
        label3 = MathTex("f(x)=\\cos x", color=BLACK).move_to(axes.coords_to_point(1.6*np.pi, -2.2)).shift(UP*6).rotate(PI/3.3)
        arrow1 = Arrow(start=axes.coords_to_point(-2.3, -1.0),
                      end=axes.coords_to_point(-0.8, -1.0),
                      buff=0,
                      stroke_width=6,
                      color="#AC4F06",
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.25)
        
        arrow2 = Arrow(start=axes.coords_to_point(-0.7, -1.0),
                      end=axes.coords_to_point(0.7, -1.0),
                      buff=0,
                      stroke_width=6,
                      color="#AC4F06",
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.3).rotate(PI/-1)
        
        arrow3 = Arrow(start=axes.coords_to_point(4.8, -1.0),
                      end=axes.coords_to_point(3.4, -1.0),
                      buff=0,
                      stroke_width=6,
                      color="#AC4F06",
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.3)
        
        arrow4 = Arrow(start=axes.coords_to_point(1.6, -1.0),
                      end=axes.coords_to_point(3.0, -1.0),
                      buff=0,
                      stroke_width=6,
                      color="#AC4F06",
                      tip_length=0.3,
                      max_tip_length_to_length_ratio=0.3)
        
        self.add(sin_curve,cos_curve2,cos_curve,axes,x_label, y_label,xlabels,zero_minus,zero_plus,x_label1,y_label1,
                 dot,label1,label2,label3,dot1,vertical_dash, pi_plus, pi_minus,arrow1,arrow2,arrow3,arrow4,axes_origin)
        
        #sin graph
        axes2 = Axes(
            x_range=[-2.5 * PI, 3.7 * PI, PI / 2],
            y_range=[-2.5, 2.5, 1],
            x_length=10,
            y_length=6,
            axis_config={"include_tip": True, "color": BLACK, "stroke_width": 3,"tip_length":0.35,"tip_width":0.25},
            tips=True,
            y_axis_config={"include_numbers":True,"font_size":28,"color":BLACK} )
        axes2.y_axis.shift(RIGHT*0.2)
        axes2.x_axis.get_tick_marks()[9].set_opacity(0)
        axes2.x_axis.get_tick_marks()[10].set_opacity(0)
        axes2.x_axis.get_tick_marks()[1].set_opacity(0)
        axes2.x_axis.get_tick_marks()[0].set_opacity(0)
        axes2.x_axis.get_tick_marks()[2].set_opacity(0)
        axes2.x_axis.get_tick_marks()[4].set_opacity(0)
        axes2.x_axis.get_tick_marks()[5].set_opacity(0)
        axes2.x_axis.get_tick_marks()[7].set_opacity(0)
        axes2.x_axis.get_tick_marks()[3].shift(LEFT*0.05)
        axes2.x_axis.get_tick_marks()[6].shift(RIGHT*0.03)
        axes2.x_axis.get_tick_marks()[8].shift(RIGHT*0.1)
        axes2.y_axis.get_tick_marks()[0].set_opacity(0)
        axes2.y_axis.get_tick_marks()[3].set_opacity(0)
        axes2.y_axis.get_tick_marks()[1].shift(DOWN*0.25)
        axes2.y_axis.get_tick_marks()[2].shift(DOWN*0.1)
        axes2.shift(RIGHT*9.2+DOWN*4)
        axes2.add_coordinates({
            
            -PI: MathTex("-\\pi", color=BLACK).scale(0.7),
            PI: MathTex("\\pi", color=BLACK).scale(0.7),
            2*PI: MathTex("2\\pi", color=BLACK).scale(0.7)
        })
        x_label = MathTex("x", color=BLACK).next_to(axes2.x_axis.get_end(), RIGHT).scale(1)
        y_label = MathTex("y", color=BLACK).next_to(axes2.y_axis.get_end(), UP).scale(1)
        x_label1 = MathTex("x'", color=BLACK).next_to(axes2.x_axis.get_start(), LEFT).scale(1)
        y_label3= MathTex("y'", color=BLACK).next_to(axes2.y_axis.get_start(), DOWN).scale(1)
        
        axes2.x_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        axes2.y_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        y_label1 = MathTex("1", color=BLACK).scale(0.6).next_to(axes2.c2p(0, 1), LEFT, buff=0.2)
        y_label2 = MathTex("-1", color=BLACK).scale(0.6).next_to(axes2.c2p(0, -1), LEFT, buff=0.2)
        sin_origin = MathTex("0", color=BLACK).scale(0.7).next_to(axes2.c2p(0, 0), DOWN+RIGHT, buff=0.15).shift(UP*0.02)
        
        sine_full = axes2.plot(lambda x: 1*np.sin(x),x_range=[-2.5*PI, 3.5*PI], color="#CF0234", stroke_width=4)
        end_point = sine_full.get_start()
        micro_tip = ArrowTriangleFilledTip(length=0.15, width=0.16, color="#1F2A7C")
        micro_tip.move_to(end_point).shift(UP*0.01)
        sine_full.add(micro_tip)
        end_point = sine_full.get_end()
        micro_tip = ArrowTriangleFilledTip(length=0.15, width=0.16, color="#1F2A7C")
        micro_tip.move_to(end_point).rotate(PI).shift(UP*0.01)
        sine_full.add(micro_tip)
        sine_label = MathTex("f(x) = \\sin x", color=BLACK).scale(0.8).next_to(axes2.c2p(-PI, 1), UP).shift(RIGHT*5.5)
        sin_dash_up = DashedLine(axes2.c2p(-2.5*PI, 1), axes2.c2p(3.4*PI, 1), color="#AF6F09",stroke_width=4).set_z_index(-1)
        sin_dash_down = DashedLine(axes2.c2p(-2.5*PI, -1), axes2.c2p(3.4*PI, -1), color="#AF6F09",stroke_width=4).set_z_index(-1)

        sin_dashed_lines = VGroup()
        labels = ["-\\frac{3\\pi}{2}", "-\\frac{\\pi}{2}", "\\frac{\\pi}{2}", "\\frac{3\\pi}{2}"]
        for x,tex in zip ([-1.5*PI, -0.5*PI, 0.5*PI, 1.5*PI],labels):
            y_val = np.sin(x)
            line = DashedLine(
                start=axes2.c2p(x, 0), 
                end=axes2.c2p(x, np.sin(x)), 
                color="#056EEE", 
                stroke_width=4,
                dash_length=0.15)
            label = MathTex(tex, color=BLACK).scale(0.7)
            direction = UP if y_val > 0 else DOWN
            label.next_to(line.get_end(), direction, buff=0.1)
            sin_dashed_lines.add(line,label)
            sin_group = VGroup(axes2, sine_full,sine_label,sin_dash_up,sin_dash_down,
                               sin_dashed_lines,y_label1,y_label2,sin_origin,x_label,x_label1,y_label,y_label3).scale(1.1)
            self.add(sin_group)

         
        #cos graph
        axes3 = Axes(
            x_range=[-2 * PI, 3 * PI, PI / 2],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=6,
            axis_config={"include_tip": True,"tip_length":0.35,"tip_width":0.25, "color": BLACK, "stroke_width": 3},
            tips=True
        ).shift(RIGHT * 10+UP*8)
        axes3.add_coordinates({
            -3*np.pi/2: MathTex("-\\frac{3\\pi}{2}", color=BLACK).scale(0.7),
            -PI/2: MathTex("-\\frac{\\pi}{2}", color=BLACK).scale(0.7),
            PI/2: MathTex("\\frac{\\pi}{2}", color=BLACK).scale(0.7),
            3*np.pi/2: MathTex("\\frac{3\\pi}{2}", color=BLACK).scale(0.7)
        })
        axes3.x_axis.get_tick_marks()[2].set_opacity(0)
        axes3.x_axis.get_tick_marks()[5].set_opacity(0)
        axes3.x_axis.get_tick_marks()[7].set_opacity(0)
        axes3.x_axis.get_tick_marks()[8].set_opacity(0)
        axes3.x_axis.get_tick_marks()[1].shift(LEFT*0.31)
        axes3.x_axis.get_tick_marks()[3].shift(LEFT*0.25)
        axes3.x_axis.get_tick_marks()[4].shift(LEFT*0.19)
        axes3.x_axis.get_tick_marks()[6].shift(LEFT*0.13)
        axes3.x_axis.get_tick_marks()[0].set_opacity(0)
        axes3.y_axis.get_tick_marks()[0].set_opacity(0)
        axes3.y_axis.get_tick_marks()[1].shift(DOWN*0.28)
        axes3.y_axis.get_tick_marks()[2].shift(DOWN*0.11)
        axes3.x_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        axes3.y_axis.add_tip(at_start=True,tip_length=0.35,tip_width=0.25)
        x_label = MathTex("x", color=BLACK).next_to(axes3.x_axis.get_end(), RIGHT).scale(1)
        y_label = MathTex("y", color=BLACK).next_to(axes3.y_axis.get_end(), UP).scale(1)
        x_label1 = MathTex("x'", color=BLACK).next_to(axes3.x_axis.get_start(), LEFT).scale(1)
        y_label3= MathTex("y'", color=BLACK).next_to(axes3.y_axis.get_start(), DOWN).scale(1)

        cosine_full = axes3.plot(lambda x: 1*np.cos(x),x_range=[-2*PI, 2.487*PI], color="#056EEE", stroke_width=4)
        end_point = cosine_full.get_start()
        micro_tip = ArrowTriangleFilledTip(length=0.15, width=0.16, color="#1F2A7C")
        micro_tip.move_to(end_point)
        cosine_full.add(micro_tip)
        end_point = cosine_full.get_end()
        micro_tip = ArrowTriangleFilledTip(length=0.15, width=0.16, color="#1F2A7C")
        micro_tip.move_to(end_point).rotate(PI/1.7)
        cosine_full.add(micro_tip)

        y_label1 = MathTex("1", color=BLACK).scale(0.6).next_to(axes3.c2p(0, 1), LEFT, buff=0.2)
        y_label2 = MathTex("-1", color=BLACK).scale(0.6).next_to(axes3.c2p(0, -1), LEFT, buff=0.2)
        cosin_origin = MathTex("0", color=BLACK).scale(0.7).next_to(axes3.c2p(0, 0), DOWN+RIGHT, buff=0.15).shift(UP*0.02)
        cosine_label = MathTex("f(x) = \\cos x", color=BLACK).scale(0.8).next_to(axes3.c2p(PI, -1), UP).shift(UP*3.3+RIGHT*2)
        cos_dash_up = DashedLine(axes3.c2p(-1.9*PI, 1), axes3.c2p(2.5*PI, 1), color="#AF6F09",stroke_width=4).set_z_index(-1)
        cos_dash_down = DashedLine(axes3.c2p(-1.9*PI, -1), axes3.c2p(2.5*PI, -1), color="#AF6F09",stroke_width=4).set_z_index(-1)
        cos_dashed_lines = VGroup()
        cos_x_vals = [-PI, PI, 2*PI]
        cos_labels_tex = ["-\\pi", "\\pi", "2\\pi"]
        for x, tex in zip(cos_x_vals, cos_labels_tex):
            y_val = np.cos(x) 
            line = DashedLine(
                start=axes3.c2p(x, 0), 
                end=axes3.c2p(x, y_val), 
                color="#CF0234", 
                stroke_width=4,
                dash_length=0.15 )
            label = MathTex(tex, color=BLACK).scale(0.7)
            direction = UP if y_val > 0 else DOWN
            label.next_to(line.get_end(), direction, buff=0.1)
            cos_dashed_lines.add(line, label)
            cos_graph_group = VGroup(axes3,cosine_full,cosine_label,cos_dash_up,cos_dash_down,cos_dashed_lines,y_label2,y_label1,cosin_origin,
                                     x_label,x_label1,y_label,y_label3).scale(1.1)
            self.add(cos_graph_group)
        
        