from tkinter import *

from tkinter import filedialog, ttk

import time

import math

from math import sqrt

import numpy as np

import Transformations
from Transformations import parallel_projection,oblique_projections,perspective_projection

from Polygon import Vertex, Polygon
#כאשר מחזירים את ההטלה ממקבילית לאלכסונית
# אנחנו שנינו את הנקודות על פי סוג ההטלה
# אז איך מחזירים?
#וגם כאשר עושים סיבוב או זום או משהו מהפעולות גם ישנה את הDATA
# original data
vertex_table_cube = [] #vertex
polygon_table_cube = [] # polygon

vertex_table_pyramid = None  #vertex
polygon_table_pyramid = None  # polygon

# parallel_projection data # הטלה מקבילית


# perspective_projection

mousePoints = []
points = []
normals = []
root = Tk()
visibilitys=[]
viewDistance = np.array([0,0,-500])
root.title("Erez Geva ID:066062712")
lamda=45

distance= StringVar()
distance.set("-500")

mySelect = StringVar()
myMessage = StringVar()
type_Projection = StringVar()
type_Projection.set("Parallel Orthographic")

rotateAngle = StringVar()
rotateAngle.set("0.5")
rotateAxis = StringVar()
rotateAxis.set("x")

scaleSize = StringVar()
scaleSize.set("2")

def deleteAll():
    pass

def myDraw(s: str, polygon_table, vertex_table):
    global polygon_table_cube, polygon_table_pyramid
    global vertex_table_cube, vertex_table_pyramid
    # type_Projection משתנה תמיד לפי הבחירה שלי
    if s == "cube" and type_Projection.get() == "Parallel Orthographic":
        #מחזיר לנו את הנקודות החדשות לאחר בחירת ההטלה
        points = parallel_projection(vertex_table)

        for polygon in polygon_table:
            if len(polygon) == 4:
                p1 = points[polygon[0] - 1]  # 1, 2, 4, 3
                p2 = points[polygon[1] - 1]
                p3 = points[polygon[2] - 1]
                p4 = points[polygon[3] - 1]
                w.create_polygon([p1[0] + 400, p1[1] + 200 ,  # x,y
                                  p2[0] + 400, p2[1] + 200,
                                  p3[0] + 400, p3[1] + 200,
                                  p4[0] + 400, p4[1] + 200],
                                 outline='blue', fill='white', width=1)

    elif s == "cube" and type_Projection.get() == "Parallel Oblique":
        # מחזיר לנו את הנקודות החדשות לאחר בחירת ההטלה
        points = oblique_projections(vertex_table)
        for polygon in polygon_table:
            if len(polygon) == 4:
                p1 = points[polygon[0] - 1]  # 1, 2, 4, 3
                p2 = points[polygon[1] - 1]
                p3 = points[polygon[2] - 1]
                p4 = points[polygon[3] - 1]
                w.create_polygon([p1[0] + 400, p1[1] + 200,  # x,y
                                  p2[0] + 400, p2[1] + 200,
                                  p3[0] + 400, p3[1] + 200,
                                  p4[0] + 400, p4[1] + 200],
                                 outline='blue', fill='white', width=1)

    elif s == "cube" and type_Projection.get() == "Perspective Projection": pass
    #אמר אפשר לקחת את הDATA שהוא נתן אותה
    if s == "pyramid" and type_Projection.get() == "Parallel Orthographic":
        points = parallel_projection(vertex_table)
        for polygon in polygon_table:
            if len(polygon) == 3:
                # points = [[1,2,3],[2,4,5],[5,6,6],[4,5,6]]
                # polygon= [1,2,4,3]

                p1 = points[polygon[0] - 1]  # 1, 2, 4, 3
                p2 = points[polygon[1] - 1]
                p3 = points[polygon[2] - 1]

                # draw 3D in 2D
                # את הפוליגון רק על ידי נקודות
                w.create_polygon([p1[0] + 400, p1[1] + 200,  # x,y
                                  p2[0] + 400, p2[1] + 200,
                                  p3[0] + 400, p3[1] + 200], outline='blue',
                                 fill='white', width=1)
    elif s == "pyramid" and type_Projection.get() == "Parallel Oblique":
        pass
    elif s == "pyramid" and type_Projection.get() == "Perspective Projection":
        pass


