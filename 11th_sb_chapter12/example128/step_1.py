from manim import*
config.frame_height=10
config.frame_width=15
config.pixel_width=2500
config.pixel_height=2500

class Step_1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        data = [
            ["1","1","2","2","3","3"],
            ["2","3","1","3","1","2"],
            ["3","2","3","1","2","1"]]

        col_labels = [
            MathTex("C_1"),
            MathTex("C_2"),
            MathTex("C_3"),
            MathTex("C_4"),
            MathTex("C_5"),
            MathTex("C_6"),]

        row_labels = [
            MathTex("A"),
            MathTex("B"),
            MathTex("C")]

        table = Table(
            data,
            col_labels=col_labels,
            row_labels=row_labels,
            include_outer_lines=True,
            line_config={"color": "#7E4071", "stroke_width": 5},)
        table.get_entries().set_color(BLACK)
        table.scale(0.9)
        table.move_to(ORIGIN)

        for r in range(2,5):
            for c in range(2,8):
                if c % 2 == 1:
                    table.add_highlighted_cell((r,c), color="#f3e6a0")
                else:
                    table.add_highlighted_cell((r,c), color="#c9dfd1")

        label1= Text("Outcomes", font_size=42,color=BLACK).next_to(table, UP, buff=0.4)
        label2= Text("Envelope", font_size=42,color=BLACK).rotate(PI/2).next_to(table, LEFT, buff=0.6)

        self.add(label1, label2, table)