import simple_graphics as sg

def draw_picture(width, height):
    """Draws a static picture."""
    sg.set_fill_color("sky blue")
    sg.fill_rectangle(0, 0, width, height)
    sg.set_fill_color("white")
    sg.draw_cloud(100, 50, 40)
    sg.set_fill_color("white")
    sg.draw_cloud(300, 75, 40)
    sg.set_fill_color("white")
    sg.draw_cloud(500, 50, 40)


if __name__ == "__main__":
    # Launch the wrapper; only edit starting dimensions of canvas if you would like to
    sg.start(draw_picture, 600, 400)
