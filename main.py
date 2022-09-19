from RegionQuadTree import *
import pygame

pygame.init()

WIDTH, HEIGHT = 1000, 1000

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))
pygame.display.flip()


# Screen color
color = (255, 0 ,0)
pygame.display.flip()

# Square Boundary
RQTREE1_boundary = ((200, 200), (400, 400))
RQTREE2_boundary = ((600, 200), (800, 400))

TREE_HEIGHT = 3

RQTree1 = RegionQuadTree(RQTREE1_boundary)
RQTree1.createTree(TREE_HEIGHT)

RQTree2 = RegionQuadTree(RQTREE2_boundary)
RQTree2.createTree(TREE_HEIGHT)

# RQTree1.bfs()
# print(RQTree1.markRectangle((2, 2)))

UNION_boundary = ((200, 600), (400, 800))
INTERSECTION_boundary = ((600, 600), (800, 800))

union = RegionQuadTree(UNION_boundary)
union.createTree(TREE_HEIGHT)
intersection = RegionQuadTree(INTERSECTION_boundary)
intersection.createTree(TREE_HEIGHT)


diff_betwenn_tables = 400

rqtree1_p = []
rqtree2_p = []
union_ = []
intersection_ = []

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            p1 = RQTree1.markRectangle(screen, position)
            p2 = RQTree2.markRectangle(screen, position)
            if p1 != None:
                if p1 not in union_:
                    union_.append(p1)
                rqtree1_p.append(p1)
            if p2 != None:
                x, y = p2
                x -= diff_betwenn_tables
                if p2 not in union_:
                    union_.append((x, y))
                rqtree2_p.append((x, y))
            intersection_ = [ p2 for p1 in rqtree1_p for p2 in rqtree2_p if p1 == p2]
                
            for e in union_:
                x, y = e
                y += diff_betwenn_tables
                union.markRectangle(screen, (x, y))
            
            for e in intersection_:
                x, y = e
                x += diff_betwenn_tables
                y += diff_betwenn_tables
                intersection.markRectangle(screen, (x, y))
            pygame.display.flip()



    RQTree1.Show(screen)
    RQTree2.Show(screen)
    union.Show(screen)
    intersection.Show(screen)

    pygame.display.flip()