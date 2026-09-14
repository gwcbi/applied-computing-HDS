# Week 4 Practical — Wednesday, Sep 16

Monday's lecture gave AI-assisted extraction a 5-minute preview on purpose —
this is where it gets real time. Today: regex hands-on, then a proper deep
dive into AI-assisted extraction and how to troubleshoot with AI, then a
head-to-head comparison using the same data.

**Data:** `inclass_headers.fasta` (this folder) — 9 messy FASTA headers, each
with sample ID, organism, and gene fields, formatted inconsistently on
purpose: pipe-delimited, colon-delimited, semicolon-delimited, and
space-separated variants; several headers missing a length field entirely
(one explicitly marked `len:NA`); and one hyphenated gene symbol
(`HLA-DRB1`). This is a different, smaller set than Lab 3's dataset
(`data/raw/lab3-messy-data/`) — today's answers won't just transfer over.

## Part 1 — Regex extraction (20 min)

Working in pairs, write regex patterns to extract three fields from every
header in `inclass_headers.fasta`:

1. **Sample ID** (e.g. `seq101`, `Seq102`, `seq-103` — note the
   inconsistent casing and punctuation)
2. **Organism** (mostly `Homo_sapiens` / `Homo sapiens` / `Hsapiens` —
   another inconsistency to handle or explicitly decide to ignore)
3. **Gene** (`KRAS`, `PTEN`, `TP53`, and one `HLA-DRB1` — the hyphen from
   Monday's live-code lesson shows up for real here)

Start from Monday's live-code pattern (`gene=([\w-]+)(?=;|\s|$)`) for the
gene field, but you'll need your own patterns for sample ID and organism —
those weren't built live on Monday. Test against **all nine** headers, not
just the first one or two — several are deliberately built to break a
pattern that only handles the "clean" cases.

**Checkpoint:** by the end of Part 1, you should have three working patterns
and a quick sanity check of each against the full file — not full production
code, just confidence that they hold up across all nine lines.

## Part 2 — Deep dive: AI-assisted extraction & troubleshooting with AI (25 min)

### Writing a real extraction prompt

A vague prompt ("extract the fields from this") gets a vague, inconsistent
answer. A good extraction prompt is specific about:

- **What fields you want, named explicitly** ("sample ID, organism, and gene
  symbol")
- **The exact input**, pasted in full — not summarized or retyped
- **The output format you want** (a table, a list of dictionaries, CSV) so
  you can actually compare it against your regex output
- **What to do with a missing field** (leave blank? mark `NA`? — decide this
  yourself, don't let the AI tool decide silently)

Compare, live as a class: "extract the fields from this file" vs. a prompt
built from the four points above, on the same two or three headers. The
difference in usefulness is usually immediate.

### The chat-vs-agentic distinction

Some AI tools just **explain** — they'll describe what a header contains and
you still do the extraction. Others can **act** — actually run code, produce
a file, or execute the extraction for you. Neither is strictly better, but
you need to know which one you're using: a tool that's explaining is a
starting point for your own regex or script; a tool that's acting is
producing output you need to verify, not just accept.

### The verification habit

This is the part that matters most, because **AI extraction fails
differently than regex does.** A broken regex either throws an error or
visibly extracts the wrong thing (like Monday's `HLA` truncation — wrong, but
noticeably short). AI extraction can fail with a completely confident,
well-formatted, wrong answer — a hallucinated field that was never in the
source text, or a "cleaned up" value that no longer matches what was
actually written. There is no error message for this.

**The habit:** for every field an AI tool extracts, spot-check it against
the actual source text before you trust it. Not every field, every time,
forever — but enough, especially early on, to know whether a given tool and
a given prompt style is reliable for this kind of data.

### How to troubleshoot with AI (the general version)

This generalizes past today's regex/extraction task — it's the same habit
that'll help whenever you're stuck this semester:

1. **Hand it the exact text** — the error message, the wrong output, the
   input that triggered it. Not a paraphrase ("it's not working right").
2. **Say what you've already tried.** Saves the tool from suggesting the
   same thing, and often surfaces the actual issue faster.
3. **Read before you run.** If an AI tool suggests a fix — a new regex, a
   code snippet — understand what it does before running it, the same
   discipline Week 2 taught for AI-suggested environment fixes.

## Part 3 — Hands-on: same task, via AI (15 min)

Using the prompting approach from Part 2, run all nine `inclass_headers.fasta`
headers through an AI tool and extract the same three fields (sample ID,
organism, gene).

Then, **field by field, compare your AI output against your Part 1 regex
output.** For each of the 27 field values (9 headers × 3 fields):

- Do they agree?
- If not, which one is actually right? (Go back to the source text — this is
  the verification habit from Part 2, applied for real.)
- Is there a pattern to where they disagree? (Hint: check the `HLA-DRB1` row
  and the row with the missing length field particularly closely.)

## Discussion (5 min)

When would you reach for regex vs. AI on a new extraction task you haven't
seen before? There's no single right answer — the point is to leave with a
real basis for that decision, not just "AI is easier" or "regex is more
reliable" as a slogan.

## Wrap-up

| | |
|---|---|
| **Due tonight, 11:59pm** | Lab 2: Analysis Notebook |
| **Next week** | Lab 3: Parsing Messy Health or Genomic Data (assigned Week 5, due Sep 30) — builds directly on today, with a new dataset |
| **Keep for later** | The prompting checklist and troubleshoot-with-AI steps above apply well beyond text extraction — worth remembering for Week 7 (AI-assisted debugging) and Week 8 (AI-assisted SQL) |
