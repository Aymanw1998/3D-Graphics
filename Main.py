import random
from tkinter import *

from tkinter import filedialog, ttk

from PIL import Image, ImageTk

import Transformations

from Transformations import parallel_projection, oblique_projections, perspective_projection

from Transformations import rotate, scale, hide_show_all_lines

from Polygon import Point, Polygon

list_Polygon = [] # list have all Polygon [class] and each polygon has Point [class]

# Create a window
root = Tk()
root.title("Ex3- 3D in 2D")

# width and height will preserve the length and width of your computer screen
width: int = root.winfo_screenwidth()
height: int = root.winfo_screenheight()

# Gives the window the length and width of the screen
root.geometry("%dx%d+0+0" % (width, height))

# Open Image
bg = Image.open("images/background.png")
# Resize Image
resized = bg.resize((width,height), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(resized)

my_label = Label(root, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

mySelect = StringVar()
myMessage = StringVar()

type_Projection = StringVar()
type_Projection.set("Parallel Orthographic")

type_Axis = StringVar()
type_Axis.set("x")

type_Size = StringVar()
type_Size.set("0")

type_Option = StringVar()
type_Option.set("Title:")
def deleteAll():
    canvas.delete("all")
    canvas.create_rectangle(canvas_width, canvas_height, 2, 2, outline='blue')
    #canvas.update()

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

def myDraw(list_poly: list):
    deleteAll()
    if type_Projection.get() == "Parallel Orthographic":
        list_Polygon = parallel_projection(list_poly)
    elif type_Projection.get() == "Parallel Oblique":
        list_Polygon = oblique_projections(list_poly) #list_poly
    else:
        list_Polygon = perspective_projection(list_poly)

    for poly in list_Polygon:
        if not hide_show_all_lines(poly):
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
                                   outline='blue', fill= "#{:06x}".format(random.randint(0, 0xFFFFFF)), width=1)


def choose_opction(s: str):
    if s == "rotate" or s == "scale":
        # for choose [x, y, z]
        label_axis.place(x=1100, y=270)
        combobox_type_axis.place(x=1200, y=270)
        if s == "rotate":
            type_Option.set("Rotate")
            label_scale.place(x=-100, y=-100)
            entry_scale.place(x=-100, y=-100)
            label_angle.place(x=1100, y=370)
            entry_angle.place(x=1100, y=400)
        elif s == "scale":
            type_Option.set("Scale")
            label_angle.place(x=-100, y=-100)
            entry_angle.place(x=-100, y=-100)
            label_scale.place(x=1100, y=370)
            entry_scale.place(x=1100, y=400)

        label_title_option.config(text= type_Option.get())
        button_ok.place(x=1200, y=500)

    if s == "ok":
        if type_Option.get() == "Rotate":
            rotate()
        elif type_Option.get() == "Scale":
            scale()


    pass

def rotate():
    global list_Polygon
    try:
        angle = int(entry_angle.get())
        if angle < 0 or angle > 180:
            print()
        else:
            list_Polygon = Transformations.rotate(list_Polygon, angle, type_Axis.get())
            myDraw(list_Polygon)
    except ValueError as e:
        print()
    pass

def scale():
    global list_Polygon
    try:
        size = float(entry_scale.get())
        list_Polygon = Transformations.scale(list_Polygon, size, size, size)
        myDraw(list_Polygon)
    except ValueError:
        print()
    pass

def save_to_file():
    pass

def create_shape(name,list_polygon, list_point):
    global polygon_table_cube, polygon_table_pyramid
    global vertex_table_cube, vertex_table_pyramid
    if name == 'cube':
        vertex_table_cube = list_point  #vertex
        polygon_table_cube = list_polygon  # polygon
    else:
        vertex_table_pyramid = list_point # points
        polygon_table_pyramid = list_polygon  # polygon

def open_file():
    global root
    global poligons
    global points

    list_polygon_cube = []
    list_point_cube = []
    list_polygon_pyramid = []
    list_point_pyramid = []
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    text_file = open(root.filename, "r")
    shape: str = None # if cube or pyramid
    type_p: str = None # polygon or point
    for line in text_file:
        count = 0
        list_number = [] # take all numbers in only line
        for x in line.split(','):
            if x == 'cube' or x == 'pyramid':
                shape = x
            elif x == 'polygon' or x == 'point':
                type_p = x
            elif line == 'cube,\n' or line == 'pyramid,\n' or  line == 'polygon,\n' or line == 'point,\n':
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

    for poligon_cube in list_polygon_cube:
        p1 = list_point_cube[poligon_cube[0] - 1]  # 1, 2, 4, 3
        p2 = list_point_cube[poligon_cube[1] - 1]
        p3 = list_point_cube[poligon_cube[2] - 1]
        p4 = list_point_cube[poligon_cube[3] - 1]
        poly = Polygon(Point(p1[0], p1[1], p1[2]),Point(p2[0], p2[1], p2[2]),
                       Point(p3[0], p3[1], p3[2]),Point(p4[0], p4[1], p4[2]))
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
    myDraw(list_Polygon)
    pass



def ClickMe(event):
    myDraw(list_Polygon)
    print(type_Projection.get())

# Open Image
open_file_btn = Image.open("images/open_file.png")
# Resize Image
resized = open_file_btn.resize((70,70), Image.ANTIALIAS)
open_file_btn = ImageTk.PhotoImage(resized)

button_open_file = Button(root, image= open_file_btn, borderwidth=0,command=lambda: open_file())
button_open_file.place(x=10, y=10)


label_combobox = Label(root, text = "Choose type to projection:", font='Ariel 12')
label_combobox.place(x=0, y=200)

combobox_type = ttk.Combobox(root, values=["Parallel Orthographic",
                                           "Parallel Oblique",
                                           "Perspective Projection"], textvariable= type_Projection)
combobox_type.bind("<<ComboboxSelected>>", ClickMe)
combobox_type.place(x=15, y=230)


# Open Image
rotate_btn = Image.open("images/rotate.png")
# Resize Image
resized = rotate_btn.resize((100,60), Image.ANTIALIAS)
rotate_btn = ImageTk.PhotoImage(resized)

button_rotate = Button(root, image= rotate_btn, borderwidth=0,command=lambda: choose_opction("rotate"))
button_rotate.place(x=15, y=300)

# Open Image
scale_btn = Image.open("images/scale.png")
# Resize Image
resized = scale_btn.resize((100,60), Image.ANTIALIAS)
scale_btn = ImageTk.PhotoImage(resized)

button_scale = Button(root, image= scale_btn, borderwidth=0,command=lambda: choose_opction("scale"))
button_scale.place(x=15, y=400)



label_title_option = Label(root, text = type_Option.get(), font='Ariel 20')
label_title_option.place(x=1100, y=150)

label_axis = Label(root, text="Choose axis:", font='Ariel 12')
combobox_type_axis = ttk.Combobox(root, values=["x", "y","z"], width= 10, textvariable= type_Axis, state='readonly')

label_scale = Label(root, text="Entry number size (to zoom):", font='Ariel 12')
entry_scale = Entry(root, textvariable= type_Size, width=10, bd=3)

label_angle = Label(root, text="Entry number angle: (0 - 180)", font='Ariel 12')
entry_angle = Entry(root, textvariable= "90", width=10, bd=3)

# Open Image
ok_btn = Image.open("images/ok.png")
# Resize Image
resized = ok_btn.resize((50,50), Image.ANTIALIAS)
ok_btn = ImageTk.PhotoImage(resized)

button_ok = Button(root, image= ok_btn, borderwidth=0,command=lambda: choose_opction("ok"))



canvas_width = 800
canvas_height = 500

canvas = Canvas(root, width=canvas_width, height=canvas_height, bg='White')
canvas.place(x=250, y=100)
canvas.create_rectangle(canvas_width, canvas_height, 4, 4, outline='blue')
message = Label(root, textvariable=myMessage)
message.grid(row=10, columnspan=4)
root.mainloop()
