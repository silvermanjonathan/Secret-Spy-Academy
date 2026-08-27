# ATTACK AT DAWN
# The words appear in pixel letters. Then the coded version appears as shapes.
# Words in the terminal, play in the window. No pygame.font: a letter is a rack of marks.

import pygame

rack = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
message = "ATTACK AT DAWN"
shift = 3

# --- terminal country: the Cipher Wheel, character for character ---
result = ""
for letter in message:
    slot = 0
    for i in range(27):
        if rack[i] == letter:
            slot = i
    slot = (slot + shift) % 27
    result = result + rack[slot]
print("Plain:", message)
print("Coded:", result)

# --- the glyph rack: one letter per slot, five strings of three marks; # is ink, . is air ---
glyphs = [
    [".#.", "#.#", "###", "#.#", "#.#"],  # A
    ["##.", "#.#", "##.", "#.#", "##."],  # B
    [".##", "#..", "#..", "#..", ".##"],  # C
    ["##.", "#.#", "#.#", "#.#", "##."],  # D
    ["###", "#..", "##.", "#..", "###"],  # E
    ["###", "#..", "##.", "#..", "#.."],  # F
    [".##", "#..", "#.#", "#.#", ".##"],  # G
    ["#.#", "#.#", "###", "#.#", "#.#"],  # H
    ["###", ".#.", ".#.", ".#.", "###"],  # I
    ["..#", "..#", "..#", "#.#", ".#."],  # J
    ["#.#", "##.", "#..", "##.", "#.#"],  # K
    ["#..", "#..", "#..", "#..", "###"],  # L
    ["#.#", "###", "#.#", "#.#", "#.#"],  # M
    ["##.", "#.#", "#.#", "#.#", "#.#"],  # N
    [".#.", "#.#", "#.#", "#.#", ".#."],  # O
    ["##.", "#.#", "##.", "#..", "#.."],  # P
    [".#.", "#.#", "#.#", ".#.", "..#"],  # Q
    ["##.", "#.#", "##.", "#.#", "#.#"],  # R
    [".##", "#..", ".#.", "..#", "##."],  # S
    ["###", ".#.", ".#.", ".#.", ".#."],  # T
    ["#.#", "#.#", "#.#", "#.#", "###"],  # U
    ["#.#", "#.#", "#.#", "#.#", ".#."],  # V
    ["#.#", "#.#", "#.#", "###", "#.#"],  # W
    ["#.#", "#.#", ".#.", "#.#", "#.#"],  # X
    ["#.#", "#.#", ".#.", ".#.", ".#."],  # Y
    ["###", "..#", ".#.", "#..", "###"],  # Z
    ["...", "...", "...", "...", "..."],  # space
]

# --- the color rack: nine colors, one per column of the key card ---
colors = [(230, 60, 60), (240, 140, 40), (250, 210, 60),      # red, orange, yellow
          (90, 200, 90), (60, 190, 200), (70, 110, 240),      # green, teal, blue
          (150, 90, 230), (240, 100, 180), (235, 235, 235)]   # purple, pink, white

pygame.init()
screen = pygame.display.set_mode((900, 300))
pygame.display.set_caption("Attack at Dawn")
clock = pygame.time.Clock()

# A letter painted mark by mark: two loops and one gate (Day 3, Drill 3).
def draw_glyph(letter, x, y, size, color):
    slot = 0
    for i in range(27):
        if rack[i] == letter:
            slot = i
    rows = glyphs[slot]
    for r in range(5):
        for c in range(3):
            if rows[r][c] == "#":
                pygame.draw.rect(screen, color, (x + c * size, y + r * size, size - 1, size - 1))

# A letter as a shape and a color: the column picks the color, the shelf picks the shape.
def draw_shape(letter, x, y):
    slot = 0
    for i in range(27):
        if rack[i] == letter:
            slot = i
    color = colors[slot % 9]
    if slot < 9:
        pygame.draw.circle(screen, color, (x, y), 9)
    elif slot < 18:
        pygame.draw.rect(screen, color, (x - 9, y - 9, 18, 18))
    else:
        pygame.draw.polygon(screen, color, [(x, y - 10), (x - 10, y + 8), (x + 10, y + 8)])

# how long is the message? count it the long way, with a tally
length = 0
for letter in message:
    length = length + 1

frame = 0
shown = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((16, 20, 36))

    # the key card: the whole rack as shapes, three shelves of nine
    pygame.draw.rect(screen, (60, 70, 100), (640, 20, 226, 78), 1)
    for shelf in range(3):
        for column in range(9):
            draw_shape(rack[shelf * 9 + column], 656 + column * 24, 36 + shelf * 24)

    # top: the words, one letter every quarter second
    x = 30
    k = 0
    for letter in message:
        if k < shown:
            draw_glyph(letter, x, 120, 8, (235, 235, 235))
        x = x + 32
        k = k + 1

    # below: the coded message as shapes, one second after the last letter lands
    x = 42
    k = 0
    for letter in result:
        if k < shown - length - 3:
            draw_shape(letter, x, 235)
        x = x + 32
        k = k + 1

    pygame.display.flip()

    # the frame clock: one more letter every quarter second
    frame = frame + 1
    if frame % 15 == 0:
        shown = shown + 1
    clock.tick(60)
