from manim import *
config.frame_height=12
config.frame_width=15
config.pixel_width=2500
config.pixel_height=2500
class axes_creation(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        #axes creation without using axes()
        x_axis = Line(start=LEFT * 6, end=RIGHT * 6, color=BLACK)
        y_axis = Line(start=DOWN * 6, end=UP * 6, color=BLACK)
        x_axis.add_tip(),x_axis.add_tip(at_start=True)
        y_axis.add_tip(),y_axis.add_tip(at_start=True)
        #labels creation
        label_1=MathTex("X",color=BLACK).shift(RIGHT*6.5)
        label_2=MathTex("Y",color=BLACK).shift(UP*6.5)
        label_3=MathTex("Y'",color=BLACK).shift(DOWN*6.5)
        label_4=MathTex("X'",color=BLACK).shift(LEFT*6.5) 
        dot=Dot(ORIGIN,color=BLACK).scale(1.2)
        #x-axis tick creation
        tick_1 = Line([-1, -0.15, 0], [-1, 0.15, 0], color=BLACK)
        tick_2 = Line([-2, -0.15, 0], [-2, 0.15, 0], color=BLACK)
        tick_3 = Line([-3, -0.15, 0], [-3, 0.15, 0], color=BLACK)
        tick_4 = Line([-4, -0.15, 0], [-4, 0.15, 0], color=BLACK)
        tick_5 = Line([-5, -0.15, 0], [-5, 0.15, 0], color=BLACK)
        tick_6 = Line([1, -0.15, 0], [1, 0.15, 0], color=BLACK)
        tick_7 = Line([2, -0.15, 0], [2, 0.15, 0], color=BLACK)
        tick_8 = Line([3, -0.15, 0], [3, 0.15, 0], color=BLACK)
        tick_9 = Line([4, -0.15, 0], [4, 0.15, 0], color=BLACK)
        tick_10 = Line([5, -0.15, 0], [5, 0.15, 0], color=BLACK)
        #y-axis tick creation
        tick_11 = Line([-0.15, -1, 0], [0.15,-1, 0], color=BLACK)
        tick_12 = Line([-0.15, -2, 0], [0.15,-2 , 0], color=BLACK)
        tick_13 = Line([-0.15, -3, 0], [0.15,-3, 0], color=BLACK)
        tick_14 = Line([-0.15, -4, 0], [0.15,-4, 0], color=BLACK)
        tick_15 = Line([-0.15, -5, 0], [0.15,-5, 0], color=BLACK)
        tick_16 = Line([-0.15, 1, 0], [0.15,1, 0], color=BLACK)
        tick_17 = Line([-0.15, 2, 0], [0.15,2, 0], color=BLACK)
        tick_18 = Line([-0.15, 3, 0], [0.15,3, 0], color=BLACK)
        tick_19 = Line([-0.15, 4, 0], [0.15,4, 0], color=BLACK)
        tick_20 = Line([-0.15, 5, 0], [0.15,5, 0], color=BLACK)
        self.add(x_axis, y_axis,label_1,label_2,label_3,label_4,tick_1,tick_2,tick_3,tick_4,tick_5,tick_6,tick_7,tick_8,tick_9,tick_10,dot,
                 tick_11,tick_12,tick_13,tick_14,tick_15,tick_16,tick_17,tick_18,tick_19,tick_20)
