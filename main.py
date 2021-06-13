# TODO:
# projections - הטלות דו מימדיות של האובייקים התלת מימדיים
# scaling - סילום, הגדלה והקטנה של צמד האובייקטים
# rotation - סיבוב צמד אובייקטים
# hideen surface removal- הסרת משטחים נסתרים
# exit program button
# load file button
# check the data is valid- else put out an error message
# help function

def parallel_projection():  # הטלה מקבילית
    # note to self: we need to ask the user for an angle!!
    pass

def perspective_projection():  # הטלה פרספקטיבית
    # we need to ask the user for an angle!!
    pass

def oblique_projections():  # הטלה אלכסונית
    # note to self: we need to ask the user for an angle!!
    pass

def scale_up():  # סילום
    pass

def scale_down():
    pass

def rotate_x_axis():  # סיבוב
    # note to self: we need to ask the user for an angle!!
    pass

def rotate_y_axis():
    pass

def rotate_z_axis():
    pass

def remove_hidden_surface():  # הסרת משטחים נסתרים
    pass


class Vertex:
    """Each vertex is a 3D point that consists of three values: x, y, z."""
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

class Edges:
    """An edge represents the line between two vertices."""
    def __init__(self, v1, v2) -> None:
        self.v1 = v1
        self.v2 = v2
        pass

class Polygon:
    """A polygon is composed of a number of edges. Since we are dealing with a cube and a pyramid, that number can either be
    3 or 4."""
    def __init__(self, e1, e2, e3, e4=None) -> None:
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
        self.e4 = e4
        pass

edges_list = []
polygon_list = []

def calculate_visability():  # help function for surface removal
    """We need to know the visibility of an object to help us remove hidden surfaces."""
    pass

def calculate_normal_vector():  # help function for surface removal
    """To perform the visibility calculation in 'calculate_visibility' we must calculate the normal vector."""
    pass

def sort_by_z():  # so we know which object is the farthest away so we can draw it first
    """The purpose of this method is to arrage the objects by their z-axis value, so we know which object is the farthest away
    and which is closest to our eyes.
    The objects will be drawn to the screen by this order: first we draw the farthest object and work our way to the closest one."""
    pass