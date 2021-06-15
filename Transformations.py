import math
import numpy as np
from math import sin, cos
from Polygon import Vertex, Polygon
################# Transformations######################
def matrix_Multiplication(matrix1, matrix2):
    result=[]
    for j in range(len(matrix2[0])):
        sum = 0
        for k in range(len(matrix2)):
            sum += matrix1[k] * matrix2[k][j]
        result.append(sum)
    return result

def parallel_projection(list_polygon, list_point):  # הטלה מקבילית
    # note to self: we need to ask the user for an angle!!
    # 90

    new_list_point = []
    cos_number: float = math.cos(90 * (math.pi / 180))
    sin_number: float = math.sin(90 * (math.pi / 180))

    #const_matrix = [[ 1, 0, 0, 0 ], [ 0, 1, 0, 0 ], [ cos_number, sin_number, 0, 0 ], [ 0, 0, 0, 1 ]]

    for p in list_point:
        p_matrix = [p[0], p[1], p[2], 1]
        #result = matrix_Multiplication(p_matrix, const_matrix)
        new_vertrex = [p[0], p[1]]
        new_list_point.append(new_vertrex)
    return new_list_point # return all point for parallel_projection


def perspective_projection():  # הטלה פרספקטיבית
    # we need to ask the user for an angle!!
    pass

def oblique_projections():  # הטלה אלכסונית
    # note to self: we need to ask the user for an angle!!
    pass

def scale(p, Sx, Sy, Sz):  # סילום
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
    if Sx > 0 and Sy > 0 and Sz > 0:
        x_prime = p.x * Sx
        y_prime = p.y * Sy
        z_prime = p.z * Sz
    else:
        print("Scaling factors must be bigger than 0!!")
        ############ print error message to GUI!!!!!!!!!!!

# def scale_down():
#     pass

def rotate_x_axis(p, theta):  # סיבוב
    # note to self: we need to ask the user for an angle!!
    """
    Theta is the angle of the rotation.
    We can write the equations of the 3d rotation along the x-axis using the following matrix:
    [x', y', z', 1] = [x, y, z, 1] * |             1             0             0             0|
                                     |             0         cos_theta     sin_theta         0|
                                     |             0         -sin_theta    cos_theta         0|
                                     |             0             0             0             1|
    So the equations will be:
    y' = y * cos_theta - z * sin_theta
    z' = y * sin_theta + z * cos_theta
    x' = x
    """
    y_prime = p.y * cos(theta) - p.z * sin(theta)
    z_prime = p.y * sin(theta) + p.z * cos(theta)
    x_prime = p.x

    transformed_point = Polygon.Vertex(x_prime, y_prime, z_prime)
    return transformed_point

def rotate_y_axis(p, theta):
    """
    Theta is the angle of the rotation.
    We can write the equations of the 3d rotation along the y-axis using the following matrix:
    [x', y', z', 1] = [x, y, z, 1] * |         cos_theta         0         -sin_theta        0|
                                     |             0             1             0             0|
                                     |         sin_theta         0         cos_theta         0|
                                     |             0             0             0             1|
    So the equations will be:
    z' = z * cos_theta - x * sin_theta
    x' = z * sin_theta + x * cos_theta
    y' = y
    """
    z_prime = p.z * cos(theta) - p.x * sin(theta)
    x_prime = p.z * sin(theta) + p.x * cos(theta)
    y_prime = p.y

    transformed_point = Polygon.Vertex(x_prime, y_prime, z_prime)
    return transformed_point

def rotate_z_axis(p, theta):
    """
    Theta is the angle of the rotation.
    We can write the equations of the 3d rotation along the z-axis using the following matrix:
    [x', y', z', 1] = [x, y, z, 1] * | cos_theta   sin_theta       0         0|
                                     |-sin_theta   cos_theta       0         0|
                                     |     0             0         1         0|
                                     |     0             0         0         1|
    So the equations will be:
    x' = x * cos_theta - y * sin_theta
    y' = x * sin_theta + y * cos_theta
    z' = z
    """
    x_prime = p.x * cos(theta) - p.y * sin(theta)
    y_prime = p.x * sin(theta) + p.y * cos(theta)
    z_prime = p.z

    transformed_point = Polygon.Vertex(x_prime, y_prime, z_prime)
    return transformed_point

def remove_hidden_surface():  # הסרת משטחים נסתרים
    """
    In a right-hand coordinate system, a vertex in space is considered to be part of the back face if the following equation is true:
    Ax' + By' + Cz' + D < 0
    when (x', y', z') is our viewing point.
    """
    pass


################## Help functions###############

def calculate_visability():  # help function for surface removal
    """We need to know the visibility of an object to help us remove hidden surfaces."""
    pass

def calculate_normal_vector():  # help function for surface removal
    """To perform the visibility calculation in 'calculate_visibility' we must calculate the normal vector."""
    pass

def sort_by_z():  # so we know which object is the farthest away so we can draw it first
    # ??????? not sure if it belongs in this file, maybe it should be in view?
    """The purpose of this method is to arrage the objects by their z-axis value, so we know which object is the farthest away
    and which is closest to our eyes.
    The objects will be drawn to the screen by this order: first we draw the farthest object and work our way to the closest one."""
    pass