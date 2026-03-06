from manim import *

config.frame_height = 7
config.frame_width = 36
config.pixel_width = 2800
config.pixel_height = 2800

class Question128(Scene):
    def construct(self):
        self.camera.background_color=WHITE
        q_image = ImageMobject("question.png")
        q_image.scale(2)
        self.add(q_image)