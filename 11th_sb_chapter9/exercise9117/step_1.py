from turtle import fillcolor
from manim import*
config.frame_height=10
config.frame_width=15
config.pixel_width=2500
config.pixel_height=2500

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[-2.5*np.pi, 2.7*np.pi, np.pi/2],
            y_range=[-4, 4, 1],
            x_length=12,
            y_length=7,
            axis_config={"include_tip": True,
                         "color": BLACK,
                         "stroke_width": 3,"tip_length": 0.35,
                         "tip_width": 0.25, },
            y_axis_config={"numbers_to_include": [-1,-2,-3, 1, 2, 3],
                           "decimal_number_config": {
                           "num_decimal_places": 0,
                           "color": BLACK, },  }, ) 
        axes.x_axis.get_tick_marks()[9].set_opacity(0)
        axes.y_axis.get_tick_marks()[0].set_opacity(0)
        axes.x_axis.get_tick_marks()[0].set_opacity(0)
        xticks = [ -2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi ]
        #labels creation
        xtick_labels = [
            MathTex("-2\\pi", color=BLACK),
            MathTex("-\\frac{3\\pi}{2}", color=BLACK),
            MathTex("-\\pi", color=BLACK),
            MathTex("-\\frac{\\pi}{2}", color=BLACK),
            MathTex("\\frac{\\pi}{2}", color=BLACK),
            MathTex("\\pi", color=BLACK),
            MathTex("\\frac{3\\pi}{2}", color=BLACK),
            MathTex("2\\pi", color=BLACK),]
        xlabels = VGroup()
        for x, label in zip(xticks, xtick_labels):
            label.scale(0.7)
            label.next_to(axes.coords_to_point(x, 0), DOWN)
            xlabels.add(label)
        x_label = Text("x", color=BLACK).next_to(axes.x_axis.get_end(), RIGHT).scale(1)
        y_label = Text("y", color=BLACK).next_to(axes.y_axis.get_end(), UP).scale(1)
        #sin curve
        sin_curve = axes.plot( lambda x: np.sin(x),x_range=[-2.1*np.pi, 0],color="#751973").insert_n_curves(100)
        label1 = MathTex("f(x)=\\sin x", color=BLACK).next_to(axes.coords_to_point(-0.7*np.pi, -2.3), LEFT)
        #1-cos(x)
        p = 1.55
        shift=0.2
        cos_curve2 = axes.plot(lambda x: 2 * ((1 - np.cos(x+shift)) / 2) ** p, x_range=[0, np.pi],color="#D90166")
        dot = Dot(axes.coords_to_point(np.pi, 2),color=BLACK)
        label2 = MathTex("f(x)=1-\\cos x", color=BLACK).next_to(axes.coords_to_point(np.pi/2, 3), RIGHT)
        #cos curve
        x_shift = 0.08  
        cos_curve = axes.plot(lambda x: np.cos(x),x_range=[np.pi + x_shift, 2.5*np.pi],color="#015482")
        circle = Circle(radius=0.06, color=BLACK).move_to(axes.coords_to_point(np.pi, -1)).set_z_index(1)
        label3 = MathTex("f(x)=\\cos x", color=BLACK).move_to(axes.coords_to_point(1.6*np.pi, -2.2)).shift(LEFT*0.5+UP*0.5)
        #arrow creation
        arrow1 = Arrow(start=LEFT*0.3,end=RIGHT * 0.1,  buff=0,stroke_width=3, tip_length=0.15,  color=BLACK).shift(DOWN*2.05+LEFT*1.7)
        arrow2 = Arrow(start=RIGHT*0.3,end=LEFT * 0.1,  buff=0,stroke_width=3, tip_length=0.15,  color=BLACK).shift(DOWN*2.05+LEFT*5)
        
        self.add(sin_curve,cos_curve2,cos_curve,axes,x_label, y_label,xlabels,
                 dot,circle,label1,label2,label3,arrow1,arrow2)
