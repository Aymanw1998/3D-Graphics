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
    # we need to ask the user for an angle!!
    pass

def perspective_projection():  # הטלה פרספקטיבית
    # we need to ask the user for an angle!!
    pass

def oblique_projections():  # הטלה אלכסונית
    # we need to ask the user for an angle!!
    pass

def scale():  # סילום
    pass

def rotate():  # סיבוב
    # we need to ask the user for an angle!!
    # we need to ask the user for an axis!!
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
    def __init__(self, e1, e2, e3, e4=None) -> None:
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3
        self.e4 = e4
        pass

edges_list = []
polygon_list = []

def calculate_visability():  # help function for surface removal
    pass

def calculate_normal_vector():  # help function for surface removal
    pass

def sort_by_z():  # so we know which object is the farthest away so we can draw it first
    pass