"""Streamlit frontend to visualize the AI study schedule on a calendar."""

from __future__ import annotations

from datetime import date, datetime, time, timedelta
from typing import Iterable

import pandas as pd
import plotly.express as px
import streamlit as st

from AI_scheduler import ScheduledItem, build_ai_schedule, build_schedule

st.set_page_config(page_title="AI Scheduler Calendar", layout="wide")


def _parse_day_number(day_label: str) -> int:
    """Extract the numeric portion from a day label like "Week1-Day3"."""

    for part in day_label.split("-"):
        if part.startswith("Day"):
            number = part.replace("Day", "")
            if number.isdigit():
                return int(number)
    return 1


def _to_dataframe(items: Iterable[ScheduledItem], start: date) -> pd.DataFrame:
    """Convert scheduled items to a tabular DataFrame with calendar metadata."""

    rows = []
    for item in items:
        day_number = _parse_day_number(item.day)
        event_date = start + timedelta(days=(item.week - 1) * 7 + day_number - 1)
        start_at = datetime.combine(event_date, time(hour=9))
        end_at = start_at + timedelta(minutes=item.duration_minutes)

        rows.append(
            {
                "Level": item.level,
                "Week": f"Week {item.week}",
                "Day": item.day,
                "Date": event_date,
                "Activity": item.activity,
                "Module": item.module,
                "Duration (min)": item.duration_minutes,
                "Goal": item.goal,
                "Start": start_at,
                "End": end_at,
                "Day number": day_number,
            }
        )

    return pd.DataFrame(rows)


def _render_calendar(df: pd.DataFrame) -> None:
    """Render a Plotly timeline that acts as a calendar visualization."""

    if df.empty:
        st.info("No schedule items to display.")
        return

    fig = px.timeline(
        df,
        x_start="Start",
        x_end="End",
        y="Week",
        color="Activity",
        hover_name="Module",
        hover_data={
            "Date": "|%b %d",  # format date in tooltip
            "Goal": True,
            "Duration (min)": True,
            "Day": True,
        },
    )
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(margin=dict(l=20, r=20, t=20, b=20))
    st.plotly_chart(fig, use_container_width=True)


def _render_table(df: pd.DataFrame) -> None:
    """Render the tabular representation of the schedule."""

    display = df.sort_values(["Date", "Day number"])[
        ["Date", "Week", "Day", "Activity", "Module", "Duration (min)", "Goal"]
    ]
    st.dataframe(display, use_container_width=True, hide_index=True)


def main() -> None:
    st.title("AI Scheduler calendar demo")
    st.write(
        "Choose a start date and schedule type to view the study plan on a calendar "
        "and in a sortable table."
    )

    with st.sidebar:
        st.header("Controls")
        start_date = st.date_input("Schedule start date", value=date.today())
        schedule_type = st.radio(
            "Schedule mode",
            ["Fixed mockup", "AI-personalized"],
            help="Select the classic mockup or the adaptive AI-driven schedule.",
        )

        if schedule_type == "AI-personalized":
            weekly_minutes = st.slider(
                "Minutes per week", min_value=60, max_value=600, value=180, step=10
            )
            weeks = st.slider("Number of weeks", min_value=2, max_value=12, value=6)
            focus = st.selectbox(
                "Focus area",
                ["balanced", "conversation", "reading", "exam"],
                help="Influences the goals and practice modules for each week.",
            )

            schedule = build_ai_schedule(
                available_minutes_per_week=weekly_minutes,
                focus_area=focus,
                weeks=weeks,
            )
            st.caption(
                "AI-personalized pacing with adjustable weekly minutes and focus area."
            )
        else:
            schedule = build_schedule()
            start_date = start_date  # keep explicit for clarity
            st.caption("Two-month mockup schedule across Levels 1–3.")

    df = _to_dataframe(schedule, start_date)

    st.subheader("Calendar")
    _render_calendar(df)

    st.subheader("Daily schedule")
    _render_table(df)

    st.markdown(
        "Tip: Use Streamlit's native download option in the chart or table menu to "
        "export the calendar or data as an image or CSV."
    )


if __name__ == "__main__":
    main()
