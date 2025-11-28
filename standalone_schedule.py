"""Standalone schedule generator for quick copy/paste demos."""
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
        return asdict(self)


def _level_block(level: int, start_week: int, start_lesson: int) -> List[ScheduledItem]:
    goals = {
        1: "Reach 90%+ accuracy on vocabulary and basic patterns with AI teaching support",
        2: "Stabilize short-form output while using voice input",
        3: "Validate practical skills through N4-level reading and listening",
    }
    goal = goals.get(level, "Strengthen the fundamentals to move to the next level")
    template = [("On-demand lesson", 30), ("Quiz", 30)]

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
    schedule: List[ScheduledItem] = []
    schedule.extend(_level_block(level=1, start_week=1, start_lesson=1))
    schedule.extend(_level_block(level=2, start_week=3, start_lesson=4))
    schedule.extend(_level_block(level=3, start_week=5, start_lesson=7))
    return schedule


def render_schedule(rows: Iterable[ScheduledItem]) -> str:
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


def main() -> None:
    schedule = build_schedule()
    print("AI-generated schedule draft (mockup)")
    print(render_schedule(schedule))


if __name__ == "__main__":
    main()
