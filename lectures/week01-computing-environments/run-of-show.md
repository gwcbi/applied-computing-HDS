# Week 1 Lecture — Run of Show
**Monday, Aug 24, 2026 · 12:45–2:00 p.m. · SPH 300 · PUBH 6854 / PUBH 4201 (combined)**

Deck: `W01L_slides.pptx` (20 slides, full speaker notes on each). This sheet is the printable timing/talking-points version.

**Heads up on pacing:** the full deck now runs ≈85 min against a 75-min slot — see the trim path at the bottom if you need to land on time exactly.

| Time | Min | Segment | Key points | Slide(s) |
|---|---|---|---|---|
| 12:45 | 5 | **Welcome & framing** | Not a programming-language class — building trustworthy, reproducible workflows for health data. | 1–2 |
| 12:50 | 5 | **HDS is a broad field** | Six domains (genomics, clinical/EHR, epi/pop health, biostat/trials, imaging, policy). Be explicit: your background is computational genomics, that's one path among many in the room. | 3 |
| 12:55 | 7 | **Icebreaker** | Show-of-hands poll on domains → pair share (domain + one intimidating computational task) → 2–3 popcorn share-outs. Flag it as a seed for their final-project thinking. | 4 |
| 1:02 | 3 | **Semester at a glance** | Quick pass on the 3 modules — we're in Module 1. | 5 |
| 1:05 | 4 | **Syllabus & grading** | Walk the grading donut: Labs 45%, Final Project 40%, Quizzes 10%, Participation 5%. | 6 |
| 1:09 | 4 | **Class policies** | AI use required *and* documented (this is graded, not a footnote). Collaboration: discuss freely, submit your own work. Late work −10%/day. | 7 |
| 1:13 | 5 | **Final project — what it is** | 40% of grade, teams of 2–3, three project types (analysis workflow / software package / database app) with concrete examples. Prompt: pick something in your own domain. | 8 |
| 1:18 | 4 | **Final project — timeline** | Today → Oct 7 proposal → Wks 11–14 project time → Dec 9 presentations. Explicit ask: jot 2–3 problem ideas from their own field before Week 7. | 9 |
| 1:22 | 2 | **Agenda for the rest of today** | Set expectations: shell/remote-dev/coding-env get lighter treatment today since Wednesday's practical is hands-on for all of it. | 10 |
| 1:24 | 12 | **UNIX shell review** | Compressed — poll comfort, hit highlights only (navigation, pipes/redirection, grep/sed/awk, permissions, ssh). Defer depth to Wednesday. | 11–12 |
| 1:36 | 15 | **Remote development & Pegasus HPC** | Why remote (scale/sensitivity/compute) → Pegasus specifics: `ssh netid@pegasus.arc.gwu.edu`, GW NetID, VPN/campus network, SLURM. **Say explicitly: request access today.** Brief tools mention (VS Code Remote-SSH, Jupyter, RStudio Server). | 13–15 |
| 1:51 | 10 | **R and Python overview** | Map, not tutorial. R = stats/tidyverse/biostat. Python = general-purpose/ML/bioinformatics. Fluency in both is a course goal. | 16 |
| 2:01 | 8 | **Coding environments tour** | Quick live tour: same script in RStudio, VS Code, JetBrains. First thing to cut if short on time. | 17 |
| — | 2 | **Discussion prompt** | "You've inherited a collaborator's folder — no README, inconsistent naming. What's the first thing you'd want to know?" Let it hang — sets up Week 2. | 18 |
| ~2:09 | — | **Looking ahead / wrap-up** | Wed Aug 26 practical (shell checklist + SSH into Pegasus + VS Code Remote-SSH + experience self-report). Lab 1 assigned next week. Four to-dos before Wednesday, incl. creating a GitHub account and adding their username to the shared Google Doc — mention the free GitHub Student Developer Pack (education.github.com/pack). Note explicitly that local git setup is Wednesday's topic, not today's. | 19–20 |

## If you need to hit 75 minutes exactly
Cut, in this order:
1. **Coding-environments tour (slide 17, −8 min)** — defer to a one-line mention; students will touch all three tools eventually anyway.
2. **Shell review (slides 11–12, −12 → −5 min)** — show the terminal-card slide only, skip the topic-by-topic walkthrough; Wednesday's practical is the real hands-on pass.
3. **Icebreaker pair-share (slide 4, −7 → −4 min)** — shorten to 1 min of pair talk instead of 2–3.
That gets you back to ~75 min without touching the new orientation content (HDS landscape, syllabus/policies, final project), which only gets covered once.

## Before you walk in
- [ ] Confirm SPH 300 has usable projector/HDMI + wifi (also hosts Wednesday's hands-on session).
- [ ] Have the `ssh netid@pegasus.arc.gwu.edu` command and the GW IT HPC access-request link ready to paste in the chat/LMS announcement right after class.
- [ ] Decide before Wednesday whether Docker access will be hands-on for everyone or conceptual-only for students without admin rights (separate open item, doesn't block Monday).
- [ ] Print or have this sheet open during the icebreaker and final-project slides — those are the two segments most likely to run long if discussion takes off.

## Still open (not blocking Monday, but coming due)
- Lab 1 submission mechanism still says "course LMS — TBD" in the lab doc; needed before Week 2.
- Final project presentation format/length still undecided (10-min talks? poster session?) — needed before Week 11, but worth having an answer ready in case a student asks during today's preview.
- PUBH 4201 (undergrad) final deliverable is a poster by default per the curriculum committee notes — the requirements doc I referenced today is written for the grad (6854) report standard; a short 4201 addendum isn't written yet. If undergrads ask for specifics beyond "poster vs. report," flag that the addendum is still coming.
