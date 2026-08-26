# ============================================================
#  THE CIPHER CONSOLE  ·  Secret Spy Academy
#  Front end for any Day 2 / Cryptography Wing cipher.
#  Read it, trace it, then run it.
#
#  HOW IT WORKS
#  1. The terminal asks for your message (CAPITALS AND SPACES)
#     plus your key. Keep the message under 36 characters.
#  2. THE CARTRIDGE encodes it. The one installed below is
#     Day 2's Cipher Wheel. Swap the cartridge for any Wing
#     cipher; two spares wait at the bottom of this file.
#  3. The window animates it: your letter's tile lights on the
#     plain rack, the signal drops to the coded rack, and the
#     coded message assembles in pixel letters.
#  Press R in the window to replay. Close the window to stop:
#  the console never closes itself.
# ============================================================

import pygame

# ===================== OPS PANEL =====================
KID_TITLE     = "CIPHER CONSOLE"   # your console's name, on the board
PULSE_FRAMES  = 10                 # frames the plain tile glows
TRAVEL_FRAMES = 22                 # frames the signal takes to drop
FLASH_FRAMES  = 12                 # frames the coded tile flashes
BOARD_COLOR   = (15, 19, 24)
TILE_COLOR    = (242, 233, 211)
TILE_INK      = (27, 31, 38)
CODED_TILE    = (31, 46, 39)
CODED_INK     = (123, 228, 149)
SIGNAL_COLOR  = (201, 139, 31)
TITLE_COLOR   = (201, 139, 31)
ECHO_COLOR    = (150, 143, 128)
ASSEMBLY_INK  = (123, 228, 149)
HINT_COLOR    = (90, 96, 88)
# =====================================================

RACK = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
LETTER_EVERY = PULSE_FRAMES + TRAVEL_FRAMES + FLASH_FRAMES

# Every character's picture: 5 rows of 3 marks. # is ink.
GLYPHS = [
[".#.","#.#","###","#.#","#.#"],  # A
["##.","#.#","##.","#.#","##."],  # B
[".##","#..","#..","#..",".##"],  # C
["##.","#.#","#.#","#.#","##."],  # D
["###","#..","##.","#..","###"],  # E
["###","#..","##.","#..","#.."],  # F
[".##","#..","#.#","#.#",".##"],  # G
["#.#","#.#","###","#.#","#.#"],  # H
["###",".#.",".#.",".#.","###"],  # I
["..#","..#","..#","#.#",".#."],  # J
["#.#","#.#","##.","#.#","#.#"],  # K
["#..","#..","#..","#..","###"],  # L
["#.#","###","###","#.#","#.#"],  # M
["#.#","###","###","###","#.#"],  # N
[".#.","#.#","#.#","#.#",".#."],  # O
["##.","#.#","##.","#..","#.."],  # P
[".#.","#.#","#.#",".#.","..#"],  # Q
["##.","#.#","##.","#.#","#.#"],  # R
[".##","#..",".#.","..#","##."],  # S
["###",".#.",".#.",".#.",".#."],  # T
["#.#","#.#","#.#","#.#","###"],  # U
["#.#","#.#","#.#","#.#",".#."],  # V
["#.#","#.#","###","###","#.#"],  # W
["#.#","#.#",".#.","#.#","#.#"],  # X
["#.#","#.#",".#.",".#.",".#."],  # Y
["###","..#",".#.","#..","###"],  # Z
["...","...","...","...","..."],  # space
]

# ---------------- the terminal briefing ----------------
print("CIPHER CONSOLE ONLINE.")
print("Capitals and spaces only. Under 36 characters fits the board.")
message = input("Message: ")
legal = 0
while legal == 0:
    legal = 1
    if len(message) == 0:
        legal = 0
    for letter in message:
        found = 0
        for j in range(27):
            if RACK[j] == letter:
                found = 1
        if found == 0:
            legal = 0
    if legal == 0:
        print("Every character must be on the rack: CAPITALS AND SPACES ONLY.")
        message = input("Message: ")
key = int(input("Key (1 to 26): "))
key = key % 27

# ================= THE CARTRIDGE =================
# Installed: Day 2's Cipher Wheel (the Caesar shift).
# Swap this whole block for any Wing cipher. Keep the
# first line (coded = "") and keep building coded the
# same way. Spare cartridges wait at the bottom.
coded = ""
for letter in message:
    slot = 0
    for j in range(27):
        if RACK[j] == letter:
            slot = j
    coded_slot = (slot + key) % 27
    coded = coded + RACK[coded_slot]
# =============== END OF CARTRIDGE ================

print("Coded:", coded)
print("The window is yours. R replays the encoding.")

# ---------------- the window ----------------
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Cipher Console")
clock = pygame.time.Clock()

TILE_W = 20
TILE_H = 26
RACK_X = 23
TOP_Y = 120
BOT_Y = 300

