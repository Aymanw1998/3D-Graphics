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


class Point3D:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z


vertices_list = [] # is a list of 3d points
polygon_list = [] # is a list of vertices