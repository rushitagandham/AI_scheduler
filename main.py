"""Entry point for the AI scheduler mockup."""

import argparse
from pathlib import Path

from AI_scheduler import ScheduledItem, build_schedule, render_schedule
from AI_scheduler.excel import export_schedule_to_excel


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate the AI scheduling mockup")
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path to save the generated table as Markdown",
    )
    parser.add_argument(
        "--excel",
        type=Path,
        help="Optional path to save the generated schedule as an Excel file",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    schedule = build_schedule()
    output = "AIによる自動スケジュール案 (モックアップ)\n" + render_schedule(schedule)

    if args.output:
        args.output.write_text(output, encoding="utf-8")
        print(f"Saved schedule to {args.output}")

    if args.excel:
        export_schedule_to_excel(schedule, args.excel)
        print(f"Saved schedule to {args.excel}")

    if not args.output:
        print(output)


if __name__ == "__main__":
    main()
