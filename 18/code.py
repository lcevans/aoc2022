with open('data.txt') as f:
    droplets = [tuple(int(e) for e in line.strip().split(',')) for line in f]

## PART 1

num_adjacent = 0
for i, drop1 in enumerate(droplets):
    for j, drop2 in enumerate(droplets):
        if i <= j:
            continue
        x1, y1, z1 = drop1
        x2, y2, z2 = drop2
        if abs(x1-x2) + abs(y1-y2) + abs(z1-z2) == 1:
            num_adjacent += 1

surface_area = 6 * len(droplets) - 2 * num_adjacent
print(surface_area)


## PART 2

MAX = max(max(x,y,z) for x,y,z in droplets)
MIN = min(min(x,y,z) for x,y,z in droplets)

# In box [MIN-1, MAX+1]^3, do graph search to see which external surfaces are hit

def neighbors(x, y, z):
    adjacent = [(x+dx, y+dy, z+dz)
               for dx in [-1, 0, 1]
               for dy in [-1, 0, 1]
               for dz in [-1, 0, 1]
               if abs(dx)+abs(dy)+abs(dz) == 1]
    for nx, ny, nz in adjacent:
        if all(MIN-1<=coor<=MAX+1 for coor in [nx,ny,nz]):
            yield (nx, ny, nz)

ext_surface_area = 0
start = (MIN-1, MIN-1, MIN-1)
visited = {start}
queue = [start]
while queue:
    x, y, z = queue.pop(0)
    for nx, ny, nz in neighbors(x, y, z):
        if (nx, ny, nz) in droplets:
            ext_surface_area += 1
        elif (nx, ny, nz) not in visited:
            visited.add((nx, ny, nz))
            queue.append((nx, ny, nz))

print(ext_surface_area)
