# My Python Learning Progress — Claude Onboarding Summary
> This file lives in my Claude project and is read automatically at the start of each session. No need to paste it.

---

## Who I am & my goal
My name is Jake Talbert. I'm a complete beginner learning Python and automation scripting with the goal of freelancing and earning $1,000+/month. I have 30–60 minutes per day to dedicate to learning (sometimes more).

## My setup
- **Office machine:** MacBook Pro, Apple M5 chip, 16GB RAM, macOS Tahoe 26.2 — primary work machine, used with an external monitor
- **Home machine:** MacBook Pro, Apple M3 Pro chip, 18GB RAM, macOS Tahoe 26.2 — secondary, now fully set up and synced
- Python 3.14.5 installed on both machines
- VS Code with the Python extension on both, Auto Save enabled, signed into GitHub
- Git installed on both (office + home), configured with name "Jake" / jtalbert1@gmail.com
- **Repo location (IMPORTANT — fixed June 16):** `~/python-projects/` — a dedicated, correctly-scoped repo on each machine. The repo is NO LONGER at home-folder root.
- GitHub account: `jtalbert1-sketch`
- GitHub repo: `github.com/jtalbert1-sketch/Python-projects` (note the **capital P**)
- Recurring sync workflow between machines: `git pull origin main` to get latest, `git push origin main` to share changes

## My learning plan
I'm following a structured 16-week routine broken into 3 phases:
- **Phase 1 (Weeks 1–4):** Python foundations — variables, loops, functions, files ✅ COMPLETE
- **Phase 2 (Weeks 5–10):** Automation skills — files, imports, spreadsheets, web scraping, browser automation, APIs, file bots ← CURRENTLY HERE
- **Phase 3 (Weeks 11–16):** Freelancing — Upwork/Fiverr profile, first client, retainers, scaling to $1k/mo

## Weekly routine
- Mon/Wed: Learn new concept (30 min) + code along (15 min)
- Tue: Practice (45 min)
- Thu/Fri: Project work (45–60 min)
- Sat: Weekly review (20–30 min)
- Sun: Rest day
*(Note: actual schedule has been flexible — catching up missed days on weekends, sometimes longer sessions when time allows.)*

## Where I am right now
- ✅ Phase 1 fully complete (Weeks 1–4) — variables, conditionals, loops, functions all mastered
- ✅ Functions retrospective quiz: 87.5% (up from 73% on Week 3 quiz)
- ✅ Phase 2 Day 1 — File handling (write/read, `with open()`, `print` vs `write`, `\n`, relative paths)
- ✅ Phase 2 Day 2 — Imports & modules (`import`, `module.function()`, `random`, `datetime`, append mode, built an activity log)
- ✅ Major infrastructure: repo scope fixed, both machines set up and synced
- **Next session:** Phase 2 Day 3 — likely CSV files (`import csv`), beginning the spreadsheets stage (flagged as the fastest realistic path to first freelance income)

## Phase 2 Roadmap (the path ahead)
Files → Spreadsheets → Web scraping → Browser automation → APIs → **AI Workflow Bridge** (capstone). Each stage builds on the last. Currently at the start, having completed the "files & imports" foundation.

## Things to review
All four Week 3 quiz items cleared ✅ — zero-based indexing, `and` vs `or`, `range()` excluding stop, `for` vs `while`.
One thing to keep sharp: `random.randint(a, b)` **includes** both ends, unlike `range()` which **excludes** the stop. Different tools, different rules.

## What I've learned so far

### Week 1 — Python Foundations
`print()`, variables (strings/ints/floats), f-strings, math with variables, updating variables, `input()`, `int()`, `float()`, `:.2f` formatting, common errors (TypeError, NameError, SyntaxError, IndentationError), running files with `python3 filename.py`, run shortcut Ctrl+F5 / ▷ button.

### Week 2 — Conditionals
`if`/`elif`/`else`, `and`/`or`, comparison operators (`>=`, `<=`, `>`, `<`, `==`, `!=`), indentation rules, top-to-bottom evaluation stopping at first true.

