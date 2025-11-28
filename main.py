"""Entry point for the AI scheduler mockup."""

import argparse
from pathlib import Path

from AI_scheduler.scheduler import build_schedule, render_schedule


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate the AI scheduling mockup")
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path to save the generated table as Markdown",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    schedule = build_schedule()
    output = "AIによる自動スケジュール案 (モックアップ)\n" + render_schedule(schedule)

    if args.output:
        args.output.write_text(output, encoding="utf-8")
        print(f"Saved schedule to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
