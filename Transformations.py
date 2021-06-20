import math
import numpy as np
from math import sin, cos
from Polygon import Point, Polygon
from ErrorHandler import display_error


def distance(list_poly):
    first_x = list_poly[0].getPoint(1).getX()
    first_y = list_poly[0].getPoint(1).getY()
    first_z = list_poly[0].getPoint(1).getZ()

    max_x: float = first_x
    min_x: float = first_x

    max_y: float = first_y
    min_y: float = first_y

    max_z: float = first_z
    min_z: float = first_z

    for poly in list_poly:
        list_p = []
        for i in range(len(poly)):
            p = poly.getPoint(i + 1)
            x_p = p.getX()
            y_p = p.getY()
            z_p = p.getZ()

            # min and max x
            if x_p < min_x:
                min_x= x_p
            if x_p > max_x:
                max_x= x_p

            # min and max y
            if y_p < min_y:
                min_y= y_p
            if y_p > max_y:
                max_y= y_p

            # min and max z
            if z_p < min_z:
                min_z = z_p
            if z_p > max_z:
                max_z = z_p

            dis_x = math.dist([max_x], [min_x])
            dis_y = math.dist([max_y], [min_y])
            dis_z = math.dist([max_z], [min_z])

            return [dis_x, dis_y, dis_z]

def hide_show_all_lines(poly):
    p1: Point = poly.getPoint(1)
    p2: Point= poly.getPoint(2)
    p3: Point = poly.getPoint(3)
    p4: Point = poly.getPoint(4)

    normal = ((p2.getX() - p1.getX()) * (p1.getY() - p3.getY())) - ((p2.getY() - p1.getY())*(p1.getX() - p3.getX()))

    if normal <= 0:
        return True
    return False
################# Transformations######################
def parallel_projection(list_poly: list, angle=40):
    new_list_poly = []
    cos_number: float = math.cos(math.radians(45))/2
    sin_number: float = math.sin(math.radians(45))/2

    const_matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [cos_number, sin_number, 0, 0], [0, 0, 0, 1]]

    for poly in list_poly:
        list_p = []
        for i in range(len(poly)):
            p: Point = poly.getPoint(i+1)
            p_matrix = [p.getX(), p.getY(), p.getZ(), 1]
            result = np.dot(np.array(p_matrix), np.array(const_matrix))
            new_p = Point(result[0], result[1], result[2])
            list_p.append(new_p)
            if i + 1 == len(poly):
                if i + 1 == 4:
                    new_list_poly.append(Polygon(list_p[0], list_p[1], list_p[2], list_p[3]))
                elif i + 1 == 3:
                    new_list_poly.append(Polygon(list_p[0], list_p[1], list_p[2]))
    return new_list_poly # return all point for parallel_projection


def perspective_projection(list_poly):

    new_list_poly = []
    temp: int = -400
    for poly in list_poly:
        list_p = []
        for i in range(len(poly)):
            p: Point = poly.getPoint(i + 1)
            d = 300
            Sz= d/(p.getZ()+d)
            const_matrix = [[Sz, 0, 0, 0], [0, Sz, 0, 0], [0, 0, 0,0], [0, 0, 0, 1]]
            p_matrix = [p.getX(), p.getY(), p.getZ(), 1]
            result = np.dot(np.array(p_matrix), np.array(const_matrix))
            # result = [x,y,z,w]
            new_p = Point(result[0]/result[3], result[1]/result[3], result[2]/result[3])
            list_p.append(new_p)
            if i + 1 == len(poly):
                if i + 1 == 4:
                    new_list_poly.append(Polygon(list_p[0], list_p[1], list_p[2], list_p[3]))
                elif i + 1 == 3:
                    new_list_poly.append(Polygon(list_p[0], list_p[1], list_p[2]))
    return new_list_poly  # return all point for parallel_projection


def oblique_projections(list_poly):
    new_list_poly = []

    const_matrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

    for poly in list_poly:
        list_p = []
        for i in range(len(poly)):
            p: Point = poly.getPoint(i + 1)
            p_matrix = [p.getX(), p.getY(), p.getZ(), 1]
            result = np.dot(np.array(p_matrix), np.array(const_matrix))
            new_p = Point(result[0], result[1], result[2])
            list_p.append(new_p)
            if i + 1 == len(poly):
                if i + 1 == 4:
                    new_list_poly.append(Polygon(list_p[0], list_p[1], list_p[2], list_p[3]))
                elif i + 1 == 3:
                    new_list_poly.append(Polygon(list_p[0], list_p[1], list_p[2]))
    return new_list_poly  # return all points for parallel_projection