### Week 3 — Loops
`for i in range(n)`, `for item in list`, `while`, `!=`, incrementing, `+=`/`-=` (discovered independently), `break` (discovered independently), lists, zero-based indexing, ⌃C to stop, `range(start, stop, step)`, nested loops, tuples, `.lower()`, `.append()`.

### Week 4 — Functions (MASTERED)
`def`, parameters, `return`, calling functions, multiple parameters, returning multiple values (`return a, b` caught with `x, y = func()`), storing return values, `print` vs `return` (print displays and discards; return hands data back for reuse), functions calling other functions, modular code, layered building, choosing data types intentionally, product thinking (clarity for end user). Key insight fully locked: a function that only `print`s returns `None` when you try to capture it.

### Week 5 — Phase 2: Files & Imports (IN PROGRESS)

**Day 1 — File Handling:**
- `open(filename, "w")` — write mode, creates a file (overwrites if it exists)
- `with open(...) as file:` — clean file-handling pattern that auto-closes
- `file.write()` vs `print()` — write goes to a file on disk, print goes to the terminal; neither does the other's job
- `\n` — manual newline; a file is one continuous character stream, so the *position* of `\n` matters, not which `write()` call it's in
- `open(filename, "r")` and `file.read()` — read a file's contents back, returned for use in the program
- Full loop: write → file → read → print
- Relative paths depend on **where the script is run from** (current working directory), not where the file lives
- Real-world framing: terminal = workshop (debugging), file = product (deliverable)

**Day 2 — Imports & Modules:**
- `import` brings in pre-built toolkits from Python's standard library ("stem of the tree; tools branch off it")
- `module.function()` dot notation — reaching into a toolbox for a specific tool
- `import random` → `random.randint(1, 100)` (includes BOTH ends) and `random.choice(list)` (random pick)
- One import unlocks all tools in that toolbox; no need to re-import for each tool
- `import datetime` → `datetime.datetime.now()` — pulls the current time from the system clock (not random, not internet/location)
- Raw timestamp format: `2026-06-16 15:00:27.819162` (year-month-day, 24-hour time, microseconds)
- **Append mode `"a"`** — adds to the END of a file without overwriting (vs `"w"` which wipes it)
- **Built a real activity log** combining `datetime` + `file.write()` + `\n` + append mode — timestamps each run, the foundation of every backup/pipeline/scheduled bot
- Watch out for autocomplete inserting unwanted imports (caught a phantom `from asyncio import log`)

## Projects on GitHub (in `~/python-projects/`)

