"""Entry point for the AI scheduler mockup."""

import argparse
from pathlib import Path

from AI_scheduler import (
    ScheduledItem,
    build_ai_schedule,
    build_schedule,
    render_schedule,
)
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
    parser.add_argument(
        "--ai-personalized",
        action="store_true",
        help="Use the AI-tuned heuristic generator instead of the fixed mockup",
    )
    parser.add_argument(
        "--minutes-per-week",
        type=int,
        default=180,
        help="Weekly study minutes for the AI generator (default: 180)",
    )
    parser.add_argument(
        "--focus",
        default="balanced",
        help="Focus area for the AI generator (balanced, conversation, reading, exam)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.ai_personalized:
        schedule = build_ai_schedule(
            available_minutes_per_week=args.minutes_per_week,
            focus_area=args.focus,
        )
        title = "AI Personalized Schedule"
    else:
        schedule = build_schedule()
        title = "AI Auto-Generated Schedule (Mockup)"

    output = f"{title}\n" + render_schedule(schedule)

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
