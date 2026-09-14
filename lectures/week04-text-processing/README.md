# Week 04 - Text Processing

A quickstart for regular expressions and parsing semi-structured health/genomic
text — the tool you reach for once your data isn't clean enough for a straight
CSV/JSON parser, but has enough of a pattern that AI-assisted extraction isn't
your only option either. Monday's lecture covers the regex fundamentals;
Wednesday's practical goes deep on AI-assisted extraction and how to
troubleshoot with AI, alongside hands-on regex practice.

No new installs this week — everything below uses tools you already have
(Python's built-in `re` module, R's built-in `stringr`/base regex, or any
text editor's find/replace) plus whichever AI assistant you're already using.

## Quick reference

| Token | Meaning | Example | Matches |
|---|---|---|---|
| `\d` | any digit | `\d+` | `142` |
| `\w` | letter, digit, or underscore | `gene=\w+` | `gene=BRCA1` |
| `\s` | whitespace | `exit=\d+\s` | `exit=1 ` |
| `.` | any character | `seq.\d+` | `seq0231` or `seqA231` |
| `+` | one or more | `\d+` | `1`, `42`, `14209` |
| `*` | zero or more | `\s*` | `''` or `'   '` |
| `?` | zero or one | `colou?r` | `color` or `colour` |
| `{n,m}` | between n and m | `\d{2,4}` | `12`, `142`, `1420` |
| `()` | capture a group | `gene=(\w+)` | captures `BRCA1` from `gene=BRCA1` |
| `^` `$` | start / end of string | `^\d+\.\d+$` | matches only if the *entire* string is a decimal |
| `[...]` | custom character set | `[\w-]+` | word characters *and* hyphens — needed for gene symbols like `HLA-DRB1` |

**Python:**
```python
import re
m = re.search(r"gene=([\w-]+)", header_line)
if m:
    gene = m.group(1)
```

**R:**
```r
library(stringr)
gene <- str_extract(header_line, "(?<=gene=)[\\w-]+")
```

**Command line (quick checks, not full extraction):**
```bash
grep -E 'gene=[A-Za-z0-9-]+' headers.fa
```

A browser-based regex tester (e.g. [regex101.com](https://regex101.com), set
to Python or PCRE flavor) is the fastest way to build a pattern incrementally
— write a little, test against real examples, adjust. That's the actual
workflow, not writing a perfect pattern in one pass.

## The one thing worth internalizing this week

**A pattern that looks right on one example can be quietly wrong on another.**
`\w+` looks perfect for a gene symbol until it meets `HLA-DRB1` and silently
truncates to `HLA` — no error, just a wrong answer. There's no shortcut around
this other than testing your pattern against more than one example, including
the ugly ones, before trusting it.

## AI-assisted extraction: what's coming Wednesday

Monday's lecture gives AI-assisted text extraction a quick preview — same
idea as regex, but you describe what you want instead of writing a pattern.
Wednesday's practical is where this gets real time: writing a good extraction
prompt, comparing AI output against your own regex output field-by-field, and
— just as important — **how to troubleshoot with AI critically**, not just
prompt it and trust whatever comes back. That last part matters because AI
extraction fails differently than regex does: not with an error message, but
with a confident, wrong answer. See "If something breaks" below for a preview
of the habit; Wednesday covers it properly.

## If something breaks

1. **Read the actual error, from the bottom up.** A regex error (`re.error`
   in Python, or a warning from `stringr`) usually names exactly what's
   malformed — an unbalanced parenthesis, an unescaped special character.
2. **Ask an AI assistant what the error means before asking it to fix it.**
   Paste the exact error text and the pattern you wrote — not a paraphrase.
   Understanding the error is worth more than a fixed pattern you don't
   understand, especially since you'll hit variations of the same mistake
   again.
3. **For a pattern that runs but gives the wrong answer** (the harder case,
   with no error message at all): test it against more than one example,
   including a deliberately messy one. This is the FASTA-header lesson from
   Monday's live-code demo, generalized.
4. **Document anything nonobvious you learn in `AI_USAGE.md`**, same as every
   other week.

## Required readings

- PCB Chapters 2–3 (Regular Expressions: Powerful Search and Replace;
  Exploring the Flexibility of Regular Expressions)
- DSF Chapter 5 (Operations on Dates, Strings, and Missing Data)

## Recommended readings

- [Python `re` module documentation](https://docs.python.org/3/library/re.html)
- Prompting guides for structured data extraction (linked in Wednesday's
  practical materials)
