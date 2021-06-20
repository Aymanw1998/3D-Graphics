class Point: # points
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

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setZ(self, z):
        self.z = z


class Polygon:
    """A polygon is composed of a number of edges. Since we are dealing with a cube and a pyramid, that number can either be
    3 or 4."""
    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point = None) -> None:
        self.p1: Point = p1
        self.p2: Point = p2
        self.p3: Point = p3
        self.p4: Point = p4
        pass
    def getPoint(self,index: int) -> Point:
        if index == 1:
            return self.p1
        elif index == 2:
            return self.p2
        elif index == 3:
            return self.p3
        elif index == 4:
            return self.p4

    def setPoint(self, index: int, p: Point):
        if index == 1:
            self.p1 = p
        elif index == 2:
            self.p2 = p
        elif index == 3:
            self.p3 = p
        elif index == 4:
            self.p4 = p

    def __len__(self):  # so we know if we're dealing with a pyramid or a cube
        if self.p4 is None:
            return 3
        else:
            return 4