**phase1_foundations/** (8 portfolio projects):
1. `rate_calculator.py` — hourly rate needed to hit monthly income goal
2. `tip_calculator.py` — splits a bill with tip across people
3. `client_qualifier.py` — categorizes clients into service tiers by budget
4. `freelance_screener.py` — screens clients by budget + timeline with and/or logic
5. `savings_calculator.py` — simulates monthly savings to a goal with a while loop
6. `invoice_generator.py` — interactive invoice builder (loops, lists, tuples, conditionals)
7. `functions_practice.py` — functions, parameters, return values, modular client report generator
8. `project_estimator.py` — interactive freelance estimator using 4 modular functions

**phase2_automation/**:
- `file_handling.py` — write/read loop, the core file-handling demo
- `imports_intro.py` — random + datetime + append-mode activity log
- *(`activity_log.txt` is generated output — intentionally NOT committed; not source code)*

**practice/** (local scratch work, not all pushed): `functions_warmup.py`, `functions_deep_dive.py`, `functions_fundamentals.py`, `functions_practice_2.py`, `loops_advanced.py`, `loops_practice.py`, `loops_practice_2.py`, `conditionals_practice.py`, `conditions_advanced.py`, `hello.py`

## Key milestones
- ✅ Weeks 1–4 complete; functions mastered; Phase 1 done
- ✅ 8 polished projects on GitHub, organized into phase folders
- ✅ Repo scope fixed + two machines synced (June 16)
- ✅ Phase 2 started (file handling + imports)
- 🔲 End of Week 10: portfolio with 3+ polished automation projects
- 🔲 Week 10–11: AI Workflow Bridge capstone
- 🔲 Week 12–13: first paid client
- 🔲 Week 14–16: $500/month
- 🔲 Month 5–6: $1,000+/month

## Longer term goal project
**AI Workflow Bridge** — a Python script that connects to an AI API to analyze text data, displayed on a Streamlit dashboard. Target: Week 10–11. Built entirely on imports (the API client and Streamlit are both imported libraries) and the modular function + file-handling patterns Jake is building now.

## Planned next steps
- **Phase 2 Day 3:** likely CSV files (`import csv`) — beginning the spreadsheets stage
- **Minor:** verify the office machine's git identity matches (Jake / jtalbert1@gmail.com) so commits attribute consistently across both machines
- **On the horizon:** Install Claude Code (overdue — bring up soon now that Phase 1 is done and environment is clean)
- **Later in Phase 2:** `.gitignore` (to formally tell git to ignore generated files like `activity_log.txt`)

## Preferences & notes
- Jake shares VS Code screenshots each session to show progress and verify output
- The **predict-then-verify** pattern works extremely well — Jake explains expected output in his own words before running, then compares to reality. Keep using it.
- The **back-and-forth conceptual dialogue** (explain → check understanding → run → confirm) genuinely helps his retention — he's said so directly
- Jake does extra credit when time allows — offer it at session end
- Jake sometimes rushes and makes small typos/indentation errors — a quick visual scan before running helps (he catches most himself)
- Jake learns well by experimenting and tweaking — he often tries variations unprompted; encourage this
- Jake asks strong conceptual "why" questions that connect new material to prior lessons — lean into these
- At the end of each session, share a **real-world Python use case** relevant to what was learned (recurring request)
- Coaching tone, plain-English analogies, step-by-step, beginner-friendly. Never rush — depth over speed, especially as complexity rises. Honor "slow down" requests without judgment.
- Jake is thinking like a developer, not just a coder — connect concepts to the AI Workflow Bridge goal; he caught a real repo-scope/security issue himself, showing strong instinct
- **Update this progress report + vocab sheet automatically after each session** (don't make Jake do it manually)
- Jake builds a YouTube habit to supplement learning; his friend Blake is also learning to code and active on GitHub
- Claude is saved as a project — this file auto-loads, no need to paste it

## How Claude should pick up
Start each session as Jake's Python learning coach. Check the day of week against the weekly routine. Ask to see his screen via screenshot when helpful. Use predict-then-verify and back-and-forth dialogue. Offer extra credit if time allows. End each session with a real-world Python use case. Never rush — Jake prefers depth over speed. Always connect new concepts to the AI Workflow Bridge goal where relevant.

---

# Python Vocab Master Sheet
*Updated through Week 5 Day 2 (Phase 2) — added to after every session*

## Core Python Concepts
**`print()`** — displays output in the terminal.
**`input()`** — pauses and waits for user to type; always returns a string.
**`int()` / `float()`** — convert text to a whole number / decimal number.
**`str` / `int` / `float`** — string (text) / integer (whole number) / decimal number.
**`variable`** — a named container storing a value.
**`f-string`** — string prefixed with `f` that embeds variables in `{}`.
**`:.2f`** — formats a float to 2 decimal places inside an f-string.
**`\n`** — newline character; inserts a line break wherever it sits in a string. Goes wherever you put it (terminal or file).
**`comment`** — a `#` line Python ignores; for humans.

## Functions
**`def`** — defines a reusable block of code.
**`parameter`** — the input slot in a definition (`def greet(name):` → `name`).
**`argument`** — the actual value passed when calling (`greet("Jake")` → `"Jake"`).
**`return`** — hands a value back out of the function to be stored/reused. (A function that only `print`s returns `None`.)
**`returning multiple values`** — `return a, b`, caught with `x, y = func()`.
**`calling a function`** — running it with `name()`.
**`modular code`** — small reusable functions, each doing one job; functions can call other functions.
**`print vs return`** — print displays and discards; return hands the value back for reuse.

## Conditionals
**`if` / `elif` / `else`**, **`and`** (both true), **`or`** (at least one true), **`==`** (compare), **`!=`**, **`>=`**, **`<=`**, **`indentation`** (controls what's inside a block).

## Loops & Lists
**`for loop`**, **`while loop`**, **`range(n)`** (0 to n-1), **`range(start, stop, step)`** (excludes stop), **`list`** `[]`, **`tuple`** `()`, **`zero-based indexing`** (index is an address, starts at 0; last item = count − 1), **`break`**, **`+=` / `-=`**, **`infinite loop`** / **`⌃C`**, **`nested loop`**, **`.append()`**, **`.lower()`**, **`enumerate()`**.

## Imports & Modules (NEW — Phase 2)
**`import`** — brings a pre-built toolkit (module/library) into your script. Goes at the top.
**`module` / `library`** — a toolkit of pre-written tools (functions) you import instead of building from scratch.
**`standard library`** — the hundreds of toolkits that ship with Python, ready to import.
**`module.function()`** — dot notation: reach into a toolbox (`module`) for a specific tool (`function`). One import unlocks all tools in that box.
**`random`** — toolbox for randomness. `random.randint(a, b)` → random whole number, **includes both ends**. `random.choice(list)` → random item from a list.
**`datetime`** — toolbox for dates/times. `datetime.datetime.now()` → current date+time from the system clock. Raw format: `YYYY-MM-DD HH:MM:SS.microseconds`, 24-hour.

## File Handling (NEW — Phase 2)
**`open(filename, mode)`** — opens (or creates) a file.
**`with open(...) as file:`** — clean pattern that auto-closes the file when done.
**`"w"` (write mode)** — creates the file; **overwrites** existing contents.
**`"r"` (read mode)** — reads an existing file.
**`"a"` (append mode)** — adds to the END without erasing existing contents (used for logs).
**`file.write("...")`** — writes text into the file (no automatic newline — add `\n` yourself).
**`file.read()`** — returns the whole file's contents as one string.
**`relative path`** — a bare filename is relative to where the script is RUN from (current working directory), not where the .py file lives.
**`activity log`** — a file that records timestamped entries each run (datetime + write + append).

## Errors
**`SyntaxError`** (broken grammar / stray punctuation), **`TypeError`** (wrong data type), **`NameError`** (undefined variable / typo), **`IndentationError`** (usually rushing), **`ValueError`** (wrong kind of value), **`KeyboardInterrupt`** (⌃C manual stop), **`debug`** (find & fix errors).

## Tools & Environment
**`terminal / CLI`**, **`GUI`**, **`script`**, **`VS Code`**, **`autocomplete`** (helpful, but can insert unwanted imports — watch it), **VS Code window ≠ files on disk** (closing the window never deletes files).

## Terminal/Shell Commands (NEW)
**`cd`** (change directory; `cd ~` jumps to home, `cd ..` goes up one), **`ls`** (list contents), **`mkdir`** (make folder(s)), **`rmdir`** (remove an EMPTY folder — safe), **`mv`** (move/rename), **`cp`** (copy, leaves original), **`*` wildcard** (`*.py` = every .py file), **`rm -rf`** (force-delete a folder and contents — irreversible, use with care), **`zsh` vs `bash`** (office uses zsh `%`, home uses bash `$` — same commands work).

## Git & GitHub
**`Git`** (tracks changes), **`GitHub`** (online repo host), **`repo`** (a folder tracked by Git — should be a DEDICATED project folder, not your home directory), **`commit`** (snapshot + message), **`push`** / **`pull`**, **`rebase`** (`git pull origin main --rebase`), **`clone`** (`git clone <URL>` — downloads a full repo with history), **`git status`** (shows changes; "working tree clean" = healthy), **`git ls-files`** (lists exactly what's tracked), **`git config --global user.name/.email`** (commit identity), **`renamed:`** (git recognizing a moved file, preserves history), **`.gitignore`** (tells git to ignore files like generated output — coming later), **`README`**, **`branch`** (`main`).

## Industry Terms
**`SaaS`**, **`open source`**, **`stack`**, **`dashboard`**, **`framework`** (Flask, Streamlit), **`API`**, **`scraping`**, **`Streamlit`**, **`CRM`**, **`coder vs developer`** (coder writes syntax; developer thinks in systems and works backward from a goal — Jake is already doing this).
