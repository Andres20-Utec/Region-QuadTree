class Node:
    def __init__(self, boundary):
        self.color = 'w'
        self.boundary = boundary
        self.isLeaf = True
        self.children = []
        self.blackChildren = 0
    
    def setChildrenBox(self):
        x0, y0 = self.boundary[0]
        x1, y1 = self.boundary[1]
        width, height = (x1 - x0) // 2, (y1 - y0) // 2
        middle = (x0 + width, y0 + height)
        top_left = (x0 , y0)
        top_mid = (x0 + width ,y0)
        left_mid = (x0, y0 + height)
        bottom_right = (x1, y1)
        bottom_mid = (x0 + width, y1)
        middle_right = (x1, y0 + height)
        self.children = [
            Node((top_left, middle)), # 1
            Node((top_mid, middle_right)), # 2
            Node((middle, bottom_right)), # 3
            Node((left_mid, bottom_mid)) # 4
        ]
    
    def containsPoint(self, point):
        x, y = point
        x1, y1 = self.boundary[0]
        x2, y2 = self.boundary[1]
        return x2 > x >= x1 and y2 > y >= y1