def scale(list_poly, Sx, Sy, Sz):
    """
    We can perform scaling using the following matrix:
    [x', y', z', 1] = [x, y, z, 1] * |Sx  0   0   0|
                                     |0   Sy  0   0|
                                     |0   0   Sz  0|
                                     |0   0   0   1|
    The scaling factors, (Sx, Sy, Sz), are positive numbers.
    So the equations will be:
    x' = x * Sx
    y' = y * Sy
    z' = z * Sz
    """
    new_list_poly = []
    if Sx > 0 and Sy > 0 and Sz > 0:
        dist_x_y_z = distance(list_poly)
        scale_x = (1 - Sx) * dist_x_y_z[0]
        scale_y = (1 - Sy) * dist_x_y_z[1]
        scale_z = (1 - Sz) * dist_x_y_z[2]
        const_matrix = [[Sx, 0, 0, 0],[0, Sy, 0, 0],[0, 0, Sz, 0],[scale_x, scale_y, scale_z, 1]]
        for poly in list_poly:
            list_p = []
            for i in range(len(poly)):
                p = poly.getPoint(i+1)
                p_matrix = [p.getX(), p.getY(), p.getZ(), 1]
                result = np.dot(np.array(p_matrix), np.array(const_matrix))
                new_p = Point(result[0], result[1], result[2])
                list_p.append(new_p)
                if i + 1 == len(poly):
                    if i + 1 == 4:
                        new_list_poly.append(Polygon(list_p[0], list_p[1], list_p[2], list_p[3]))
                    elif i + 1 == 3:
                        new_list_poly.append(Polygon(list_p[0], list_p[1], list_p[2]))
        return new_list_poly
    else:
        display_error("Scaling factors must be bigger than 0!!")
        return list_poly

def rotate(polygons_list: list, theta, axis="x"):
    """
    We recieve a list of polygons, theta (the rotation angle), and the axis to rotate around.
    We can express the equations of the 3d rotation along the x-axis using the following matrix:
    [x', y', z', 1] = [x, y, z, 1] * |             1             0             0             0|
                                     |             0         cos_theta     sin_theta         0|
                                     |             0         -sin_theta    cos_theta         0|
                                     |             0             0             0             1|

    We can express the equations of the 3d rotation along the y-axis using the following matrix:
    [x', y', z', 1] = [x, y, z, 1] * |         cos_theta         0         -sin_theta        0|
                                     |             0             1             0             0|
                                     |         sin_theta         0         cos_theta         0|
                                     |             0             0             0             1|

    We can express the equations of the 3d rotation along the z-axis using the following matrix:
    [x', y', z', 1] = [x, y, z, 1] * | cos_theta   sin_theta       0         0|
                                     |-sin_theta   cos_theta       0         0|
                                     |     0             0         1         0|
                                     |     0             0         0         1|
    """
    theta = np.radians(theta)
    rotate_x_axis_matrix = [[1, 0, 0, 0], [0, cos(theta), sin(theta), 0], [0, -sin(theta), cos(theta), 0], [0, 0, 0, 1]]
    rotate_y_axis_matrix = [[cos(theta), 0, -sin(theta), 0], [0, 1, 0, 0], [sin(theta), 0, cos(theta), 0], [0, 0, 0, 1]]
    rotate_z_axis_matrix = [[cos(theta), sin(theta), 0, 0], [-sin(theta), cos(theta), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]


    if axis == "x":
        rotation_matrix = rotate_x_axis_matrix
    elif axis == "y":
        rotation_matrix = rotate_y_axis_matrix
    elif axis == "z":
        rotation_matrix = rotate_z_axis_matrix
    else:
        display_error("Rotation axis can only be 'x' 'y' or 'z'.")

    new_polygons_list = []
    dist_x_y_z = distance(polygons_list)
    neg_x = - dist_x_y_z[0]
    neg_y = - dist_x_y_z[1]
    neg_z = - dist_x_y_z[2]
    transitionFix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [neg_x, neg_y, neg_z, 1]]
    for poly in polygons_list:
        list_p = []
        for i in range(len(poly)):
            p = poly.getPoint(i + 1)
            p_matrix = [p.x, p.y, p.z, 1]
            p_matrix = np.dot(np.array(p_matrix), np.array(transitionFix))
            p_matrix = np.dot(np.array(p_matrix), np.array(rotation_matrix))
            p_matrix = np.dot(np.array(p_matrix), np.array(transitionFix))
            new_p = Point(int(p_matrix[0]), int(p_matrix[1]), int(p_matrix[2]))
            list_p.append(new_p)
            if i + 1 == len(poly):
                if i + 1 == 4:
                    new_polygons_list.append(
                        Polygon(list_p[0], list_p[1], list_p[2], list_p[3]))
                elif i + 1 == 3:
                    new_polygons_list.append(
                        Polygon(list_p[0], list_p[1], list_p[2]))
    return new_polygons_list