def draw_glyph(letter, x, y, scale, color):
    slot = 0
    for j in range(27):
        if RACK[j] == letter:
            slot = j
    for r in range(5):
        for c in range(3):
            if GLYPHS[slot][r][c] == "#":
                pygame.draw.rect(screen, color, (x + c * scale, y + r * scale, scale, scale))

def draw_text(text, y, scale, color):
    step = 3 * scale + scale
    width = len(text) * step - scale
    x = int(320 - width / 2)
    for k in range(len(text)):
        draw_glyph(text[k], x + k * step, y, scale, color)

length = len(message)
pos = 0
frame_in = 0
done = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        pos = 0
        frame_in = 0
        done = 0

    # which tiles are talking this frame
    plain_slot = 0
    for j in range(27):
        if RACK[j] == message[pos]:
            plain_slot = j
    coded_slot = 0
    for j in range(27):
        if RACK[j] == coded[pos]:
            coded_slot = j
    tx = RACK_X + plain_slot * (TILE_W + 2) + 10
    bx = RACK_X + coded_slot * (TILE_W + 2) + 10

    screen.fill(BOARD_COLOR)
    draw_text(KID_TITLE, 22, 4, TITLE_COLOR)
    draw_text(message, 74, 2, ECHO_COLOR)

    # the two racks
    for t in range(27):
        x = RACK_X + t * (TILE_W + 2)
        pygame.draw.rect(screen, TILE_COLOR, (x, TOP_Y, TILE_W, TILE_H))
        draw_glyph(RACK[t], x + 7, TOP_Y + 8, 2, TILE_INK)
        pygame.draw.rect(screen, CODED_TILE, (x, BOT_Y, TILE_W, TILE_H))
        draw_glyph(RACK[t], x + 7, BOT_Y + 8, 2, CODED_INK)

    # the active plain tile always glows
    px = RACK_X + plain_slot * (TILE_W + 2)
    pygame.draw.rect(screen, SIGNAL_COLOR, (px - 2, TOP_Y - 2, TILE_W + 4, TILE_H + 4), 2)

    reveal_current = 0
    if frame_in < PULSE_FRAMES:
        pygame.draw.circle(screen, SIGNAL_COLOR, (tx, TOP_Y + TILE_H + 6), 5)
    elif frame_in < PULSE_FRAMES + TRAVEL_FRAMES:
        p = frame_in - PULSE_FRAMES
        f = p / TRAVEL_FRAMES
        lx = int(tx + (bx - tx) * f)
        ly = int(TOP_Y + TILE_H + (BOT_Y - TOP_Y - TILE_H) * f)
        pygame.draw.circle(screen, (90, 62, 20), (lx, ly), 9)
        pygame.draw.circle(screen, SIGNAL_COLOR, (lx, ly), 5)
    elif frame_in < LETTER_EVERY:
        cx = RACK_X + coded_slot * (TILE_W + 2)
        pygame.draw.rect(screen, ASSEMBLY_INK, (cx - 2, BOT_Y - 2, TILE_W + 4, TILE_H + 4), 2)
        reveal_current = 1

    # the coded message assembles
    step = 16
    width = length * step - 4
    ax = int(320 - width / 2)
    for k in range(pos):
        draw_glyph(coded[k], ax + k * step, 396, 4, ASSEMBLY_INK)
    if reveal_current == 1:
        draw_glyph(coded[pos], ax + pos * step, 396, 4, ASSEMBLY_INK)

    if done == 1:
        draw_text("PRESS R TO REPLAY", 452, 2, HINT_COLOR)

    if done == 0:
        frame_in = frame_in + 1
    if frame_in == LETTER_EVERY:
        pos = pos + 1
        frame_in = 0
    if pos == length:
        done = 1
        pos = length - 1
        frame_in = LETTER_EVERY - 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# ================= SPARE CARTRIDGES =================
# To swap: delete the installed cartridge block above and
# paste one of these in its place. Nothing else changes.
#
# --- THE ROTOR (the wheel that turns itself) ---
# coded = ""
# i = 0
# for letter in message:
#     slot = 0
#     for j in range(27):
#         if RACK[j] == letter:
#             slot = j
#     coded_slot = (slot + (key + i) % 27) % 27
#     coded = coded + RACK[coded_slot]
#     i = i + 1
#
# --- THE UNBREAKABLE WHEEL (Vigenere) ---
# Add this line just above the cartridge, with the inputs:
#     keyword = input("Keyword: ")
# coded = ""
# i = 0
# for letter in message:
#     slot = 0
#     for j in range(27):
#         if RACK[j] == letter:
#             slot = j
#     kletter = keyword[i % len(keyword)]
#     kslot = 0
#     for j in range(27):
#         if RACK[j] == kletter:
#             kslot = j
#     coded_slot = (slot + kslot) % 27
#     coded = coded + RACK[coded_slot]
#     i = i + 1
# ====================================================
