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
| 2 | [The Cipher Room](https://silvermanjonathan.github.io/Secret-Spy-Academy/day2_cipher_room.html) | the tally, the counter with a gate, best-so-far, `==`/`!=`, `while` & the sentinel gate, first pygame windows, the `while running` loop and the frame tally | The Evidence Log + the Patrol Drone |
| 3 | [The Gadget Blueprint](https://silvermanjonathan.github.io/Secret-Spy-Academy/day3_gadget_blueprint.html) | `def` & parameters, `append`, `random.randint`; reading the engine's patterns | The Blueprint Rehearsal + the initialed engine |
| 4 | [The Gadget Commission](https://silvermanjonathan.github.io/Secret-Spy-Academy/day4_gadget_commission.html) | zero new syntax: the Gadget Schematic & two worked changes (alert mode, the lock ring) | Your Commissioned Gadget: a customized [Tracker Scope](https://silvermanjonathan.github.io/Secret-Spy-Academy/tracker_scope_pygame.py) |
| 5 | [The Bug Hunt & the Final Debrief](https://silvermanjonathan.github.io/Secret-Spy-Academy/day5_bug_hunt.html) | zero new syntax: the five-step protocol & the VS Code debugger | The Bug Hunt Log + the Final Debrief |

The Commission is **due by the end of Day 4**. Day 5 is reserved for debugging and the Debrief. Side missions (the Cipher Grid, the Safecracker's Ledger, the Remote, a second gadget) are listed on the hub and sealed until they ship.

## Files

Flat repo, no build step. Ship everything together; the hub must always be re-uploaded alongside any new or changed page.

```
README.md                        ← you are here (site root)
spy_academy_hub.html             ← the front door
day1_induction_day.html
day2_cipher_room.html
day3_gadget_blueprint.html
day4_gadget_commission.html
day5_bug_hunt.html
tracker_scope_pygame.py          ← the Day 4 engine, byte-identical to the Day 3 in-page listing
field_notebook_handout.html      ← the printable Field Notebook (trace sheets and the Bug Hunt Log, one per agent)
```

## Student setup

- VS Code with the Python extension, Python 3.10+ (the traceback "Did you mean" hint assumes 3.10+; the "Did you forget to import" hint shown on Day 5 appears on 3.12+, and nothing depends on it).
- Installs happen the day they're needed, in the VS Code terminal:
  - Day 2: `pip install pygame` (and `pip install rich` for the stretch tier)
  - Days 3–5: nothing new; pygame carries through
  - Day 1 stretch only: `pip install pyfiglet`
- Print one [Field Notebook](https://silvermanjonathan.github.io/Secret-Spy-Academy/field_notebook_handout.html) per agent before Day 1; the pages send recruits to it all week, and Day 5 writes the Bug Hunt Log in it.
- Pages are self-paced with predict-before-reveal answers built in, so the teacher is never the bottleneck.

## House laws

- **One change per run.**
- **Read it, trace it, then run it.**
- Loops stay traceable: `for` loops are counted, and every `while` can point at the line that moves it toward no. A `while` with no visible exit is treated as a bug.
- Every window holds itself open with the same `while running` loop the engine uses. No self-closing windows, no `pygame.time.wait`, no `pygame.event.pump`, no `pygame.font`: words live in the terminal, play lives in the window.
- Excluded from the whole week by design: `return` values, dictionaries, classes, sprites/image files, file I/O, `try`/`except`, `break`, nested `if` gates.

## Pacing model

Novelty is front-loaded and decays to zero: Day 1 carries about ten mechanics in twelve drills, Day 2 names four patterns and adds three marks, Day 3 adds exactly two marks and spends the rest of the day reading, and Days 4 and 5 add nothing. The Day 4 engine is paced backward: every ingredient it uses is owned at least one full day earlier, and the hub's teacher panel lists each one with the drill that taught it.

## Standards

Each page carries a collapsed teacher panel with verbatim standards, the teaching drills, the evidence collected, and where recruits actually stall. Verified claims: CCSS-M **5.OA.B.3** (Day 2), **5.G.A.2** (Day 3, reinforced Day 4), CSTA **E5-ALG-PS-01** (Day 4). Four grade-5 CSTA PRO-progression codes remain marked `??` / *Needs verification* pending confirmation at the source viewer; confirm them before distributing any page. E5-SYS-SE-13 is deliberately not claimed.

Mapped to: Computer Science Teachers Association. (2026). *2026 CSTA PK–12 computer science standards.* https://csteachers.org/pk12standards/ · CC BY-NC-SA 4.0. Mathematics standards © 2010 NGA Center for Best Practices & CCSSO. "Mapped to" is this project's claim; it is not a CSTA- or CCSS-reviewed designation.

---

*Secret Spy Academy · Recruit Cohort · keep your Field Notebook close*
