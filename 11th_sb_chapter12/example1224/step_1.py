from manim import*
config.frame_height=10
config.frame_width=15
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
            include_outer_lines=False ).set_color(BLACK)
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