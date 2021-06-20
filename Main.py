"""
Ayman Wahbani   209138155
Sapir Ezra      313546194
Moriel Turjeman 308354968
"""


import random
import tkinter.font
from tkinter import *
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import Transformations
from Transformations import parallel_projection, oblique_projections, perspective_projection
from Transformations import hide_show_all_lines
from Polygon import Point, Polygon
from ErrorHandler import display_error, display_info

# list of all the polygons we have, each polygon consists of either 3 or 4 points
list_Polygon = []

# Create the window
root = Tk()
root.title("Ex3- 3D Transformations and Projections")

# Produces a window the size of a user's screen
width: int = root.winfo_screenwidth()
height: int = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width, height))

# Set the background image
bg = Image.open("images/background.png")
resized = bg.resize((width, height), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(resized)
my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

# Variale for projection
type_Projection = StringVar()
type_Projection.set("Parallel Orthographic")

# Variable for axis
type_Axis = StringVar()
type_Axis.set("x")

# Variable for ZoomIn (n) and ZoomOut(1/n)
type_Size = StringVar()
type_Size.set("0")

# Variable for rotation angle
type_Angle = StringVar()
type_Angle.set("0")

# Variable for projection angle
type_Angle_proj = StringVar()
type_Angle_proj.set("40")

# title for the Option
type_Option = StringVar()
type_Option.set("")

'''
function: restart 
delete all shapes in canvas
'''

def help_me_file():
    # Method 2: Open with subprocess
    import subprocess
    path = 'help.pdf'
    subprocess.Popen([path], shell=True)

def restart():
    canvas.delete("all")
    canvas.create_rectangle(canvas_width, canvas_height, 2, 2, outline='blue')


def myDraw(list_poly: list):
    """Drawing the polygons to the screen using the chosen projection."""
    # restart all shape becuase we have new shapes
    restart()

    # choose projection
    if type_Projection.get() == "Parallel Orthographic":
        list_Polygon = parallel_projection(list_poly)
    elif type_Projection.get() == "Parallel Oblique":
        try:
            list_Polygon = oblique_projections(list_poly, int(type_Angle_proj.get()))
        except ValueError:  # כאשר אין מספר
            display_error("Must be a number for oblique project")
        except AttributeError:  # כאשר אין כלום
            display_error("Enter value for oblique projection")
    else:
        list_Polygon = perspective_projection(list_poly)

    # Draw each polygon
    for poly in list_Polygon:
        if not hide_show_all_lines(poly):  # for hiding hidden surfaces
            continue
        p1: Point = poly.getPoint(1)
        p2: Point = poly.getPoint(2)
        p3: Point = poly.getPoint(3)
        p4: Point = poly.getPoint(4)
        if p4 is not None:
            canvas.create_polygon([p1.getX() + 400, p1.getY() + 200,
                                   p2.getX() + 400, p2.getY() + 200,
                                   p3.getX() + 400, p3.getY() + 200,
                                   p4.getX() + 400, p4.getY() + 200],
                                  outline='blue', fill="#{:06x}".format(random.randint(0, 0xFFFFFF)), width=1)
        else:
            canvas.create_polygon([p1.getX() + 400, p1.getY() + 200,
                                   p2.getX() + 400, p2.getY() + 200,
                                   p3.getX() + 400, p3.getY() + 200],
                                  outline='blue', fill="#{:06x}".format(random.randint(0, 0xFFFFFF)), width=1)


def choose_option(s: str):
    """Choosing transformation."""
    if s == "rotate" or s == "scale":
        # for choose [x, y, z]
        if s == "rotate":
            type_Option.set("Rotate")
            # "Hides" all objects we do not use
            label_scale.place(x=-100, y=-100)
            entry_scale.place(x=-100, y=-100)
            # "Displays" all the objects we use in the desired location
            label_axis.place(x=1100, y=270)
            combobox_type_axis.place(x=1200, y=270)
            label_angle.place(x=1100, y=370)
            entry_angle.place(x=1100, y=400)
            button_ok.place(x=1200, y=500)
        elif s == "scale":
            type_Option.set("Scale")
            # "Hides" all objects we do not use
            label_axis.place(x=-100, y=-100)
            combobox_type_axis.place(x=-100, y=-100)
            label_angle.place(x=-100, y=-100)
            entry_angle.place(x=-100, y=-100)
            # "Displays" all the objects we use in the desired location
            label_scale.place(x=1100, y=270)
            entry_scale.place(x=1100, y=300)
            button_ok.place(x=1200, y=400)

        label_title_option.config(text=type_Option.get())

    # Activation of a particular cost
    if s == "ok":
        if type_Option.get() == "Rotate":
            rotate()
        elif type_Option.get() == "Scale":
            scale()

    pass


def rotate():
    global list_Polygon
    try:
        angle = float(entry_angle.get())
        if angle < 0 or angle > 180:
            display_info("Must be a number between 0 and 180")
        else:
            list_Polygon = Transformations.rotate(list_Polygon, angle, type_Axis.get())
            myDraw(list_Polygon)
    except ValueError as e:
        display_error("Must be number, no string")
    pass


def scale():
    global list_Polygon
    try:
        size = float(entry_scale.get())

        list_Polygon = Transformations.scale(list_Polygon, size, size, size)
        myDraw(list_Polygon)
    except ValueError:
        display_error("Must be number, no string")
    pass


def open_file():
    global root
    restart()
    list_polygon_cube = []
    list_point_cube = []
    list_polygon_pyramid = []
    list_point_pyramid = []
    try:
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        text_file = open(root.filename, "r")
    except FileNotFoundError:
        display_info("You have choose the correct file")
        return
    shape: str = None  # if cube or pyramid
    type_p: str = None  # polygon or point
    for line in text_file:
        count = 0
        list_number = []  # take all numbers in only line
        for x in line.split(','):
            if x == 'cube' or x == 'pyramid':
                shape = x
            elif x == 'polygon' or x == 'point':
                type_p = x
            elif line == 'cube,\n' or line == 'pyramid,\n' or line == 'polygon,\n' or line == 'point,\n':
                continue
            else:
                if x != '\n':
                    # take all numbers in line
                    list_number.append(int(x))
                elif shape == 'cube' and type_p == 'polygon':
                    list_polygon_cube.append(list_number)
                elif shape == 'cube' and type_p == 'point':
                    list_point_cube.append(list_number)
                elif shape == 'pyramid' and type_p == 'polygon':
                    list_polygon_pyramid.append(list_number)
                elif shape == 'pyramid' and type_p == 'point':
                    list_point_pyramid.append(list_number)

    # We have listPolygon and list point
    # So we want to create a class of list polygons
    for poligon_cube in list_polygon_cube:
        p1 = list_point_cube[poligon_cube[0] - 1]  # 1, 2, 4, 3
        p2 = list_point_cube[poligon_cube[1] - 1]
        p3 = list_point_cube[poligon_cube[2] - 1]
        p4 = list_point_cube[poligon_cube[3] - 1]
        poly = Polygon(Point(p1[0], p1[1], p1[2]), Point(p2[0], p2[1], p2[2]),
                       Point(p3[0], p3[1], p3[2]), Point(p4[0], p4[1], p4[2]))
        list_Polygon.append(poly)
    print(type(list_Polygon[0]))
    for poligon_pyramid in list_polygon_pyramid:
        p1 = list_point_pyramid[poligon_pyramid[0] - 1]  # 1, 2, 4, 3
        p2 = list_point_pyramid[poligon_pyramid[1] - 1]
        p3 = list_point_pyramid[poligon_pyramid[2] - 1]
        poly = Polygon(Point(p1[0], p1[1], p1[2]), Point(p2[0], p2[1], p2[2]),
                       Point(p3[0], p3[1], p3[2]))
        list_Polygon.append(poly)

    # We have now all list
    myDraw(list_Polygon)  # call myDraw to draw the polygons to the screen with our choices.


def ClickMe(event):
    myDraw(list_Polygon)
    print(type_Projection.get())


# Open Image for "open file" button.
open_file_btn = Image.open("images/open_file.png")
# Resize Image
resized = open_file_btn.resize((70, 70), Image.ANTIALIAS)
open_file_btn = ImageTk.PhotoImage(resized)

button_open_file = Button(root, image=open_file_btn, borderwidth=0, command=lambda: open_file())
button_open_file.place(x=10, y=10)


# Open Image for "open file help" button.
help_btn = Image.open("images/help.png")
# Resize Image
resized = help_btn.resize((70, 70), Image.ADAPTIVE)
help_btn = ImageTk.PhotoImage(resized)

button_help = Button(root, image=help_btn, borderwidth=0, command=lambda: help_me_file())
button_help.place(x=1200, y=10)


label_combobox = Label(root, text="Choose projection:", font='Ariel 12')
label_combobox.place(x=0, y=200)
# Dropdown menu for choosing projection
combobox_type = ttk.Combobox(root, values=["Parallel Orthographic",
                                           "Parallel Oblique",
                                           "Perspective Projection"], textvariable=type_Projection, state='readonly')
combobox_type.bind("<<ComboboxSelected>>", ClickMe)
combobox_type.place(x=15, y=230)

entry_angle_proj = Entry(root, textvariable=type_Angle_proj, width=10, bd=3).place(x=15, y=270)

button_proj = Button(root, text="Draw", command=lambda: myDraw(list_Polygon)).place(x=100, y=270)

# Open Image for "rotate" button.
rotate_btn = Image.open("images/rotate.png")
# Resize Image
resized = rotate_btn.resize((100, 60), Image.ANTIALIAS)
rotate_btn = ImageTk.PhotoImage(resized)

button_rotate = Button(root, image=rotate_btn, borderwidth=0, command=lambda: choose_option("rotate"))
button_rotate.place(x=15, y=300)

# Open Image for "scale" button.
scale_btn = Image.open("images/scale.png")
# Resize Image
resized = scale_btn.resize((100, 60), Image.ANTIALIAS)
scale_btn = ImageTk.PhotoImage(resized)

button_scale = Button(root, image=scale_btn, borderwidth=0, command=lambda: choose_option("scale"))
button_scale.place(x=15, y=400)

label_title_option = Label(root, text=type_Option.get(), font='Ariel 20')
label_title_option.place(x=1100, y=150)

label_axis = Label(root, text="Choose axis:", font='Ariel 12')
combobox_type_axis = ttk.Combobox(root, values=["x", "y", "z"], width=10, textvariable=type_Axis, state='readonly')

label_scale = Label(root, text="Enter scale size (to zoom):", font='Ariel 12')
entry_scale = Entry(root, textvariable=type_Size, width=10, bd=3)

label_angle = Label(root, text="Enter angle for rotation: (0 - 180)", font='Ariel 12')
entry_angle = Entry(root, textvariable=type_Angle, width=10, bd=3)

# Open Image for
ok_btn = Image.open("images/ok.png")
# Resize Image
resized = ok_btn.resize((50, 50), Image.ANTIALIAS)
ok_btn = ImageTk.PhotoImage(resized)

button_ok = Button(root, image=ok_btn, borderwidth=0, command=lambda: choose_option("ok"))

help_label_font = tkinter.font.Font(family="Ariel", size=12, underline=1)
help_label = Label(root, text="help", font=help_label_font, justify="left")
help_label.place(x=10, y=600)

help_str_2 = """To start, click the top left button to open a file.
Then, choose the desired projection: oblique, orthographic or perspective.
To scale the image, enter any value greater than 0 and click 'scale' and then click the green 'v' button.
To rotate the image, enter the rotation angle (0-180) and the rotation axis (x, y or z) and click the green 'v' button."""
help_text2 = Label(root, text=help_str_2, font='Ariel 8', justify="left")
help_text2.place(x=10, y=620)

canvas_width = 800
canvas_height = 500

canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='White')
canvas.place(x=250, y=100)
canvas.create_rectangle(canvas_width, canvas_height, 4, 4, outline='blue')
root.mainloop()
