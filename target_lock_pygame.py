import pygame, random

pygame.init()
WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Target Lock")
clock = pygame.time.Clock()

# ---------- THE OPS PANEL (your customizations live here) ----------
LOCK_SPEED = 5             # how far the arrow keys move the lock each pass
TARGET_DARTS = [-2, -1, -1, 0, 0, 1, 1, 2]  # the target's possible darts; repeat a number to make it likelier
TURN_EVERY = 25            # the target picks a new direction every 25 passes
LOCK_RANGE = 26            # how close counts as on target (the dot inside the ring)
POINT_EVERY = 50           # hold the lock this many passes in a row to score
WIN_SCORE = 10             # first to this many points wins; keep it 28 or fewer so the pips fit

SCOPE_LEFT = 120
SCOPE_TOP = 40
SCOPE_SIZE = 400
CENTER_X = 320
CENTER_Y = 240
INK = (27, 31, 38)
PHOSPHOR = (123, 228, 149)
AMBER = (201, 139, 31)
CORAL = (255, 120, 90)
# -------------------------------------------------------------------

SCOPE_RIGHT = SCOPE_LEFT + SCOPE_SIZE
SCOPE_BOTTOM = SCOPE_TOP + SCOPE_SIZE

def draw_scope(surface):
    pygame.draw.rect(surface, PHOSPHOR,
                     (SCOPE_LEFT, SCOPE_TOP, SCOPE_SIZE, SCOPE_SIZE), 2)
    pygame.draw.circle(surface, PHOSPHOR, (CENTER_X, CENTER_Y), 140, 1)
    pygame.draw.circle(surface, PHOSPHOR, (CENTER_X, CENTER_Y), 70, 1)

def draw_lock(surface, x, y, color):
    # the crosshair and the lock ring, drawn wherever the lock is
    pygame.draw.line(surface, color, (SCOPE_LEFT, y), (SCOPE_RIGHT, y), 1)
    pygame.draw.line(surface, color, (x, SCOPE_TOP), (x, SCOPE_BOTTOM), 1)
    pygame.draw.circle(surface, color, (x, y), 24, 2)

def draw_target(surface, x, y):
    pygame.draw.circle(surface, CORAL, (x, y), 8)

# The victory banner: racks of letters, drawn square by square.
# Every X below becomes one small rectangle, by the score pips' rule.
MISSION_ROWS = [
"X   X XXXXX  XXXX  XXXX XXXXX  XXX  X   X",
"XX XX   X   X     X       X   X   X XX  X",
"X X X   X    XXX   XXX    X   X   X X X X",
"X   X   X       X     X   X   X   X X  XX",
"X   X XXXXX XXXX  XXXX  XXXXX  XXX  X   X",
]
FINISHED_ROWS = [
"XXXXX XXXXX X   X XXXXX  XXXX X   X XXXXX XXXX ",
"X       X   XX  X   X   X     X   X X     X   X",
"XXXX    X   X X X   X    XXX  XXXXX XXXX  X   X",
"X       X   X  XX   X       X X   X X     X   X",
"X     XXXXX X   X XXXXX XXXX  X   X XXXXX XXXX ",
]

def draw_banner(surface, rows, left, top):
    for r in range(5):
        row = rows[r]
        for c in range(len(row)):
            if row[c] == "X":
                pygame.draw.rect(surface, PHOSPHOR,
                                 (left + c * 8, top + r * 8, 7, 7))

def draw_score(surface, points):
    # one pip per point, placed by Day 1's rule: start at the corner, step by 14
    for p in range(points):
        pygame.draw.rect(surface, PHOSPHOR,
                         (SCOPE_LEFT + 12 + p * 14, SCOPE_TOP + 12, 8, 8))

