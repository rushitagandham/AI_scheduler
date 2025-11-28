# Automated schedule mockup

This document sketches a mockup where AI automatically builds and shares a learning plan based on client requirements. It fixes online class dates and assignment deadlines, then mixes on-demand viewing, quizzes, review, and level-up checks.

## Concept
- Define learning goals and success criteria (90%+ accuracy, AI reminders) per level
- Propose a baseline pace of two 30-minute blocks per day
- Auto-notify "Today's tasks" and "Today's content" and copy instructors on late submissions
- Combine voice input with chat questions, with English/Chinese support in mind

## Schedule output example
Running `python main.py` produces a table like this:

```
AI-generated schedule draft (mockup)
Level | Week | Day | Activity | Module | Duration(min) | Goal
--- | --- | --- | --- | --- | --- | ---
1 | 1 | Week1-Day1 | On-demand lesson | L1-1 | 30 | Reach 90%+ accuracy on vocabulary and basic patterns with AI teaching support
1 | 1 | Week1-Day2 | Quiz | L1-1 | 30 | Reach 90%+ accuracy on vocabulary and basic patterns with AI teaching support
1 | 1 | Week1-Day3 | Buffer / AI review | L1-1 Review | 30 | Reach 90%+ accuracy on vocabulary and basic patterns with AI teaching support
...
```

## Screen ideas (text-only)
- **Today's task**: "Watch On-demand L1-2 for 30 minutes" / Due: 23:59 / Email instructor if late
- **Today's online class**: 19:00-19:30 with a prebooked Zoom link
- **AI Q&A chat**: Ask questions in Japanese, English, or Chinese with a voice-input button
- **Notifications**: Remind via LINE/email when deadlines approach and tasks remain incomplete

## Client talking points
1. **Fixed slots plus auto-fill**: Lock class-day slots and let AI allocate remaining time to on-demand/quiz/review
2. **Progress alerts**: Detect overdue work or low scores and notify both instructors and learners
3. **Flexible rescheduling**: Drag-and-drop changes trigger a recalculated AI proposal
4. **Evidence**: Export reports for quiz accuracy, viewing completion, and question history

Use this mockup as a starting point for client demos or screen prototyping.
