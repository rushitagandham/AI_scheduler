from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Iterable, List


@dataclass(frozen=True)
class ScheduledItem:
    level: int
    week: int
    day: str
    activity: str
    module: str
    duration_minutes: int
    goal: str

    def to_row(self) -> dict:
        """Return a dict representation for export or JSON serialization."""
        return asdict(self)


def _level_block(level: int, start_week: int, start_lesson: int) -> List[ScheduledItem]:
    goals = {
        1: "Reach 90%+ accuracy on vocabulary and basic patterns with AI teaching support",
        2: "Stabilize short-form output while using voice input",
        3: "Validate practical skills through N4-level reading and listening",
    }
    goal = goals.get(level, "Strengthen the fundamentals to move to the next level")
    template = [
        ("On-demand lesson", 30),
        ("Quiz", 30),
    ]

    items: List[ScheduledItem] = []
    lesson_number = start_lesson

    for block_index in range(3):
        week = start_week + (block_index // 2)
        day_base = (block_index % 2) * 3

        for day_index, (activity, minutes) in enumerate(template, start=1):
            items.append(
                ScheduledItem(
                    level=level,
                    week=week,
                    day=f"Week{week}-Day{day_base + day_index}",
                    activity=activity,
                    module=f"L{level}-{lesson_number}",
                    duration_minutes=minutes,
                    goal=goal,
                )
            )

        items.append(
            ScheduledItem(
                level=level,
                week=week,
                day=f"Week{week}-Day{day_base + 3}",
                activity="Buffer / AI review",
                module=f"L{level}-{lesson_number} Review",
                duration_minutes=30,
                goal=goal,
            )
        )

        lesson_number += 1

    items.append(
        ScheduledItem(
            level=level,
            week=week,
            day=f"Week{week}-Day7",
            activity="Level-up test",
            module=f"Level{level}→Level{level + 1}",
            duration_minutes=60,
            goal="Confirm 80%+ mastery and advance to the next level",
        )
    )

    return items


def build_schedule() -> List[ScheduledItem]:
    """Create the fixed two-month schedule used for the mockup demo."""

    schedule: List[ScheduledItem] = []
    schedule.extend(_level_block(level=1, start_week=1, start_lesson=1))
    schedule.extend(_level_block(level=2, start_week=3, start_lesson=4))
    schedule.extend(_level_block(level=3, start_week=5, start_lesson=7))
    return schedule


def build_ai_schedule(
    available_minutes_per_week: int = 180,
    focus_area: str = "balanced",
    weeks: int = 6,
) -> List[ScheduledItem]:
    """Create a lightly personalized schedule tuned by simple AI-inspired heuristics.

    The generator adjusts daily durations based on available minutes per week and
    annotates goals with the requested focus area. It keeps the same tabular shape
    as the mockup schedule so it can be exported the same way.
    """

    if available_minutes_per_week <= 0:
        raise ValueError("available_minutes_per_week must be greater than zero")

    focus_goals = {
        "conversation": "Prioritize voice input and conversation practice to automate speaking output",
        "reading": "Tackle short reading passages each week to reinforce vocabulary",
        "exam": "Include practice tests to target score improvements",
        "balanced": "Balance input and output to reinforce learning",
    }
    goal = focus_goals.get(focus_area, focus_goals["balanced"])

    # Give learners at least 20 minutes/day, cap at 90 minutes to keep sessions short.
    daily_minutes = min(90, max(20, available_minutes_per_week // 5))

    schedule: List[ScheduledItem] = []
    lesson_number = 1

    for week in range(1, weeks + 1):
        level = 1 + (week - 1) // 2
        week_goal = f"{goal} (AI suggested pace: {daily_minutes} min/day)"

        # Five-day cadence that rotates learning, assessment, AI review, and practice.
        activities = [
            ("On-demand lesson", daily_minutes, f"L{level}-{lesson_number}"),
            (
                "Quiz",
                max(20, daily_minutes - 10),
                f"L{level}-{lesson_number} Check quiz",
            ),
            (
                "AI review / refresh",
                min(30, daily_minutes),
                f"L{level}-{lesson_number} Review notes",
            ),
            (
                "Focus practice",
                daily_minutes,
                f"{focus_area.capitalize()} practice L{level}-{lesson_number}",
            ),
            (
                "Integrated check",
                min(60, daily_minutes + 10),
                f"L{level}-{lesson_number} Integrated exercise",
            ),
        ]

        for day_index, (activity, minutes, module) in enumerate(activities, start=1):
            schedule.append(
                ScheduledItem(
                    level=level,
                    week=week,
                    day=f"Week{week}-Day{day_index}",
                    activity=activity,
                    module=module,
                    duration_minutes=minutes,
                    goal=week_goal,
                )
            )

        lesson_number += 1

    return schedule


def render_schedule(rows: Iterable[ScheduledItem]) -> str:
    """Render the schedule as a Markdown-friendly table."""

    header = ["Level", "Week", "Day", "Activity", "Module", "Duration(min)", "Goal"]
    lines = [" | ".join(header), " | ".join(["---"] * len(header))]

    for item in rows:
        lines.append(
            " | ".join(
                [
                    str(item.level),
                    str(item.week),
                    item.day,
                    item.activity,
                    item.module,
                    str(item.duration_minutes),
                    item.goal,
                ]
            )
        )

    return "\n".join(lines)


__all__ = [
    "ScheduledItem",
    "build_ai_schedule",
    "build_schedule",
    "render_schedule",
]
