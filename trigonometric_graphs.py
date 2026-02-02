from manim import *
import numpy as np
config.background_color=WHITE
config.frame_height=7
config.frame_width=18
config.pixel_width=2500
config.pixel_height=2500
def axes_creation():
    axes = Axes(
        x_range=[-1*PI, 1*PI, PI/2],
        y_range=[-2, 2, 1],
        x_length=4,
        y_length=2,
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
        axes = axes_creation().to_corner(UL,buff=0.3).shift(UP*4)
        graph1 = axes.plot(lambda x: np.sin(x), color=BLUE)
        label1 = MathTex("y=\\sin x",color=BLACK).to_edge(UL).scale(1.0).shift(UP*1.8)
        self.add(axes, graph1, label1)
        #cos graph
        axes=axes_creation().to_corner(UR,buff=0.3).shift(UP*4)
        graph2=axes.plot(lambda x: np.cos(x), color=RED)
        label2 = MathTex("y=\\cos x", color=BLACK).to_edge(UR).scale(1.0).shift(UP*1.8)
        self.add(axes,graph2,label2)
        #tan graph
        axes = axes_creation().shift(UP*6.3)
        graph3 = axes.plot(lambda x: np.tan(x),x_range=[-PI/3, PI/3],color="#FE4B03" )
        label3 = MathTex("y=\\tan x",color=BLACK).shift(UP*4.5)
        self.add(axes, graph3, label3)