def changeDistance():
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
    # we have create cube and pyramid
    create_shape("cube", list_polygon_cube,list_point_cube)
    create_shape("pyramid", list_polygon_pyramid, list_point_pyramid)
    myDraw("cube",list_polygon_cube,list_point_cube)
    myDraw("pyramid", list_polygon_pyramid, list_point_pyramid)
    pass

def myEvent(event):
    pass

def myMain(s: str): pass


# selectChangeView1 = Button(root, text="Parallel Orthographic", command=lambda: setView("Parallel Orthographic"))
# selectChangeView1.grid(row=3, column=0)
#
# selectChangeView2 = Button(root, text="Parallel Oblique", command=lambda: setView("Parallel Oblique"))
# selectChangeView2.grid(row=3, column=1)
#
# selectChangeView3 = Button(root, text="Perspective Projection", command=lambda: setView("Perspective Projection"))
# selectChangeView3.grid(row=3, column=2)

# כאש אני משנה את בחירתי לסוג ההטלה מופעלת הפונקציה
def ClickMe(event):
    #מסירי את מה שמופיע ומצייר אחת חדש לפי סוג ההטלה
    #deleteAll()
    #myDraw("cube"), myDraw("pyramid")
    print(type_Projection.get())

labelTop = Label(root, text = "Choose type to projection")
labelTop.grid(row=0,column=0)

comboExample = ttk.Combobox(root, values=["Parallel Orthographic", "Parallel Oblique","Perspective Projection"], textvariable= type_Projection)
comboExample.bind("<<ComboboxSelected>>", ClickMe)
comboExample.grid(row=0, column=1)
selectRotateB = Button(root, text="Click Me", command=lambda: ClickMe(type_Projection.get()))
selectRotateB.grid(row=0, column=2)

selectRotateB = Button(root, text="Rotate Shapes  (need axis x/y/z and angle in Radians)", command=lambda: Transformations.rotate_x_axis())
selectRotateB.grid(row=4, column=0)
selectRotateL = Label(root, text="Enter Angle in Radiance:")
selectRotateL.grid(row=4, column=1)
selectRotateE = Entry(root, textvariable=rotateAngle)
selectRotateE.grid(row=4, column=2)
selectRotateL = Label(root, text="Enter Rotate Axis:")
selectRotateL.grid(row=4, column=3)
selectRotateE = Entry(root, textvariable=rotateAxis)
selectRotateE.grid(row=4, column=4)

selectScaleB = Button(root, text="Scale(need point of rafarance and sclae)", command=lambda: Transformations.scale())
selectScaleB.grid(row=5, column=0)
selectScaleL = Label(root, text="Enter Scale:")
selectScaleL.grid(row=5, column=1)
selectScaleE = Entry(root, textvariable=scaleSize)
selectScaleE.grid(row=5, column=2)

selectScaleB = Button(root, text="Change View Distance (for perspective play)", command=lambda: changeDistance())
selectScaleB.grid(row=6, column=0)
selectScaleL = Label(root, text="Enter Distance:")
selectScaleL.grid(row=6, column=1)
selectScaleE = Entry(root, textvariable=distance)
selectScaleE.grid(row=6, column=2)


saveB = Button(root, text="file save", command=lambda: save_to_file())
saveB.grid(row=2, column=4)

openB = Button(root, text="file open", command=lambda: open_file())
openB.grid(row=2, column=5)

canvas_width = 800
canvas_height = 500

w = Canvas(root, width=canvas_width, height=canvas_height)
w.grid(row=11, columnspan=9, sticky=W)
w.bind("<Button-1>", myEvent)
w.create_rectangle(canvas_width, canvas_height, 2, 2, outline='red')
message = Label(root, textvariable=myMessage)
message.grid(row=10, columnspan=4, sticky=W)
root.after(10, myMain(''))
root.mainloop()
