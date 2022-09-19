from turtle import width
from Node import *
import pygame
class RegionQuadTree:
    def __init__(self, boundary):
        self.root = None
        self.boundary = boundary
    
    def createTree(self, tree_height):
        self.root = Node(self.boundary)
        if(tree_height > 0):
            self.root.setChildrenBox()
            self.root.isLeaf = False
            children = self.root.children
            self.insert(tree_height - 1, children)
        else:
            self.root.isLeaf = True

    def insert(self, tree_height: int, children: Node):
        if(tree_height >= 1):
            for child in children:
                child.isLeaf = False
                child.setChildrenBox()
                self.insert(tree_height - 1, child.children)
        else:
            for child in children:
                child.isLeaf = True
    
    def markRectangle(self, screen, point):
        if(self.root.containsPoint(point)):
            measure = self.root.boundary[1][0] - self.root.boundary[0][0]
            return self.Mark(self.root, screen, point, measure, measure)
        return None


    def Mark(self, node : Node, screen, point, width = 0, height = 0):
        if not node.isLeaf:
            node.color = 'g'
            width, height = (node.boundary[1][0] - node.boundary[0][0]), node.boundary[1][1] - node.boundary[0][1]
            for child in node.children:
                if child.containsPoint(point):
                    child.color = 'g'
                    child.blackChildren += 1
                    return self.Mark(child, screen, point, width//2, height//2)
        else:
            if node.containsPoint(point):
                node.color = 'b'
                x1, y1 = node.boundary[0]
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x1 + 1, y1 + 1, width - 1, height - 1))
                return (x1, y1)
            return None

    def Show(self, screen):
        if self.root != None:
            width, height = self.boundary[1][0] - self.boundary[0][0], self.boundary[1][1] - self.boundary[0][1]
            self.Draw(screen, self.root, width, height)
    
    def Draw(self, screen, node, width, height):
        if not node.isLeaf:
            for child in node.children:
                self.Draw(screen, child ,width // 2, height // 2)
        else:
            x1, y1 = node.boundary[0]
            pygame.draw.rect(screen, (71, 88, 212), pygame.Rect(x1, y1, width, height), 2)
    



    def bfs(self):
        visited = []
        queue = []
        visited.append(self.root)
        queue.append(self.root)
        while queue:
            m = queue.pop(0)
            print(m.boundary)
            if len(m.children) != 0:
                children = m.children
                for i, child in enumerate(children):
                    queue.append(child)






