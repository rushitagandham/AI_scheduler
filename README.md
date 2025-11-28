diff --git a/README.md b/README.md
index e69de29bb2d1d6434b8b29ae775ad8c2e48c5391..e2b778abc56eb2d2f3238647c234254665f1db86 100644
--- a/README.md
+++ b/README.md
@@ -0,0 +1,21 @@
+# AI Scheduler Mockup
+
+This repository contains a lightweight mockup for an AI-assisted scheduling flow requested by a Japanese e-learning client. Running the script prints a two-month progression plan (Levels 1–3) that alternates on-demand lessons, short quizzes, AI review days, and level-up checks.
+
+## How to run
+
+```bash
+python main.py            # print the table to stdout
+python main.py --output schedule.md  # save the table to a Markdown file
+```
+
+The output is a Markdown-style table that can be copied into client-facing materials or attached as a demo asset.
+
+## One-file version you can copy/paste
+If you just need a single Python file to drop into a notebook or slide deck, copy `standalone_schedule.py` and run:
+
+```bash
+python standalone_schedule.py
+```
+
+It prints the same Markdown table without any external dependencies.
