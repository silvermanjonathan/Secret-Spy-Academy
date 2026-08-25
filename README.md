# Secret Spy Academy

A five-day Grade 5 Python week from the **Beyond Vibe Coding** curriculum: recruits leave able to *read, trace, and reason about* the code they run. Your computer is your terminal, VS Code is your workshop, and Python is the language it obeys. Exactly, and only exactly.

## → Enter HQ

**[Enter HQ — the live hub](https://silvermanjonathan.github.io/Secret-Spy-Academy/spy_academy_hub.html)**

Live site root: <https://silvermanjonathan.github.io/Secret-Spy-Academy/>

This repo has no `index.html` by design: this README is the site root, and the hub is the front door. Every lesson page is fully self-contained (all CSS/JS inline) and links back through the hub.

All course links in this README are absolute `github.io` addresses on purpose. They open the rendered webpages even when you're reading this file on `github.com`, where a relative link opens the raw HTML source instead.

## The week

| Day | Briefing | New tools | Artifact |
|---|---|---|---|
| 1 | [Induction Day & the Three Clearance Checks](https://silvermanjonathan.github.io/Secret-Spy-Academy/day1_induction_day.html) | `print`, tracebacks, variables, `input`/`int()`, f-strings, `for`/`range`, `if`/`elif`/`else`, lists, `random.choice`, `in` | The Induction Terminal + a Division assignment |
| 2 | [The Cipher Room](https://silvermanjonathan.github.io/Secret-Spy-Academy/day2_cipher_room.html) | cryptography day, two benches. Morning, the Cipher Machine: paper wheel by hand, the rack, `==`/`!=`, the slot search, the shift (wrap met as a crash-and-repair), the tally, the Caesar wheel, decode, the key ceremony. Afternoon, the Codebreaker's Bench: `while` & the sentinel gate, `%` as clock arithmetic (the wheel respelled professionally), the frequency leak, cracking all 27 keys, the double-shift clerk's error. Morning hinge is a legitimate floor landing | The Dead Drop + the Safe House door |
| 3 | [The Gadget Blueprint](https://silvermanjonathan.github.io/Secret-Spy-Academy/day3_gadget_blueprint.html) | `def` & parameters, the loaded dice; first pygame windows, the `while running` loop and the frame tally, the keyboard as a rack; playing and reading the capstone game | The Blueprint Rehearsal + the initialed game |
| 4 | [The Gadget Commission](https://silvermanjonathan.github.io/Secret-Spy-Academy/day4_gadget_commission.html) | zero new syntax: the Gadget Schematic, the knobs, the banner, your own def, the Bug Hunt protocol & log | Your Commissioned Edition, finished: a redesigned [Target Lock](https://silvermanjonathan.github.io/Secret-Spy-Academy/target_lock_pygame.py) |
| 5 | [The Final Debrief](https://silvermanjonathan.github.io/Secret-Spy-Academy/day5_final_debrief.html) | zero new syntax: presentations only (Run, Point, Tell), the audience's what-if, the Dead Drop exchange | The Final Debrief + the Field Agent badge |

The Commission is **finished by the end of Day 4**, debugging included. Day 5 is presentations only.

The capstone is **Target Lock**, a playable game: a coral target darts and pauses around the scope, the agent steers the lock with the arrow keys, holding it on target scores, and the first to ten points sees the MISSION FINISHED banner (drawn without `pygame.font`, from racks of strings). Day 3 plays and reads the clean game; Day 4 commissions each agent's own edition: a kid mode and a pro mode, their colors, their banner, and one routine of their own. Nine side missions are live for agents who finish early, all terminal-only. The first two open after Day 2: [The Cipher Grid](https://silvermanjonathan.github.io/Secret-Spy-Academy/side_mission_cipher_grid.html) stacks a parallel-racks substitution cipher with a column-read grid into a double lock, and [The Safecracker's Ledger](https://silvermanjonathan.github.io/Secret-Spy-Academy/side_mission_safecracker.html) cracks a safe by counting and by gambling, then searches the ledger with best-so-far.

The other seven form the **Cryptography Wing**, built on Day 2's two benches (the wheel and `%`). [The Unbreakable Wheel](https://silvermanjonathan.github.io/Secret-Spy-Academy/side_mission_unbreakable_wheel.html) is the Vigenère cipher plus the rotor, and the proof that Day 2's frequency leak bounces off both. [The Tamper Seal](https://silvermanjonathan.github.io/Secret-Spy-Academy/side_mission_tamper_seal.html) is integrity: a one-letter checksum, its blind spot, and the position-weighted repair. [The One-Time Pad](https://silvermanjonathan.github.io/Secret-Spy-Academy/side_mission_one_time_pad.html) is the provably unbreakable cipher and the reuse leak that enforces its burn rule (sequence it after the Wheel). [The Hidden Channel](https://silvermanjonathan.github.io/Secret-Spy-Academy/side_mission_hidden_channel.html) is steganography on channel 5, the Wing's lightest mission. [The Keyword Cipher](https://silvermanjonathan.github.io/Secret-Spy-Academy/side_mission_keyword_cipher.html) builds a memorizable substitution rack and audits its lazy tail (sequence it after the Cipher Grid). [The Shared Secret](https://silvermanjonathan.github.io/Secret-Spy-Academy/side_mission_shared_secret.html) is Diffie-Hellman at classroom scale, the Wing's summit. [The Crack Tournament](https://silvermanjonathan.github.io/Secret-Spy-Academy/side_mission_crack_tournament.html) closes the Wing as a whole-class event with two leagues and a referee's checker.

## Files

Flat repo, no build step. Ship everything together; the hub must always be re-uploaded alongside any new or changed page.

```
README.md                        ← you are here (site root)
spy_academy_hub.html             ← the front door
day1_induction_day.html
day2_cipher_room.html
day3_gadget_blueprint.html
day4_gadget_commission.html
day5_final_debrief.html
target_lock_pygame.py            ← the capstone game, byte-identical to the Day 3 in-page listing
side_mission_cipher_grid.html    ← side mission: the Cipher Grid (after Day 2)
side_mission_safecracker.html    ← side mission: the Safecracker's Ledger (after Day 2)
side_mission_unbreakable_wheel.html   ← Cryptography Wing: Vigenère + the rotor
side_mission_tamper_seal.html         ← Cryptography Wing: checksum seals, plain and weighted
side_mission_one_time_pad.html        ← Cryptography Wing: the pad and the reuse leak (after the Wheel)
side_mission_hidden_channel.html      ← Cryptography Wing: steganography on channel 5
side_mission_keyword_cipher.html      ← Cryptography Wing: keyword racks, audited (after the Cipher Grid)
side_mission_shared_secret.html       ← Cryptography Wing: Diffie-Hellman at classroom scale
side_mission_crack_tournament.html    ← Cryptography Wing: the whole-class closing event
field_notebook_handout.html      ← the printable Field Notebook (trace sheets, the codebreaker's corner, and the Bug Hunt Log, one per agent)
```

## Student setup

- VS Code with the Python extension, Python 3.10+ (the traceback "Did you mean" hint shown on Day 1 assumes 3.10+; nothing depends on it).
- Installs happen the day they're needed, in the VS Code terminal:
  - Day 2: nothing (the cipher day is pure terminal)
  - Day 3: `pip install pygame`, first thing in the morning
  - Days 4–5: nothing new; pygame carries through
  - Day 1 stretch only: `pip install pyfiglet`
- Print one [Field Notebook](https://silvermanjonathan.github.io/Secret-Spy-Academy/field_notebook_handout.html) per agent before Day 1; the pages send recruits to it all week, and Day 4 writes the Bug Hunt Log in it.
- Pages are self-paced with predict-before-reveal answers built in, so the teacher is never the bottleneck.

## House laws

- **One change per run.**
- **Read it, trace it, then run it.**
- Loops stay traceable: `for` loops are counted, and every `while` can point at the line that moves it toward no. A `while` with no visible exit is treated as a bug.
- Every window holds itself open with the same `while running` loop the game uses. No self-closing windows, no `pygame.time.wait`, no `pygame.event.pump`, no `pygame.font`: words live in the terminal, play lives in the window (the victory banner is drawn from racks of strings, square by square, precisely to keep that law).
- Excluded from the whole week by design: `return` values, dictionaries, classes, sprites/image files, file I/O, `try`/`except`, `break`, nested `if` gates.

## Pacing model

Novelty is front-loaded and decays to zero: Day 1 carries about ten mechanics in twelve drills, Day 2 adds three marks and builds a working cipher out of four named patterns, Day 3 adds one mark plus the pygame vocabulary and then plays and reads the capstone game, and Days 4 and 5 add nothing. Day 3 is the heaviest day; that is the price of a cipher day, paid knowingly. The capstone is paced backward: every ingredient it uses is owned at least one full day earlier, and the hub's teacher panel lists each one with the drill that taught it.

## Standards

Each page carries a collapsed teacher panel with verbatim standards, the teaching drills, the evidence collected, and where recruits actually stall. Verified claims: CCSS-M **5.OA.B.3** (Day 3, Addressed), **5.G.A.2** (Day 3), CSTA **E5-ALG-PS-01** (Day 4, reinforced Day 5). Four grade-5 CSTA PRO-progression codes remain marked `??` / *Needs verification* pending confirmation at the source viewer; confirm them before distributing any page. E5-SYS-SE-13 is deliberately not claimed.

Mapped to: Computer Science Teachers Association. (2026). *2026 CSTA PK–12 computer science standards.* https://csteachers.org/pk12standards/ · CC BY-NC-SA 4.0. Mathematics standards © 2010 NGA Center for Best Practices & CCSSO. "Mapped to" is this project's claim; it is not a CSTA- or CCSS-reviewed designation.

---

*Secret Spy Academy · Recruit Cohort · keep your Field Notebook close*
