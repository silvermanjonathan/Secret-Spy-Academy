import pygame, random

pygame.init()
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Beacon Field")
clock = pygame.time.Clock()

# ---------- THE OPS PANEL (your customizations live here) ----------
BEACON_COLORS = [(123, 228, 149), (242, 233, 211), (201, 139, 31)]
BEACON_COUNT = 12
DRIFT_SPEED = 1
SWEEP_SPEED = 4
DRAIN_RATE = 1
FULL_BATTERY = 200

SCOPE_LEFT = 120
SCOPE_TOP = 40
SCOPE_SIZE = 400
CENTER_X = 320
CENTER_Y = 240
INK = (27, 31, 38)
PHOSPHOR = (123, 228, 149)
# -------------------------------------------------------------------

SCOPE_RIGHT = SCOPE_LEFT + SCOPE_SIZE
SCOPE_BOTTOM = SCOPE_TOP + SCOPE_SIZE

# Parallel lists: beacon number i is xs[i], ys[i], batteries[i], colors[i]
xs = []
ys = []
batteries = []
colors = []

for i in range(BEACON_COUNT):
    xs.append(random.randint(SCOPE_LEFT + 20, SCOPE_RIGHT - 20))
    ys.append(random.randint(CENTER_Y, SCOPE_BOTTOM - 40))
    batteries.append(random.randint(60, FULL_BATTERY))
    colors.append(random.choice(BEACON_COLORS))

def draw_scope(surface):
    pygame.draw.rect(surface, PHOSPHOR,
                     (SCOPE_LEFT, SCOPE_TOP, SCOPE_SIZE, SCOPE_SIZE), 2)
    pygame.draw.circle(surface, PHOSPHOR, (CENTER_X, CENTER_Y), 140, 1)
    pygame.draw.circle(surface, PHOSPHOR, (CENTER_X, CENTER_Y), 70, 1)
    pygame.draw.line(surface, PHOSPHOR,
                     (SCOPE_LEFT, CENTER_Y), (SCOPE_RIGHT, CENTER_Y), 1)
    pygame.draw.line(surface, PHOSPHOR,
                     (CENTER_X, SCOPE_TOP), (CENTER_X, SCOPE_BOTTOM), 1)

def draw_beacon(surface, x, y, battery, color):
    if battery > 130:
        size = 7
    elif battery > 50:
        size = 5
    else:
        size = 3
    pygame.draw.circle(surface, color, (x, y), size)

sweep_x = SCOPE_LEFT
frame = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    sweep_x = sweep_x + SWEEP_SPEED            # the sweep: Day 2's drone, on duty
    if sweep_x > SCOPE_RIGHT:                  # past the right edge: wrap
        sweep_x = SCOPE_LEFT

    screen.fill(INK)
    draw_scope(screen)
    pygame.draw.line(screen, PHOSPHOR,
                     (sweep_x, SCOPE_TOP), (sweep_x, SCOPE_BOTTOM), 3)

    for i in range(BEACON_COUNT):
        ys[i] = ys[i] - DRIFT_SPEED                 # rising: y gets SMALLER
        xs[i] = xs[i] + random.randint(-1, 1)       # the wobble
        batteries[i] = batteries[i] - DRAIN_RATE    # the drain: a tally in reverse
        if batteries[i] < 0:                        # dead: a fresh beacon takes the slot
            xs[i] = random.randint(SCOPE_LEFT + 20, SCOPE_RIGHT - 20)
            ys[i] = random.randint(CENTER_Y, SCOPE_BOTTOM - 40)
            batteries[i] = FULL_BATTERY
        draw_beacon(screen, xs[i], ys[i], batteries[i], colors[i])

    pygame.display.flip()
    frame = frame + 1          # counts the passes; timed gates read it
    clock.tick(60)

pygame.quit()
