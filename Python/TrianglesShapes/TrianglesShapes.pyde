import random as rn

WIDTH = 512
HEIGHT = 430
step = 0.01
POINTS_COUNT = 50

points = []
triangles = dict()
lines = dict()
lines_draw = dict()
#lines = [[str(x) + str(y), rn.randint(1, 10000)] for y in range (29) for x in range(y + 1, 30)]
for y in range (POINTS_COUNT - 1):
    for x in range(y + 1, POINTS_COUNT):
        lines[str(y) + str(x)] = rn.randint(1, 10000)
        

def with_chance(n):
    n = (1 - n) * 100
    randomN = rn.randint(0, 100)
    if randomN >= n:
        return True
    else:
        return False

def setup():
    global points, triangles
    size(WIDTH, HEIGHT)
    background(0)
    for _ in range(POINTS_COUNT):
        randomX = rn.randint(1, WIDTH - 1)
        randomY = rn.randint(1, HEIGHT - 1)
        points.append([randomX, randomY, rn.randint(1, 100000)])
    
    
def draw():
    global points, lines, triangles
    background(0)
    for i in range(len(points)):
        points[i][0] += (noise(points[i][2]) * 2 - 1)
        if points[i][0] >= WIDTH:
            points[i][0] = 1
        elif points[i][0] <= 0:
            points[i][0] = WIDTH
        points[i][1] += (noise(points[i][2] + 500) - 0.5) * 4
        if points[i][1] >= HEIGHT:
            points[i][1] = 1
        elif points[i][1] <= 0:
            points[i][1] = HEIGHT
        points[i][2] += step
        noStroke()
        fill(255)
        circle(points[i][0], points[i][1], 5)
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            if 0 < ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5 <= 100 and noise(lines[str(i) + str(j)]) >= 0.55:
                stroke(255)
                line(points[i][0], points[i][1], points[j][0], points[j][1])
                lines_draw[str(i) + str(j)] = True
            else:
                lines_draw[str(i) + str(j)] = False
            lines[str(i) + str(j)] += step
    for i in range(len(points) - 2):
        for j in range(i + 1, len(points) - 1):
            for z in range(j + 1, len(points)):
                if lines_draw[str(i) + str(j)] and lines_draw[str(j) + str(z)] and lines_draw[str(i) + str(z)]:
                    try:
                        proz = triangles[str(i) + str(j) + str(z)]
                    except KeyError:
                        triangles[str(i) + str(j) + str(z)] = rn.randint(10, 90)
                        proz = triangles[str(i) + str(j) + str(z)]
                    noStroke()
                    fill(255, 255, 255, proz)
                    triangle(points[i][0], points[i][1], points[j][0], points[j][1], points[z][0], points[z][1])
                else:
                    triangles.pop(str(i) + str(j) + str(z), None)
                    
                
    
