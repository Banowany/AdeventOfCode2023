import copy


class Brick:
    def __init__(self, corner1, corner2) -> None:
        self.minx = min(corner1[0], corner2[0])
        self.maxx = max(corner1[0], corner2[0])
        self.miny = min(corner1[1], corner2[1])
        self.maxy = max(corner1[1], corner2[1])
        self.minz = min(corner1[2], corner2[2])
        self.maxz = max(corner1[2], corner2[2])

    def try_fall(self, gridxy) -> bool:
        new_min_z = 0
        for x in range(self.minx, self.maxx+1):
            for y in range(self.miny, self.maxy+1):
                if gridxy[x][y] + 1 > new_min_z:
                    new_min_z = gridxy[x][y] + 1
        
        is_fall = False
        if new_min_z < self.minz:
            is_fall = True
            diff = self.minz - new_min_z
            self.minz -= diff
            self.maxz -= diff
        
        for x in range(self.minx, self.maxx+1):
            for y in range(self.miny, self.maxy+1):
                    gridxy[x][y] = self.maxz
        
        return is_fall




def line_to_brick(corners_as_string: str) -> Brick:
    corner1_as_string, corner2_as_string = corners_as_string.split('~')
    corner1 = [int(x) for x in corner1_as_string.split(',')]
    corner2 = [int(x) for x in corner2_as_string.split(',')]
    return Brick(corner1, corner2)

with open('Day22/input.in', 'r') as file:
    lines = file.read().splitlines()

bricks = [(i, line_to_brick(line)) for i, line in enumerate(lines)]
bricks = sorted(bricks, key=lambda brick: brick[1].minz)

maxx = max(brick.maxx for i, brick in bricks)
maxy = max(brick.maxy for i, brick in bricks)
gridxy = [[0 for _ in range(maxy+1)] for _ in range(maxx+1)]



for i, brick in bricks:
    brick.try_fall(gridxy)

result = 0
for i in range(len(bricks)):
    gridxy = [[0 for _ in range(maxy+1)] for _ in range(maxx+1)]
    any_fall = False
    for j, (_, brick) in enumerate(copy.deepcopy(bricks)):
        if i == j:
            continue

        if brick.try_fall(gridxy):
            any_fall = True
            break
    
    if not any_fall:
        result += 1

print(result)