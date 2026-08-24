# Week 13: Human-in-the-Loop Analytics

**Lecture:** Nov 16 · **Practical:** Nov 18 · **Module 3**

## Learning objectives (from syllabus)

- Design human-centered AI workflows
- Apply oversight to AI-assisted analysis

## Lecture outline

1. **Human-in-the-loop (HITL) systems** (20 min) — what HITL means
   concretely: checkpoints where a human reviews/approves/corrects before
   a pipeline proceeds, rather than full automation.
2. **Integrating AI into analytical workflows** (20 min) — where HITL
   checkpoints naturally fit in a pipeline (e.g., after AI-assisted data
   extraction, before it feeds a statistical model) — ties back to Week 10
   workflow management concepts directly.
3. **Transparency and validation in AI-assisted analysis** (20 min) —
   logging what AI did, making it inspectable/auditable, not just trusting
   a final output.

## Hands-on exercise (in class, ungraded)

Add validation checkpoints to an AI-assisted workflow — take a simple
existing pipeline (can reuse the Lab 5 structure) and insert an explicit
human-review step with clear accept/reject criteria.

## Connections

This is the conceptual capstone of the course's "required but supervised
AI use" theme running since Week 1 — good week for an explicit callback to
the syllabus's Generative AI policy and to ask students to reflect on how
their own practice has (or hasn't) matched it so far.

## Discussion prompt

"Where in your final project would an AI mistake be low-stakes vs.
high-stakes? Where did you actually put a checkpoint, and does it match?"
