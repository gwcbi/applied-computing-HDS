# Week 4: Text Processing

**Lecture:** Sep 14 · **Practical:** Sep 16 · **Module 1**

## Required readings

- PCB Chapters 2–3
- DSF Chapter 5

## Recommended readings

- Python `re` documentation
- Prompting guides for structured data extraction

## Learning objectives (from syllabus)

- Clean real-world health data
- Compare classical and AI-based parsing approaches
- Identify failure modes in automated tools

## Lecture outline

1. **Regular expressions from first principles** (25 min) — literal chars,
   character classes, quantifiers, groups, anchors. Use *health/genomic*
   examples throughout, not generic string examples (e.g., matching a lab
   value with units, matching a FASTA header field).
2. **Parsing semi-structured files** (20 min) — FASTA format, metadata
   files, log files as running examples. Show that "semi-structured" means
   there's a pattern, but it's not as rigid as CSV/JSON — hence regex
   rather than a straight parser.
3. **Live-code: build a regex parser incrementally** (20 min) — start
   naive, break it on an edge case, refine. This mirrors the actual
   experience of writing regex and normalizes iterating rather than
   getting it right the first time.
4. **AI-assisted text extraction** (15 min) — same task, done by prompting
   an AI assistant; compare output side by side with the regex approach
   live. Directly previews Lab 3's comparison structure.
5. **Failure modes** (10 min) — where both regex and AI extraction
   predictably break (ambiguous free text, inconsistent delimiters,
   AI hallucinating a field that isn't there).

## Hands-on exercise (in class, ungraded)

Extract structured fields (e.g., sample ID, organism, gene) from a handful
of messy FASTA headers using both regex and an AI tool — a lighter-weight
version of Lab 3's task, done live/in pairs.

## Connections

Directly scaffolds **Lab 3 (Parsing Messy Health or Genomic Data)**, due
Week 5 — this week's in-class exercise should use a *different* small
sample than the Lab 3 dataset (`data/raw/lab3-messy-data/`) so the lab
isn't just a repeat of the in-class answer.

## Open item

Need a small in-class-only messy-text sample distinct from the Lab 3
dataset — not yet created (quick to generate from the same script pattern
used for Lab 3 if needed).