lock_x = CENTER_X                # the lock starts at the center
lock_y = CENTER_Y
target_x = SCOPE_LEFT + 80       # the target starts low on the left
target_y = SCOPE_BOTTOM - 80
target_dx = 0                    # the target's current dart, rolled below
target_dy = 0
reroll = 0                       # the pass number of the next direction change
score = 0                        # points earned
mission_complete = False         # flips when the score reaches WIN_SCORE
streak = 0                       # passes locked on in a row, so far
locked = 0                       # a tally of every pass spent locked on
frame = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- the Remote: the keyboard is a rack, one slot per key, True while held ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        lock_x = lock_x - LOCK_SPEED
    if keys[pygame.K_RIGHT]:
        lock_x = lock_x + LOCK_SPEED
    if keys[pygame.K_UP]:
        lock_y = lock_y - LOCK_SPEED            # up is SMALLER y
    if keys[pygame.K_DOWN]:
        lock_y = lock_y + LOCK_SPEED

    # --- the fence: the lock can't leave the scope ---
    if lock_x < SCOPE_LEFT:
        lock_x = SCOPE_LEFT
    if lock_x > SCOPE_RIGHT:
        lock_x = SCOPE_RIGHT
    if lock_y < SCOPE_TOP:
        lock_y = SCOPE_TOP
    if lock_y > SCOPE_BOTTOM:
        lock_y = SCOPE_BOTTOM

    # --- the target: darts in a random direction, and changes its mind ---
    if frame == reroll:
        target_dx = random.choice(TARGET_DARTS)
        target_dy = random.choice(TARGET_DARTS)
        reroll = reroll + TURN_EVERY
    if mission_complete:                        # the mission is over: the target stands down
        target_dx = 0
        target_dy = 0
    target_x = target_x + target_dx
    target_y = target_y + target_dy

    # --- the walls: the target bounces, flipping its dart ---
    if target_x < SCOPE_LEFT + 10:
        target_x = SCOPE_LEFT + 10
        target_dx = 0 - target_dx
    if target_x > SCOPE_RIGHT - 10:
        target_x = SCOPE_RIGHT - 10
        target_dx = 0 - target_dx
    if target_y < SCOPE_TOP + 10:
        target_y = SCOPE_TOP + 10
        target_dy = 0 - target_dy
    if target_y > SCOPE_BOTTOM - 10:
        target_y = SCOPE_BOTTOM - 10
        target_dy = 0 - target_dy

    # --- the lock test: four checkpoints, and all four must pass ---
    close = 0
    if lock_x > target_x - LOCK_RANGE:
        close = close + 1
    if lock_x < target_x + LOCK_RANGE:
        close = close + 1
    if lock_y > target_y - LOCK_RANGE:
        close = close + 1
    if lock_y < target_y + LOCK_RANGE:
        close = close + 1
    if close == 4:                              # on target
        lock_color = PHOSPHOR
        locked = locked + 1
        streak = streak + 1
    else:                                       # searching
        lock_color = AMBER
        streak = 0

    # --- scoring: hold the lock for POINT_EVERY passes in a row ---
    if mission_complete:                        # no more points; the medal is yours
        streak = 0
    if streak == POINT_EVERY:
        score = score + 1
        streak = 0
        print(f"Point! Score: {score} of {WIN_SCORE}")
    if score == WIN_SCORE:                      # the winning condition
        mission_complete = True

    screen.fill(INK)
    draw_scope(screen)
    draw_lock(screen, lock_x, lock_y, lock_color)   # the scope follows the lock
    draw_target(screen, target_x, target_y)
    draw_score(screen, score)
    if mission_complete:
        draw_banner(screen, MISSION_ROWS, 156, 190)
        draw_banner(screen, FINISHED_ROWS, 132, 250)

    pygame.display.flip()
    frame = frame + 1          # counts the passes
    clock.tick(60)

pygame.quit()
if mission_complete:
    print(f"MISSION COMPLETE: {WIN_SCORE} points. On target for {locked} of {frame} passes.")
else:
    print(f"Mission ends at {score} point(s). On target for {locked} of {frame} passes.")
