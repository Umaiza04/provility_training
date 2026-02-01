from manim import *
config.background_color=WHITE

class animation_task(Scene):
    def construct(self):
        bluedot=Dot([-2.2,-2,0],color= "#0343DF",z_index=10).scale(1.5)
        #left label
        label1=Text("left",color=BLACK).next_to(bluedot,DOWN).scale(0.7)
        reddot=Dot([2.2,-2,0],color="#FF000D",z_index=10).scale(1.5)
        #right label
        label2=Text("right",color=BLACK).next_to(reddot,DOWN).scale(0.7)
        blackdot1=Dot([0,-2,0],color=BLACK).scale(1.5) 
        blackdot2=Dot([0,2,0],color=BLACK).scale(1.5)
        #center label
        label3=Text("center",color=BLACK).next_to(blackdot2,UP).scale(0.7)
        #lines creation
        line1=Line(start=[-2.2,-2,0],end=[2.2,-2,0],color=BLACK).set_stroke(width=4)
        line2=always_redraw(lambda: Line(blackdot1.get_center(),end=blackdot2.get_center(),color=BLACK).set_stroke(width=4).add_tip())
        line3=always_redraw(lambda: Line(start=blackdot2.get_center(),end=bluedot.get_center(),color=BLACK).set_stroke(width=4))
        line4=always_redraw(lambda: Line(start=blackdot2.get_center(),end=reddot.get_center(),color=BLACK).set_stroke(width=4))
        #animation
        self.play(FadeIn(bluedot,label1)),self.play(FadeIn(reddot,label2))
        self.play(FadeOut(label1,label2))
        self.play(Create(line1))
        self.play(FadeIn(blackdot1))
        self.play(Create(line2),FadeIn(blackdot2))
        self.play(Create(line3)),self.play(Create(line4))
        self.play(blackdot2.animate.shift(DOWN*2.3)),self.play(blackdot2.animate.shift(UP*2.3))
        self.play(FadeIn(label1,label2,label3),FadeOut(line1,line2,blackdot1))
        self.wait(1)       

