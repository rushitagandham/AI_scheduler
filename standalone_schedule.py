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
        1: "AIの講師サポートを活用しながら、単語と基本文型を90%以上正答する",
        2: "音声入力を併用し、短文のアウトプットを安定させる",
        3: "N4レベルの読解・聴解を通じて実践運用を確認する",
    }
    goal = goals.get(level, "次のレベルに進むための基礎を固める")
    template = [("オンデマンド", 30), ("小テスト", 30)]

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
                activity="予備日 / AIレビュー",
                module=f"L{level}-{lesson_number}復習",
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
            activity="レベルアップテスト",
            module=f"Level{level}→Level{level + 1}",
            duration_minutes=60,
            goal="学習到達度80%以上を確認して次のレベルへ進む",
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
    print("AIによる自動スケジュール案 (モックアップ)")
    print(render_schedule(schedule))


if __name__ == "__main__":
    main()
