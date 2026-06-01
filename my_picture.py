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

    # draw mountain
    sg.set_fill_color("#0096FF")
    sg. fill_triangle(400, 200, 500, 100, 600, 200)
    sg.set_fill_color("#0096FF")
    sg. fill_triangle(200, 200, 300, 50, 400, 200)
    sg.set_fill_color("#0096FF")
    sg. fill_triangle(0, 200, 100, 100, 200, 200)
    
    sg.set_fill_color("#FFFFFF")
    sg. fill_triangle(460, 140, 500, 100, 540, 140)
    sg.set_fill_color("#FFFFFF")
    sg. fill_triangle(274, 90, 300, 50, 326, 90)
    sg.set_fill_color("#FFFFFF")
    sg. fill_triangle(60, 140, 100, 100, 140, 140)
    
    sg.set_fill_color("#0096FF")
    sg. fill_rectangle(0, 200, 600, 200)

if __name__ == "__main__":
    # Launch the wrapper; only edit starting dimensions of canvas if you would like to
    sg.start(draw_picture, 600, 400)
