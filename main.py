diff --git a/main.py b/main.py
index 482c8d4995d831ee553dfe3e22fd9f6a257ee7de..9f98dce54ec7234e08868ebc1493158b70edf518 100644
--- a/main.py
+++ b/main.py
@@ -1,6 +1,32 @@
-def main():
-    print("Hello from ai-scheduler!")
+"""Entry point for the AI scheduler mockup."""
+
+import argparse
+from pathlib import Path
+
+from scheduler import build_schedule, render_schedule
+
+
+def parse_args() -> argparse.Namespace:
+    parser = argparse.ArgumentParser(description="Generate the AI scheduling mockup")
+    parser.add_argument(
+        "--output",
+        type=Path,
+        help="Optional path to save the generated table as Markdown",
+    )
+    return parser.parse_args()
+
+
+def main() -> None:
+    args = parse_args()
+    schedule = build_schedule()
+    output = "AIによる自動スケジュール案 (モックアップ)\n" + render_schedule(schedule)
+
+    if args.output:
+        args.output.write_text(output, encoding="utf-8")
+        print(f"Saved schedule to {args.output}")
+    else:
+        print(output)
 
 
 if __name__ == "__main__":
     main()
