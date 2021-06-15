class Cube:
    def __init__(self, list_polygon):
        self.list_polygon = list_polygon

class pyramid:
    def __init__(self, list_polygon):
        self.list_polygon = list_polygon

class Vertex: # points
    """Each vertex is a 3D point that consists of three values: x, y, z."""
    def __init__(self, x, y, z=0) -> None:
        self.x = x
        self.y = y
        self.z = z
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z


# class Edges: #
#     """An edge represents the line between two vertices."""
#     def __init__(self, v1, v2) -> None:
#         self.v1 = v1
#         self.v2 = v2
#         pass

class Polygon:
    """A polygon is composed of a number of edges. Since we are dealing with a cube and a pyramid, that number can either be
    3 or 4."""
    def __init__(self, e1: Vertex, e2:Vertex, e3:Vertex, e4:Vertex=None) -> None:
        self.e1:Vertex = e1
        self.e2:Vertex = e2
        self.e3:Vertex = e3
        self.e4:Vertex = e4
        pass
    def sentP(self,index: int) -> Vertex:
        if index == 1:
            return self.e1
        elif index == 2:
            return self.e2
        elif index == 3:
            return self.e3
        elif index == 4:
            return self.e4