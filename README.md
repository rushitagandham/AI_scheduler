# AI Scheduler Mockup

This repository contains a lightweight mockup for an AI-assisted scheduling flow requested by a Japanese e-learning client. Running the script prints a two-month progression plan (Levels 1–3) that alternates on-demand lessons, short quizzes, AI review days, and level-up checks.

## How to run

```bash
python main.py                       # print the fixed mockup table to stdout
python main.py --output schedule.md  # save the table to a Markdown file
python main.py --excel schedule.xlsx # export the schedule as an Excel workbook

# AI-personalized generator that adjusts durations/goals from simple heuristics
python main.py --ai-personalized --minutes-per-week 200 --focus conversation
```

The output is a Markdown-style table that can be copied into client-facing materials or attached as a demo asset. The Excel export keeps the same columns with auto-sized widths for easier readability.

## One-file version you can copy/paste
If you just need a single Python file to drop into a notebook or slide deck, copy `standalone_schedule.py` and run:

```bash
python standalone_schedule.py
```

It prints the same Markdown table without any external dependencies.
