from manim import *
import numpy as np
config.background_color=WHITE
config.frame_height=7
config.frame_width=18
config.pixel_width=2500
config.pixel_height=2500
def axes_creation():
    axes = Axes(
        x_range=[-PI, PI, PI/2],
        y_range=[-4, 4, 1],
        x_length=4,
        y_length=4,
        axis_config={"color":BLACK,"include_tip":False } )
    #tick_labels
    x_labels = {-PI: MathTex("-\\pi",color=BLACK),
                -PI/2: MathTex("-\\frac{\\pi}{2}",color=BLACK),
                 PI/2: MathTex("\\frac{\\pi}{2}",color=BLACK),
                 PI: MathTex("\\pi",color=BLACK)}
    axes.add_coordinates(x_labels)
    return axes
class TrigonometricGraph(Scene):
    def construct(self):
        #sin graph
        axes = axes_creation().to_corner(UL,buff=0.3).shift(UP*4.2)
        graph1 = axes.plot(lambda x: np.sin(x), color=BLUE)
        label1 = MathTex("y=\\sin x",color=BLACK).to_edge(UL).scale(1.0).shift(DOWN+UP*1+RIGHT)
        self.add(axes, graph1, label1)
        #cos graph
        axes=axes_creation().to_corner(UR,buff=0.3).shift(UP*4.2)
        graph2=axes.plot(lambda x: np.cos(x), color=RED)
        label2 = MathTex("y=\\cos x", color=BLACK).to_edge(UR).scale(1.0).shift(UP+DOWN*1+LEFT)
        self.add(axes,graph2,label2)
        #tan graph
        axes = axes_creation().shift(UP*5.4)
        graph3 = axes.plot(lambda x: np.tan(x),x_range=[-PI/2 + 0.25, PI/2 - 0.25],color="#FE4B03" )
        label3 = MathTex("y=\\tan x",color=BLACK).shift(UP*3)
        self.add(axes, graph3, label3)
        #cot graph
        axes=axes_creation().to_corner(DL,buff=0.3)
        graph4=axes.plot(lambda x: 1/np.tan(x),x_range=[0.25, PI - 0.25], color=MAROON)
        label4=MathTex("y=\\cot",color=BLACK).shift(DOWN*4+LEFT*6)
        self.add(axes,graph4,label4)
        #sec graph
        axes=axes_creation().to_corner(DR,buff=0.3)
        graph5=axes.plot(lambda x: 1/np.cos(x), x_range=[-PI/2 + 0.2, PI/2 - 0.2], color=ORANGE)
        label5=MathTex("y=\\sec",color=BLACK).shift(DOWN*4+RIGHT*7)
        self.add(axes,graph5,label5)
        #cosec graph
        axes=axes_creation().shift(UP+DOWN*2.2)
        graph6 = axes.plot( lambda x: 1/np.sin(x) - 1, x_range=[0.2, PI - 0.2], color=PURPLE )
        label6=MathTex(r"y=\csc x",color=BLACK).shift(DOWN*3.8)
        self.add(axes,graph6,label6)
